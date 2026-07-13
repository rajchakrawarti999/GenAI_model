from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = "Sentence-transformers/all-MiniLm-L6-v2")

documents = [

    "Delhi is the capital of India ",
    "kolakata is the capital of west bengal",
    "paris is the capital of France"
]

result = embedding.embed_documents(documents)