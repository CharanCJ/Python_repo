import os
import pandas as pd
from dotenv import load_dotenv
from llama_index.experimental.query_engine import PandasQueryEngine
from prompt import new_prompt, instruction_str, context
from note_engine import note_engine 
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from pdf import India_engine

load_dotenv()

population_path = os.path.join("data","WorldPopulation2023.csv")
population_df = pd.read_csv(population_path)
print(population_df.head(5))

population_query_engine = PandasQueryEngine(df=population_df, verbose=True, instruction_str=instruction_str)

population_query_engine.update_prompts({"pandas_prompt": new_prompt})
#population_query_engine.query("What is the population of India") will query directly the source

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name = "population_data",
            description = "this gives information for the world population and demographics",
        )
    ),
     QueryEngineTool(
        query_engine=India_engine,
        metadata=ToolMetadata(
            name = "India_data",
            description = "this gives information about the country called India",
        ),
    ),
]

llm = OpenAI(model="gpt-3.5-turbo-16k")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt(q to quit):")) !="q":
    result = agent.query(prompt)
    print(result)
