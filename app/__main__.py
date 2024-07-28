import os
import autogen
from autogen import AssistantAgent, UserProxyAgent
from app.examples.multi_agent_conversation import multi_agent_example
from app.examples.docker_code_execution import docker_code_execution_example
from app.examples.docker_code_execution_v2 import docker_code_execution_example_v2

# llm_config = {"model": "gpt-4o-mini", "api_key": os.environ["OPENAI_API_KEY"]}
# assistant = AssistantAgent("assistant", llm_config=llm_config)

# user_proxy = UserProxyAgent(
#     "user_proxy", code_execution_config={"executor": autogen.coding.LocalCommandLineCodeExecutor(work_dir="coding")}
# )

# # Start the chat
# user_proxy.initiate_chat(
#     assistant,
#     message="Plot a chart of NVDA and TESLA stock price change YTD.",
# )

def main():
    # multi_agent_example()
    docker_code_execution_example_v2()
    
main()