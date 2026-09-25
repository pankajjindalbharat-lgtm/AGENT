import os
from crewai import Crew
from agents import reader_agent ,researcher_agent ,idea_generator_agent  , file_creator_agent 
from tasks  import all_tasks
from dotenv import load_dotenv

#setting environment variables
load_dotenv()


#Settingup crew
crew = Crew(
    agents=[reader_agent , researcher_agent , idea_generator_agent , file_creator_agent ],
    tasks=[all_tasks],
    verbose=True
)

#SEtting yo the main method
def main():
#print _ 60 times
    print("Welcome to my first hand written crew")
    result = crew.kickoff(inputs = {"path" : "input.txt"}) 
    print("Hey its done")
    print("Result is" , result)

if __name__ == "__main__":
    main()

