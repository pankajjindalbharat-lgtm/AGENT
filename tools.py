# tools.py
# All tools in one place

from crewai_tools import FileReadTool
from crewai_tools import SerperDevTool
from crewai_tools import FileWriterTool


# Initialize tools
file_tool   = FileReadTool()
search_tool = SerperDevTool()
file_writer_tool = FileWriterTool()  # or FileWriterTool(base_dir='/var/output') to allow writes outside cwd
