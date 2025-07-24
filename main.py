from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor

from tools import save_tool

load_dotenv()

class MeetingSummary(BaseModel):
    meeting_topic: str
    summary: str
    action_items: list[str]
    participants: list[str]

llm = ChatOpenAI(model="gpt-4o-mini")

parser = PydanticOutputParser(pydantic_object=MeetingSummary)

input_understanding = """
You are an AI assistant that summarizes meeting transcripts.
You take the raw meeting discussion text and identify the main discussion points.
"""

state_tracker = """
Retain information such as previous summaries or recurring participants if given.
Current context: {chat_history}
"""

task_planner = """
Analyze the transcript, summarize the key decisions and topics, and extract action items.
List participants if mentioned.
"""

output_generator = """
Respond in structured format using the following schema:
{format_instructions}
Avoid unnecessary text outside the output.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", input_understanding + "\n" + task_planner + "\n" + output_generator),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),
]).partial(format_instructions=parser.get_format_instructions())

tools = [save_tool]

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
with open("meeting_transcript.txt", "r", encoding="utf-8") as f:
    query = f.read()

raw_response = agent_executor.invoke({"query": query})
print("\n--- Raw Response ---\n", raw_response)

try:
    structured_response = parser.parse(raw_response.get("output"))
    print("\n--- Meeting Summary ---\n", structured_response)
except Exception as e:
    print("Error parsing response:", e, "\nRaw Output:", raw_response)