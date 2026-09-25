from crewai import Agent , LLM
import os
import os
from dotenv import load_dotenv
from tools import file_tool , search_tool , file_writer_tool


#load env setup
load_dotenv()

#setupLLM
llm = LLM(
    model="gemini/gemini-3.5-flash-lite",
    temperature=0.2
)
#setup agent1
# ─────────────────────────────────────
# Agent 1 — Reader
# ─────────────────────────────────────
reader_agent = Agent(
    role="File Reader",
    goal="Read and extract information from files",
    llm=llm,
    backstory="An assistant skilled at reading and interpreting file contents.",
    tools=[file_tool] ,
    verbose=True
)

#setupagent2
# ─────────────────────────────────────
# Agent 2 — Researcher
# ─────────────────────────────────────
researcher_agent = Agent(
    role="Senior Research Analyst",
    goal="""Research the topic from input file
            thoroughly using web search.
            Find latest trends, opportunities,
            challenges and real world examples.
            Provide comprehensive research report.""",
    backstory="""You are a world class research analyst
                 who has conducted research for Fortune 500
                 companies. You know exactly what to search
                 for and how to find the most relevant and
                 latest information. You always search
                 multiple angles of a topic.""",
    llm=llm,
    tools=[search_tool],
    verbose=True
)

#setupagent3
# ─────────────────────────────────────
# Agent 3 — Idea Generator
# ─────────────────────────────────────
idea_generator_agent = Agent(
    role="Innovation and Strategy Expert",
    goal="""Using the input file requirements
            and research findings, generate
            exactly 5 unique, practical and
            detailed ideas. Each idea must be
            specific, actionable and well
            thought out with full details.""",
    backstory="""You are a renowned innovation expert
                 who has helped 200+ companies generate
                 breakthrough ideas. You combine deep
                 research with creative thinking and
                 practical business knowledge to produce
                 ideas that are both innovative and
                 implementable. You think from multiple
                 perspectives.""",
    llm=llm,
    verbose=True
)

#setupagent3
# ─────────────────────────────────────
# Agent 4 — File creator agent
# ─────────────────────────────────────
file_creator_agent = Agent(
    role="Document Creator and File Manager",
    goal="""Take all 5 ideas from Idea Generator.
            Create a detailed professional document
            for each idea and save each one to
            its own file with datetime stamp.
            Then create a master list file.
            Confirm all files are saved.""",
    backstory="""You are an expert technical writer
                 and file management specialist.
                 You create professional documents
                 that are clear, detailed and well
                 structured. You always save files
                 with proper timestamps and confirm
                 every upload. You never miss saving
                 any file.""",
    llm=llm,
    tools=[
     file_writer_tool
    ],
    verbose=True
)