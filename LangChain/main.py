## Integrate our code OpenAI API

from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.memory import ConversationBufferMemory

from langchain.chains import SequentialChain

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
openai_key = os.getenv('API_KEY')
os.environ["OPENAI_API_KEY"]= openai_key

# streamlit framework
st.title('LangChain With OpenAI API')
input_text=st.text_input("Search the topic")

# Memory
title_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')
launch_memory = ConversationBufferMemory(input_key='launch', memory_key='chat_history')
feature_memory = ConversationBufferMemory(input_key='feature', memory_key='description_history')

## OPENAI LLM
llm=OpenAI(temperature=0.8)


# first Prompt Template
first_input_prompt=PromptTemplate(
    input_variables=['name'],
    template="Tell me about {name}"
)
chain=LLMChain( llm=llm, prompt=first_input_prompt, verbose=True, output_key='title', memory=title_memory)

# second Prompt Template
second_input_prompt=PromptTemplate(
    input_variables=['title'],
    template="when was {title} launch"
)
chain2=LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='launch', memory=launch_memory)

# third  Prompt Templates
third_input_prompt=PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major features {title} in the world"
)
chain3=LLMChain(llm=llm,prompt=third_input_prompt,verbose=True,output_key='features',memory=feature_memory)

# Creating sequenceChain
parent_chain=SequentialChain(chains=[chain,chain2,chain3],input_variables=['name'],output_variables=['title','launch','features'],verbose=True)



if input_text:
    st.write(parent_chain({'name':input_text}))

    with st.expander('Launch '):
        st.info(launch_memory.buffer)

    with st.expander('Major Features'):
        st.info(feature_memory.buffer)

## ChatModels with OpenAI

from langchain.chat_models import  ChatOpenAI
from langchain.schema import HumanMessage,SystemMessage,AIMessage

## OPENAI LLM
ChatModelllm=ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"],temperature=0.8,model="gpt-3-5-turbo")
ChatModelllm

## Create a schema
ChatModelllm([
    SystemMessage(content="You are a code Generator AI"),
    HumanMessage(content="Give me a code for Binary Search Tree using JAVA")
 ])