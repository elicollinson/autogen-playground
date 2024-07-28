from autogen.coding import DockerCommandLineCodeExecutor
from autogen import ConversableAgent
import tempfile
import os
import datetime
from app.config.config import settings
    
def docker_code_execution_example_v2():

    # Create a temporary directory to store the code files.
    temp_dir = tempfile.TemporaryDirectory()
    
    # Create a Docker command line code executor.
    executor = DockerCommandLineCodeExecutor(
        image=settings.EXECUTION_IMAGE,  # Execute code using the given docker image name.
        timeout=int(settings.EXECUTION_TIMEOUT),  # Timeout for each code execution in seconds.
        work_dir=temp_dir.name,  # Use the temporary directory to store the code files.
    )

    code_writer_agent = ConversableAgent(
        "code_writer_agent",
        system_message=settings.CODE_WRITER_SYSTEM_MESSAGE,
        llm_config={"config_list": [{"model": settings.MODEL, "api_key": settings.OPENAI_API_KEY}]},
        code_execution_config=False,  # Turn off code execution for this agent.
    )
    
    # Create an agent with code executor configuration that uses docker.
    code_executor_agent_using_docker = ConversableAgent(
        "code_executor_agent_docker",
        llm_config=False,  # Turn off LLM for this agent.
        code_execution_config={"executor": executor},  # Use the docker command line code executor.
        human_input_mode="ALWAYS",  # Always take human input for this agent for safety.
    )

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    chat_result = code_executor_agent_using_docker.initiate_chat(
        code_writer_agent,
        message=f"Today is {today}. Write Python code to plot TSLA's and META's "
        "stock price gains YTD, and save the plot to a file named 'stock_gains.png'.",
    )
    
