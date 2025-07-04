import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
from preprocess_text import preprocess_text

df = pd.read_csv("../reddit_memes_dataset/data.csv")

def combine_text(row: pd.Series) -> list:
    return preprocess_text(f"{str(row['Title'])}. {str(row['Extracted Text'])}")

df["full_text"] = df.apply(combine_text, axis=1)

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

embeddings = model.encode(df["full_text"].tolist(), convert_to_numpy=True, show_progress_bar=True)

np.save("../embeddings/embedding.npy", embeddings)
