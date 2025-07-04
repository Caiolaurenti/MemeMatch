# MemeMatch 🧠😂

**MemeMatch** is a Streamlit-powered web app that recommends the most semantically relevant meme based on user input. It's a playful demonstration of natural language processing, semantic similarity, and image retrieval — all dressed up in meme form for your amusement (or your recruiter’s confusion).

---

## 🚀 Live Demo
[Click here to try it out](https://memematch.streamlit.app)  
_(Please wait a few seconds for the app to wake up if it’s been sleeping.)_

---

## 🧰 Technologies Used

### ⚙️ Backend
- **Python** — The Swiss army knife of devs and data scientists.
- **Pandas** — Data wrangling without the emotional breakdown.
- **NumPy** — Fast math magic for vectors and arrays.
- **scikit-learn** — Cosine similarity to match user input with memes like a brainy dating service.

### 🤖 NLP & Embeddings
- **Sentence Transformers (`paraphrase-MiniLM-L6-v2`)** — Converts text into dense vectors that capture meaning. Because just looking at words is so 1999.
- **Preprocessing** — Text normalization, URL stripping, emoji removal. Basically a digital loofah.

### 🖼️ Images
- **Pillow (PIL)** — Opens and displays memes like a civilized image library.

### 🌐 Web App
- **Streamlit** — Rapid UI framework for Python nerds who want buttons without HTML trauma.
- **Streamlit Community Cloud** — Free hosting because you’re broke or just wisely frugal.

---

---

## 📝 How It Works
1. You enter a sentence.
2. It's preprocessed and embedded into a semantic vector.
3. We compute cosine similarity against all meme captions.
4. The most relevant meme image is displayed — joy ensues.

---

## 📦 Setup Instructions
```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/memematch.git
cd memematch

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py


