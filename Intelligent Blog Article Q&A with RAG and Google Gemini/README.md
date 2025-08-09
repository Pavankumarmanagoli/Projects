# Intelligent Blog Article Q&A with RAG and Google Gemini

## Overview
This project showcases a retrieval-augmented generation (RAG) pipeline that answers questions about a technical blog post. The system scrapes the article, indexes it in a vector store, and uses Google's Gemini 1.5 Pro to produce grounded responses.

## Features
- Automated web scraping and cleaning of blog content
- Text chunking and embedding with Google Generative AI `embedding-001`
- Semantic retrieval using a Chroma vector store
- Context-aware answer generation through LangChain and Gemini
- Jupyter notebook demonstrating the end-to-end workflow

## Architecture
1. **Web Scraping** – `WebBaseLoader` retrieves and parses the target article with BeautifulSoup.
2. **Chunking & Embedding** – `RecursiveCharacterTextSplitter` prepares text for `GoogleGenerativeAIEmbeddings`.
3. **Vector Store** – Chroma stores embeddings for similarity search.
4. **Retrieval & Generation** – Relevant chunks are fetched via LangChain and supplied to Gemini-1.5-Pro.
5. **Question Answering** – Gemini generates responses grounded in the retrieved context.

## Getting Started

### Prerequisites
- Python 3.10+
- Google API key
- LangChain API key (optional for tracing)

### Installation
```bash
pip install --upgrade langchain langchain-community langchainhub langchain-chroma beautifulsoup4
pip install -q langchain_google_genai
```

### Environment Variables
```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = "your_langchain_api_key"
os.environ["GOOGLE_API_KEY"] = "your_google_api_key"
os.environ["LANGCHAIN_PROJECT"] = "RAG"
```

### Run the Demo
Open `RAG_Project.ipynb` and execute the cells to scrape the article, build the vector store, and query the model:
```python
from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
response = model.invoke("What is this article about?")
print(response.content)
```

## Reference
Source article: [Lil’Log – "LLMs as Agents" by Lilian Weng](https://lilianweng.github.io/posts/2023-06-23-agent/)

## Future Work
- Support multiple articles and document types
- Integrate a user interface for interactive queries
- Deploy as a web service

## Contributing
Contributions are welcome. Please open an issue or submit a pull request.

## License
This project is released under the MIT License.
