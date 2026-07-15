# GenAI Model 🚀

A collection of hands-on GenAI experiments and mini-projects built while learning LangChain, LLMs, embeddings, and prompt engineering.

## 📂 Project Structure

```
GenAI_model/
│
├── ChatModel/
│   ├── 1_chatmodel_openai.py       # Chat model using OpenAI
│   ├── 2_chatmodel_anthropic.py    # Chat model using Anthropic (Claude)
│   ├── 3_chatModel_google.py       # Chat model using Google (Gemini)
│   ├── 4_chatmodel_hf_api.py       # Chat model using HuggingFace API
│   └── 5_chatmodel_hf_local.py     # Chat model using local HuggingFace model
│
├── EmbeddingModels/
│   ├── 1_embedding_openai_query.py # OpenAI embeddings for a single query
│   ├── 2_embedding_openai_docs.py  # OpenAI embeddings for multiple documents
│   └── 3_embedding_hf_api.py       # HuggingFace API embeddings
│
├── LLms/
│   └── 1_llm.py                    # Basic LLM usage example
│
├── Prompt/
│   ├── prompt_template.py          # Reusable prompt template logic
│   ├── prompt_ui.py                # Streamlit app: Research Paper Explanation Tool
│   └── template.json               # Saved prompt template
│
├── requirements.txt
└── test.py
```

## 🧠 Featured Project: Research Paper Explanation Tool

Located in the `Prompt/` folder — a Streamlit-based tool that explains research papers based on user preferences.

**Features:**
- Select a research paper (e.g., *Attention Is All You Need*)
- Choose an explanation style (Beginner-Friendly, Technical, etc.)
- Choose explanation length (Short, Medium, Long)
- Uses a LangChain prompt template + HuggingFace LLM to generate a tailored explanation

**Run it locally:**
```bash
cd Prompt
streamlit run prompt_ui.py
```

## ⚙️ Setup

1. Clone the repo
   ```bash
   git clone https://github.com/rajchakrawarti999/GenAI_model.git
   cd GenAI_model
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your API keys:
   ```
   OPENAI_API_KEY=your_key_here
   ANTHROPIC_API_KEY=your_key_here
   GOOGLE_API_KEY=your_key_here
   HUGGINGFACEHUB_API_TOKEN=your_key_here
   ```

## 🛠️ Tech Stack

- **LangChain** — LLM orchestration & prompt templates
- **Streamlit** — Interactive UI
- **OpenAI / Anthropic / Google / HuggingFace** — LLM & embedding providers
- **python-dotenv** — Environment variable management

## 📌 Notes

This repo is a learning-in-progress collection — each folder explores a different building block of GenAI application development (chat models, embeddings, LLMs, and prompt engineering), leading up to the complete Streamlit tool in `Prompt/`.

## 📄 License

This project is for educational purposes.
