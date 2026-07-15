from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    provider="featherless-ai",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

st.header("Reasearch Tool")

paper_input = st.selectbox("select Research paper Name", ["Attention Is All You Need", "BERT : Pre-training of Deep Bildirectional Transformers", "GPT-3: language models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Syanthesis"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium(3-5 Paragraphs)", "Long(detailed explanation)"])

template = load_prompt("template.json")


if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({
        "paper_input" : paper_input,
        "style_input" : style_input,
        "length_input": length_input
    })
    st.write(result.content)
