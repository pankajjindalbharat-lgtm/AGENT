from crewai import Task
import os
from dotenv import load_dotenv
from agents import reader_agent , researcher_agent , idea_generator_agent ,file_creator_agent


#load task1


# ─────────────────────────────────────
# Task 1 — Read Input File
# ─────────────────────────────────────
read_file_task = Task(
    description="""
    Read the input file at: {input_file}

    Use read_input_file tool to read it.

    Extract and structure:
    1. Main topic
    2. Background information
    3. Focus areas
    4. Target audience
    5. Any specific requirements
    6. Expected outcomes

    Provide complete structured summary
    so other agents can use this info.
    """,
    expected_output="""
    Structured document containing:
    - TOPIC: (main topic)
    - BACKGROUND: (context)
    - FOCUS AREAS: (list)
    - TARGET AUDIENCE: (who it is for)
    - REQUIREMENTS: (specific needs)
    - EXPECTED OUTPUT: (what is needed)
    """,
    agent=reader_agent
)
#load task2

# ─────────────────────────────────────
# Task 2 — Research the Topic
# ─────────────────────────────────────
research_task = Task(
    description="""
    Using the topic and focus areas from
    the input file reading, do thorough research.

    Search for:
    1. Latest trends in this area
    2. Current challenges and problems
    3. Market opportunities
    4. Real world examples and case studies
    5. What experts are saying
    6. Future predictions
    7. Technologies and tools available
    8. Competitors and existing solutions

    Do at least 5 different searches
    to cover all angles of the topic!
    """,
    expected_output="""
    Comprehensive research report with:
    - Topic overview
    - Latest trends (minimum 5)
    - Key challenges (minimum 3)
    - Market opportunities (minimum 5)
    - Real world examples (minimum 3)
    - Expert opinions
    - Future outlook
    - Relevant technologies
    - All sources used
    """,
    agent=researcher_agent,
    context=[read_file_task]
)

#load task3
# ─────────────────────────────────────
# Task 3 — Generate Ideas
# ─────────────────────────────────────
generate_ideas_task = Task(
    description="""
    Using BOTH:
    - Input file requirements (from Task 1)
    - Research findings (from Task 2)

    Generate exactly 5 unique ideas.

    For EACH idea provide:

    IDEA [NUMBER]:
    TITLE: [catchy title]
    ONE LINE: [single sentence summary]
    PROBLEM: [what problem it solves]
    SOLUTION: [how it solves it]
    TARGET: [who will use it]
    UNIQUENESS: [why it is different]
    IMPACT: [what difference it makes]
    DIFFICULTY: [Easy/Medium/Hard]
    TIME TO BUILD: [estimate]

    Make ideas:
    → Specific and actionable
    → Based on real research
    → Relevant to the topic
    → Practical to implement
    → Different from each other
    """,
    expected_output="""
    Exactly 5 detailed ideas in format:

    IDEA 1:
    TITLE: ...
    ONE LINE: ...
    PROBLEM: ...
    SOLUTION: ...
    TARGET: ...
    UNIQUENESS: ...
    IMPACT: ...
    DIFFICULTY: ...
    TIME TO BUILD: ...

    IDEA 2: ...
    (repeat for all 5)
    """,
    agent=idea_generator_agent,
    context=[
        read_file_task,
        research_task
    ]
)


# ─────────────────────────────────────
# Task 4 — Create and Upload Files
# ─────────────────────────────────────
create_files_task = Task(
    description="""
    Take ALL 5 ideas from previous task.

    For EACH idea (do this 5 times!):

    STEP 1: Create detailed document with:
    - Full description (minimum 200 words)
    - Problem statement
    - Proposed solution
    - Target audience
    - Key features (minimum 5)
    - Implementation steps (numbered)
    - Required technologies/tools
    - Timeline estimate
    - Expected outcomes
    - Potential challenges
    - Success metrics
    - Why this idea is unique

    STEP 2: Save using save_idea_file tool
    Pass this JSON:
    {{
        "idea_number": [1-5],
        "title": "[idea title]",
        "topic": "[main topic from input file]",
        "content": "[full detailed content]"
    }}

    STEP 3: After saving ALL 5 ideas:
    Create master list using save_ideas_list_file:
    {{
        "topic": "[main topic]",
        "ideas": [
            {{
                "title": "idea 1 title",
                "summary": "one line summary",
                "filename": "saved filename",
                "timestamp": "datetime"
            }}
        ],
        "files_created": ["file1", "file2"...]
    }}

    STEP 4: List all output files to confirm
    Use list_output_files with "output"

    IMPORTANT:
    → Save ALL 5 ideas - do not skip any!
    → Each idea gets its own file
    → Include datetime in every file
    """,
    expected_output="""
    Complete upload confirmation:
    - 5 individual idea files created ✅
    - 1 master list file created ✅
    - All files have datetime stamps ✅
    - List of all created files
    - Any errors encountered
    """,
    agent=file_creator_agent,
    context=[
        read_file_task,
        generate_ideas_task
    ]
)


# All tasks in order
all_tasks = [
    read_file_task,
    research_task,
    generate_ideas_task,
    create_files_task
]