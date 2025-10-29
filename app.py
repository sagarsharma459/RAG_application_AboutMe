import os, sys
sys.path.append(os.path.dirname(__file__))

import streamlit as st
from utils.embedding import get_embedding
from utils.chunking import chunk_text
from utils.retrieval import load_faiss_index, retrieve_chunks
from utils.prompt import build_prompt
from utils.completion import generate_completion

st.title("RAG App – Sagar Sharma Story")
st.write("Ask questions about Sagar Sharma.")

query = st.text_input("Enter your question here")

if query:
    index, chunk_mapping = load_faiss_index()
    top_chunks = retrieve_chunks(query, index, chunk_mapping)
    prompt = build_prompt(top_chunks, query)
    response = generate_completion(prompt)
    
    st.subheader("Answer")
    st.write(response)

    with st.expander("Retrieved Chunks"):
        for chunk in top_chunks:
            st.markdown(f"- {chunk}")
