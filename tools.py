from crewai import LLM
from crewai_tools import PDFSearchTool
from crewai_tools import SerperDevTool


llm = LLM(
    model="gpt-4",
    temperature=0.8,
    max_tokens=150)
# Initialize the tool allowing for any PDF content search if the path is provided during execution
#Tool 1
pdf_tool = PDFSearchTool()

#Tool 2
search_tool= SerperDevTool(n=3)