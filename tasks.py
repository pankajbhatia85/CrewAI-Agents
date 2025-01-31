from crewai import Task
from tools import search_tool,pdf_tool_path,PDFSearchTool
from agents import reader_agent, search_agent, professional_writer_agent


file_path=pdf_tool_path()
pdf_tool = PDFSearchTool(pdf=file_path)
answer_customer_question_task = Task(
    description=(
        """
        Answer the customer's questions based on the home inspection PDF.
        The research agent will search through the PDF to find the relevant answers to user query.
        Your final answer MUST be clear and accurate, based on the content of the home inspection PDF.

        Here is the customer's question:
        {customer_question}
        """
    ),
    expected_output="""
        Provide clear and accurate answers to the customer's questions based on 
        the content of the home inspection PDF.
        """,
    tools=[pdf_tool],
    agent=reader_agent,
)

write_email_task = Task(
    description=(
        """
        - Write a professional email to a contractor based 
            on the Reader agent findings.
        -The email must include the property address
        - The email should clearly state the issues found in the specified section 
            of the report and request a quote or action plan for fixing these issues.
        - Ensure the email is signed with the following details:
        
            Best regards,

            Pankaj Bhatia,
            """
    ),
    expected_output="""
        Write a clear and concise email that can be sent to a contractor to address the 
        issues found in the home inspection report.
        """,
    tools=[],
    agent=professional_writer_agent
)