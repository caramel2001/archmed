import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def generate_wordcloud(text, bg_color="white"):
    # Load the SciSpacy model for entity recognition
    nlp = spacy.load("en_core_sci_md")
    # Initialize an empty dictionary to store the entity frequencies
    entity_freq = {}
    # Loop through each entity in the text and count the frequency
    for ent in nlp(text).ents:
        if ent.text.lower() not in STOP_WORDS:
            if ent.text.lower() not in entity_freq:
                entity_freq[ent.text.lower()] = 1
            else:
                entity_freq[ent.text.lower()] += 1

    # Generate the wordcloud from the entity frequencies
    stopwords = set(STOP_WORDS)
    wordcloud = WordCloud(
        width=800,
        height=800,
        background_color=bg_color,
        max_words=50,
        stopwords=stopwords,
        prefer_horizontal=1,
    ).generate_from_frequencies(entity_freq)
    return wordcloud


def show_wordcloud(wc):
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wc)
    plt.axis("off")
    plt.tight_layout(pad=0)
