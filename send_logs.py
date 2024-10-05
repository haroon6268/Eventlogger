from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from get_logs import get_logs

# Load enviroment Variables
load_dotenv()

# Grab OpenAI Key
key = os.getenv("OPEN_API_KEY")

# Create OpenAI Client
llm = ChatOpenAI(api_key=key)

# Grab System Logs
system_logs = get_logs("System")

# Grab Application Logs
app_logs = get_logs("Application")

# Get Setup Logs
setup_logs = get_logs("Setup")

logs = setup_logs + app_logs + system_logs

class Output(BaseModel):
    isSuspicous: str = Field(description="Should return either Good or Warning depending on if file is suspicous")
    description: str = Field(description="Describe why you think it is suspicous")

parser = JsonOutputParser(pydantic_object=Output)
# Create Prompt
prompt = PromptTemplate(
    template="You are a cybersecurity expert who is recieving an event log file from the user. Answer the user query. \n{format_instructions}\n{input}\n",
    input_variables=["query"],
    partial_variables={"format_instructions":parser.get_format_instructions()}
)

chain = prompt | llm | parser


def send_system_logs(label_var, label):
    label_var.set("Loading...")
    label.update()
    logs = get_logs("System")
    result = chain.invoke({"input": logs})
    isSuspicous = result.get('isSuspicous', "Error")
    label_var.set(isSuspicous)
    description = result.get('description', "Error")
    print("System: " + description)
def send_setup_logs(label_var, label):
    label_var.set("Loading...")
    label.update()
    logs = get_logs("Setup")
    result = chain.invoke({"input":logs})
    isSuspicous = result.get('isSuspicous', "Error")
    label_var.set(isSuspicous)
    description = result.get('description', "Error")
    print("Setup: " + description)

def send_app_logs(label_var, label):
    label_var.set("Loading...")
    label.update()
    logs = get_logs("Application")
    result = chain.invoke({"input":logs})
    isSuspicous = result.get('isSuspicous', "Error")
    label_var.set(isSuspicous)
    description = result.get('description', "Error")
    print("Application: " + description)


