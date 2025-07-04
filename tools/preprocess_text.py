import re
import unicodedata

def preprocess_text(text):
    # Normalize unicode
    text = unicodedata.normalize("NFKC", text)

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)

    # Remove emojis and non-standard characters (except basic punctuation)
    text = re.sub(r'[^\w\s,.!?\'\"]', '', text)

    # Remove extra spaces
    return re.sub(r'\s+', ' ', text).strip()