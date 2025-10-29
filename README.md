# 🧠 RAG Application - About Me

A **Retrieval-Augmented Generation (RAG)** application built using **Streamlit** that combines retrieval-based and generative AI to answer questions based on your personal or professional data.  
This project demonstrates how to use **FAISS**, **OpenAI Embeddings**, and **LangChain** to build a smart question-answering system.

---

## 🚀 Demo
🔗 **Live Demo:** [Streamlit App](https://sagarsharmaragpplication.streamlit.app/)  


---

## 📂 Project Structure

```
RAG_application_AboutMe/
│
├── app.py                     # Main Streamlit application
├── requirements.txt           # Project dependencies
├── .gitignore                 # Ignored files for Git
│
├── data/                      # Folder containing uploaded documents or knowledge base
│
├── faiss_store/               # Directory for FAISS vector index storage
│
└── utils/                     # Utility scripts for modular logic
    ├── __init__.py
    ├── embedding.py           # Functions for creating embeddings
    ├── retrieval.py           # Functions for document retrieval
    ├── chunking.py            # Functions for splitting text into chunks
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/sagarsharma459/RAG_application_AboutMe.git
cd RAG_application_AboutMe
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv Rag_venv
Rag_venv\Scripts\activate      # For Windows
# source Rag_venv/bin/activate  # For Linux/Mac
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables
Create a **.env** file in the project root directory and add your OpenAI API key:
```
API_KEY=your_api_key_here
```

### 5️⃣ Run Streamlit App
```bash
streamlit run app.py
```

Then open the local URL (usually http://localhost:8501) in your browser.

---

## 🧩 Key Features

✅ **Document Upload & Processing** – Upload text, PDF, or doc files for knowledge ingestion.  
✅ **Semantic Search with FAISS** – Efficient similarity-based retrieval.  
✅ **Embedding using OpenAI Models** – High-quality text vectorization.  
✅ **RAG Pipeline** – Combines retrieval and generation for context-aware answers.  
✅ **Streamlit UI** – Intuitive and user-friendly web interface.

---

## 🧠 How It Works

1. The app loads and indexes your documents using **FAISS**.  
2. Queries are converted into embeddings using **OpenAI API**.  
3. The most relevant chunks are retrieved and passed to the **LLM** for response generation.  
4. The answer is displayed in a clean Streamlit interface.

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Streamlit**
- **OpenAI API**
- **LangChain**
- **FAISS**
- **NumPy / Pandas**

---

## 🤖 Example Usage

1. Upload your CV, portfolio, or “About Me” document.  
2. Ask questions like:  
   - “What is Sagar Sharma’s professional background?”  
   - “What technologies has Sagar worked with?”  
   - “Summarize his experience in AI and ML.”  
3. Get precise and human-like answers instantly.

---

## 🧱 Future Enhancements

- Add **multi-document support**
- Integrate **local embeddings (e.g., HuggingFace)** for offline use
- Add **chat history** and **memory retention**
- Deploy using **Docker** or **Streamlit Cloud**

---

## 💬 Contributing

Contributions are welcome!  
If you’d like to improve the app or fix bugs, fork the repo and submit a pull request.

---

## 🧑‍💻 Author

**Sagar Sharma**  
🔗 [GitHub Profile](https://github.com/sagarsharma459)  
📧 [Contact Me](mailto:your_email@example.com)

---

## 🪪 License

This project is licensed under the **MIT License** — feel free to use and modify it.

---

⭐ **If you like this project, don’t forget to star the repo!**
