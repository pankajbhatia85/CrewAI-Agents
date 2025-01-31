from crewai import Crew,Process
from crewai_tools import SerperDevTool
#from dotenv import load_dotenv
#from tools import pdf_tool,search_tool,llm
from tasks import answer_customer_question_task,write_email_task
from agents import reader_agent, search_agent, professional_writer_agent
from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
from typing import Optional
import uvicorn
import os
#load_dotenv()
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")

#customer_question = input(
#    "Which section of the report would you like to generate a work order for?\n"
#)
#result = crew.kickoff(inputs={"customer_question": customer_question})

# Initialize FastAPI app
app = FastAPI()

# Request model for structured inputs
class CustomerQuery(BaseModel):
    customer_question: str

@app.post("/process_query/")
async def process_query(
    customer_question: str = Form("Enter section e.g roof, kitchen,appliances to generate report..."),
    file: UploadFile = File(...)
):
    """
    Endpoint to process a customer query and a PDF file.

    Parameters:
    - customer_question: The question provided by the user based on uploaded pdf.
    - file: The PDF file uploaded by the user.

    Returns:
    - The result from the Crew process.
    """
    current_path = os.getcwd()  # Always returns a valid string
    file_name = file.filename

    # Validate file_name
    if not file_name:
        return {
            "success": False,
            "error": "No file name provided. Please upload a valid file."
        }

    # Construct the file path
    file_path = os.path.join(current_path, file_name)
    try:
        if not file_path.endswith(".pdf"):
            return {
                "success": False,
                "error": "Uploaded file is not a PDF. Please upload a valid .pdf file."
            }
        # Read the file content
        

        with open(file_path, "wb") as f:
            f.write(await file.read())
        crew = Crew(
        agents=[reader_agent,search_agent,professional_writer_agent],
        tasks=[answer_customer_question_task, write_email_task],
        process=Process.sequential,
        )
        # Kickoff the Crew process with inputs
        result = crew.kickoff(inputs={
            "customer_question": customer_question
        })

        # Delete the file after processing
        os.remove(file_path)

        return {
            "success": True,
            "result": result
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# Run FastAPI app using uvicorn if needed
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
