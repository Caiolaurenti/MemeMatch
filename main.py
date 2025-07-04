import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from tools.preprocess_text import preprocess_text

@st.cache_resource
def load_model():
    return SentenceTransformer("paraphrase-MiniLM-L6-v2")

@st.cache_data
def load_data_and_embeddings():
    df = pd.read_csv("./reddit_memes_dataset/data.csv")
    embedding = np.load("./embeddings/embedding.npy")
    return df, embedding

model = load_model()
df, embedding = load_data_and_embeddings()

st.title("Find the Most Relevant Meme")
user_input = st.text_input("Type something in English:")

if user_input:
    processed_input = preprocess_text(user_input)
    embedded_input = model.encode(processed_input)

    arg_meme = np.argmax(cosine_similarity([embedded_input], embedding))
    meme_file = df.iloc[arg_meme]["File Name"]

    st.image(f"./reddit_memes_dataset/memes/{meme_file}", caption="Here’s your perfect meme. You earned this.")

