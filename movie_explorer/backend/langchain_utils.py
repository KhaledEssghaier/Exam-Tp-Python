from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from pathlib import Path

# Explicitly load .env from backend directory
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

def generate_summary_prompt(movie):
    actors_str = ", ".join([actor.actor_name for actor in movie.actors])
    prompt_text = (
        "Generate a short, engaging summary for the movie '{title}' ({year}), "
        "directed by {director} and starring {actors}."
    )
    return prompt_text.format(
        title=movie.title,
        year=movie.year,
        director=movie.director,
        actors=actors_str
    )

def get_summary_llm(movie):
    llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="meta-llama/llama-guard-4-12b")
    prompt_template = PromptTemplate.from_template(
        "Generate a short, engaging summary for the movie '{title}' ({year}), directed by {director} and starring {actors}."
    )
    chain = LLMChain(llm=llm, prompt=prompt_template)

    actors_str = ", ".join([actor.actor_name for actor in movie.actors])
    return chain.run({
        "title": movie.title,
        "year": movie.year,
        "director": movie.director,
        "actors": actors_str
    })
