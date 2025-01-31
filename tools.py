from crewai import LLM
from crewai_tools import PDFSearchTool
from crewai_tools import SerperDevTool
import os

llm = LLM(
    model="gpt-3.5-turbo",
    temperature=0.8,
    max_tokens=150)
# Initialize the tool allowing for any PDF content search if the path is provided during execution
#Tool 1
def pdf_tool_path():
    # Get the current directory
    current_directory = os.getcwd()
   # Find the single PDF file
    pdf_files = [file for file in os.listdir(current_directory) if file.endswith('.pdf')]
    if pdf_files:
     file_path = os.path.abspath(os.path.join(current_directory, pdf_files[0]))
     return file_path
    else:
       file_path=None
       return file_path

file_path=pdf_tool_path()
pdf_tool = PDFSearchTool(pdf=file_path)
   

#Tool 2
search_tool= SerperDevTool(n_results=3)