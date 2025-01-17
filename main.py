from crewai import Crew,LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from tools import pdf_tool,search_tool,llm
from agents import reader_agent, search_agent, professional_writer_agent
import os
load_dotenv()




crew = Crew(
    agents=[research_agent, professional_writer_agent],
    tasks=[answer_customer_question_task, write_email_task],
    process=Process.sequential,
)

customer_question = input(
    "Which section of the report would you like to generate a work order for?\n"
)
result = crew.kickoff(inputs={"customer_question": customer_question})