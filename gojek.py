import pandas as pd
import re
import string
from textblob import TextBlob

df = pd.read_csv(r"D:\TA\[5] Data\labeling\gojek_tweets.csv", encoding='latin1')
df["text"] = df["text"].astype(str)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)  # hapus URL
    text = re.sub(r"@\w+", "", text)     # hapus mention
    text = re.sub(r"#\w+", "", text)     # hapus hashtag
    text = re.sub(r"\s+", " ", text)     # hapus spasi berlebih
    text = text.translate(str.maketrans("", "", string.punctuation))  # hapus tanda baca
    return text.strip()

df["text"] = df["text"].apply(clean_text)

positive_id = [
    "bagus", "suka", "mantap", "hebat", "puas", "baik", "keren", "top", "senang",
    "ramah", "cepat", "terbaik", "menyenangkan", "luar biasa"
]

negative_id = [
    "jelek", "buruk", "benci", "kecewa", "parah", "lelet", "lambat", "tidak puas", "jelek banget",
    "mengecewakan", "kasar", "error", "gagal", "menyebalkan", "telat"
]

def hybrid_sentiment(text):
    pos_score = sum(len(re.findall(rf"\b{re.escape(word)}\b", text)) for word in positive_id)
    neg_score = sum(len(re.findall(rf"\b{re.escape(word)}\b", text)) for word in negative_id)

    blob = TextBlob(text)
    eng_score = blob.sentiment.polarity

    final_score = eng_score + (pos_score * 0.5) - (neg_score * 0.5)

    if final_score > 0.1:
        return "positif"
    elif final_score < -0.1:
        return "negatif"
    else:
        return "netral"

irrelevant_keywords = ["promo", "diskon", "link", "gratis", "beli sekarang", "voucher", "iklan", "follow", "giveaway"]
df["is_irrelevant"] = df["text"].apply(lambda x: any(word in x for word in irrelevant_keywords))
df_filtered = df[~df["is_irrelevant"]].copy()

df_filtered["sentiment"] = df_filtered["text"].apply(hybrid_sentiment)

output_path = r"D:\TA\[5] Data\labeling\tweets_clean_labeled.csv"
df_filtered[["text", "sentiment"]].to_csv(output_path, index=False)
print(f"✅ Selesai! Data bersih & berlabel disimpan di:\n{output_path}")
