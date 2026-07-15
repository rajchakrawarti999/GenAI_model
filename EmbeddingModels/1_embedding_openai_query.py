from langchain_openai import openAIEmbeddings
from dotenv import load_dotenv

embedding = openAIEmbeddings(model="text-embedding-3-large" , dimensions = 32)

result = embedding.embed_query("Delhi is the capital of india")

print(str(result))