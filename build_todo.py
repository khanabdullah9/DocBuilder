from typing import Union, List, Annotated, Sequence, TypedDict
from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, BaseMessage, SystemMessage, AIMessage
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode

from utils import get_sample_prompt_response

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    api_key = API_KEY,
    temperature = 0
)

@tool
def write_markdown(content: str) -> str:
    """
        Writes LLM generated content in a md file
        :param content: LLM generated content
        :return: str
        """
    with open("TODO.md","w") as md:
        md.write(content)

    return "content written!"

tools_list = [write_markdown]
llm = llm.bind_tools(tools_list)

class AgentState(TypedDict):
    messages: Annotated[
        Sequence[BaseMessage], add_messages
    ]

def model_call(state: AgentState) -> AgentState:
    example_prompt, example_response = get_sample_prompt_response()
    sys_msg = SystemMessage(content = f"""
        You are a helpful assistant!
        You are supposed to create a todo plan for another LLM agent to follow and create a word doc based on the user prompt.
        You and the other agent will receive the same user prompt
        
        You have one tool: write_markdown
        Never call any other tool
        
        Other agent has these tools: read_markdown, write_content, write_paragraph, write_bullet_points, write_ordered_list, write_table, save_doc
            write_paragraph: write only paragraph to the document
            write_bullet_points: add bullet points in the document
            write_ordered_list: add order points in the document
            write_table: add a table in the document
            save_doc: save the doc
        You are supposed to give instructions to the agent when to call which tool      
        
        example prompt: {example_prompt}
        example response: {example_response}
        
        Do not search the web for any data, just answer with your knowledge.
        
        You are expected to return markdown formatted content
    """)
    response = llm.invoke(
        [sys_msg] + state["messages"]
    )
    return dict(
        messages = [response]
    )

def should_continue(state: AgentState) -> str:
    messages = state["messages"][-1]
    if isinstance(messages, AIMessage) and messages.tool_calls:
        return "tool_node"

    return "stop"

graph = StateGraph(AgentState)

graph.add_node("model_call", model_call)
tool_node = ToolNode(tools = tools_list)
graph.add_node("tool_node", tool_node)

graph.add_edge(START, "model_call")
graph.add_conditional_edges("model_call",
                            should_continue,
                            {
                                "tool_node": "tool_node",
                                "stop": END
                            })
graph.add_edge("tool_node", END)

app = graph.compile()

while True:
    user_input = input("Enter: ")
    if user_input.strip() == "q":
        break

    try:
        app.invoke(dict(
            messages=[("user", user_input)]
        ))
        print("TODO generated!")
    except Exception as err:
        print(f"[ERR]: {str(err)}")
