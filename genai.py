import streamlit as st
from langchain.llms import Cohere
from langchain import PromptTemplate, LLMChain
import random


chat_template = """You are an empathetic AI counselor providing emotional support. Feel free to share your feelings. Your prompt is: {emotion}"""
chat_prompt = PromptTemplate(template=chat_template, input_variables=["emotion"])
llm_chat = Cohere(cohere_api_key='MGaK571I9pL2gPqUek9NevPhzl0taS9fERTvusEU')
llm_chain_chat = LLMChain(prompt=chat_prompt, llm=llm_chat)


motivation_template = """You are an empathetic AI counselor providing motivational quotes. Here's a quote for you: {quote}"""
motivation_prompt = PromptTemplate(template=motivation_template, input_variables=["quote"])
llm_motivation = Cohere(cohere_api_key='MGaK571I9pL2gPqUek9NevPhzl0taS9fERTvusEU')
llm_chain_motivation = LLMChain(prompt=motivation_prompt, llm=llm_motivation)

def main():
    st.title("Emotional Counseling Chatbot")
    
    st.sidebar.header("Options")
    option = st.sidebar.radio("Choose an option", ["Chat", "Motivation"])
    
    if option == "Chat":
        chat()
    elif option == "Motivation":
        motivation()

def chat():
    st.subheader("Chat with the Counselor")
    user_input = st.text_input("You: How are you feeling today?")
    
    if user_input.lower() == "exit":
        st.write("Counselor: Take care. Remember, I'm here if you need to talk.")
    else:
        response = llm_chain_chat.run(user_input)
        st.write("Counselor:", response)

def motivation():
    st.subheader("Get Motivated")
    
    generated_quote = llm_chain_motivation.run("")
    st.write("Counselor:", generated_quote)

if __name__ == "__main__":
    main()
