from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    provider="featherless-ai",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

template2 = PromptTemplate(
    template="Greet the person named {name} in exactly 5 different languages. For each language, write the language name followed by the greeting.",
    input_variables=["name"]
)

prompt = template2.invoke({"name" : "Raj"})

result = model.invoke(prompt)

print(result.content)
