import os

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from collections import Counter

from wordcloud import WordCloud


# ==========================================
# SETTINGS
# ==========================================

DATASET_PATH = "processing/imdb_cleaned.csv"

OUTPUT_FOLDER = "analytics"


os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)


# ==========================================
# LOAD DATASET
# ==========================================

print("Loading dataset...")

df = pd.read_csv(
    DATASET_PATH
)


print(
    "Dataset loaded:",
    df.shape
)


# ==========================================
# CHECK COLUMNS
# ==========================================

print("\nColumns:")

print(
    df.columns.tolist()
)


# ==========================================
# NORMALIZE SENTIMENT
# ==========================================

df["sentiment"] = (
    df["sentiment"]
    .astype(str)
    .str.lower()
    .str.strip()
)


# ==========================================
# REVIEW LENGTH
# ==========================================

df["review_length"] = (
    df["review"]
    .astype(str)
    .apply(len)
)


df["word_count"] = (
    df["review"]
    .astype(str)
    .apply(
        lambda x: len(x.split())
    )
)


# ==========================================
# SENTIMENT COUNTS
# ==========================================

sentiment_counts = (
    df["sentiment"]
    .value_counts()
)


print("\nSentiment distribution:")

print(
    sentiment_counts
)


# ==========================================
# CHART 1
# SENTIMENT DISTRIBUTION
# ==========================================

plt.figure(
    figsize=(8, 6)
)


plt.pie(
    sentiment_counts.values,
    labels=sentiment_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={
        "width": 0.42
    }
)


plt.title(
    "IMDb Review Sentiment Distribution",
    fontsize=16,
    fontweight="bold"
)


plt.tight_layout()


plt.savefig(
    os.path.join(
        OUTPUT_FOLDER,
        "sentiment_distribution.png"
    ),
    dpi=180,
    bbox_inches="tight"
)


plt.close()


print(
    "Saved sentiment_distribution.png"
)


# ==========================================
# CHART 2
# REVIEW LENGTH
# ==========================================

plt.figure(
    figsize=(10, 6)
)


sns.histplot(
    df["review_length"],
    bins=50,
    kde=True
)


plt.title(
    "Review Length Distribution",
    fontsize=16,
    fontweight="bold"
)


plt.xlabel(
    "Review Length (Characters)"
)


plt.ylabel(
    "Number of Reviews"
)


plt.tight_layout()


plt.savefig(
    os.path.join(
        OUTPUT_FOLDER,
        "review_length.png"
    ),
    dpi=180,
    bbox_inches="tight"
)


plt.close()


print(
    "Saved review_length.png"
)


# ==========================================
# CHART 3
# SENTIMENT VS REVIEW LENGTH
# ==========================================

plt.figure(
    figsize=(10, 6)
)


sns.boxplot(
    data=df,
    x="sentiment",
    y="word_count"
)


plt.title(
    "Review Word Count by Sentiment",
    fontsize=16,
    fontweight="bold"
)


plt.xlabel(
    "Sentiment"
)


plt.ylabel(
    "Number of Words"
)


plt.tight_layout()


plt.savefig(
    os.path.join(
        OUTPUT_FOLDER,
        "sentiment_review_length.png"
    ),
    dpi=180,
    bbox_inches="tight"
)


plt.close()


print(
    "Saved sentiment_review_length.png"
)


# ==========================================
# TEXT CLEANING
# ==========================================

stop_words = {

    "the",
    "and",
    "a",
    "to",
    "of",
    "is",
    "in",
    "it",
    "this",
    "that",
    "was",
    "for",
    "with",
    "as",
    "on",
    "but",
    "are",
    "be",
    "have",
    "has",
    "had",
    "i",
    "you",
    "he",
    "she",
    "they",
    "we",
    "my",
    "me",
    "his",
    "her",
    "their",
    "an",
    "or",
    "so",
    "if",
    "from",
    "at",
    "by",
    "movie",
    "film"

}


def get_words(text):

    import re

    text = text.lower()


    text = re.sub(
        r"<.*?>",
        " ",
        text
    )


    text = re.sub(
        r"[^a-z\s]",
        " ",
        text
    )


    words = text.split()


    words = [

        word

        for word in words

        if word not in stop_words

        and len(word) > 2

    ]


    return words


# ==========================================
# POSITIVE WORDS
# ==========================================

print(
    "\nAnalyzing positive words..."
)


positive_text = " ".join(

    df[
        df["sentiment"] == "positive"
    ]["review"]
    .astype(str)

)


positive_words = get_words(
    positive_text
)


positive_counter = Counter(
    positive_words
)


positive_top = (
    positive_counter
    .most_common(15)
)


# ==========================================
# POSITIVE WORD CHART
# ==========================================

words = [
    x[0]
    for x in positive_top
]


counts = [
    x[1]
    for x in positive_top
]


plt.figure(
    figsize=(10, 7)
)


plt.barh(
    words[::-1],
    counts[::-1]
)


plt.title(
    "Top Positive Words",
    fontsize=16,
    fontweight="bold"
)


plt.xlabel(
    "Frequency"
)


plt.tight_layout()


plt.savefig(
    os.path.join(
        OUTPUT_FOLDER,
        "positive_words.png"
    ),
    dpi=180,
    bbox_inches="tight"
)


plt.close()


print(
    "Saved positive_words.png"
)


# ==========================================
# NEGATIVE WORDS
# ==========================================

print(
    "Analyzing negative words..."
)


negative_text = " ".join(

    df[
        df["sentiment"] == "negative"
    ]["review"]
    .astype(str)

)


negative_words = get_words(
    negative_text
)


negative_counter = Counter(
    negative_words
)


negative_top = (
    negative_counter
    .most_common(15)
)


# ==========================================
# NEGATIVE WORD CHART
# ==========================================

words = [
    x[0]
    for x in negative_top
]


counts = [
    x[1]
    for x in negative_top
]


plt.figure(
    figsize=(10, 7)
)


plt.barh(
    words[::-1],
    counts[::-1]
)


plt.title(
    "Top Negative Words",
    fontsize=16,
    fontweight="bold"
)


plt.xlabel(
    "Frequency"
)


plt.tight_layout()


plt.savefig(
    os.path.join(
        OUTPUT_FOLDER,
        "negative_words.png"
    ),
    dpi=180,
    bbox_inches="tight"
)


plt.close()


print(
    "Saved negative_words.png"
)


# ==========================================
# WORD CLOUD
# ==========================================

print(
    "Generating word cloud..."
)


all_words = (

    positive_words

    +

    negative_words

)


wordcloud = WordCloud(

    width=1200,

    height=600,

    background_color="white",

    max_words=150,

    min_font_size=10

).generate(

    " ".join(all_words)

)


plt.figure(
    figsize=(14, 7)
)


plt.imshow(
    wordcloud,
    interpolation="bilinear"
)


plt.axis(
    "off"
)


plt.title(
    "IMDb Review Word Cloud",
    fontsize=18,
    fontweight="bold"
)


plt.tight_layout()


plt.savefig(
    os.path.join(
        OUTPUT_FOLDER,
        "wordcloud.png"
    ),
    dpi=180,
    bbox_inches="tight"
)


plt.close()


print(
    "Saved wordcloud.png"
)


# ==========================================
# FINISHED
# ==========================================

print("\n===================================")

print(
    "ANALYTICS GENERATION COMPLETE"
)

print(
    "Charts saved in:",
    OUTPUT_FOLDER
)

print("===================================")