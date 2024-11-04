import pandas as pd
import requests
from bs4 import BeautifulSoup

df=pd.read_excel('input.xlsx')

def fetch_article(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the article title (adjust the selector to match the website's structure)
    title = soup.find('h1').get_text(strip=True) if soup.find('h1') else 'No Title Found'
    
    # Extract the article text (adjust the selector to match the website's structure)
    paragraphs = soup.find_all('p')
    article_text = '\n'.join([para.get_text(strip=True) for para in paragraphs])
    
    return title, article_text

def save_article(url_id, title, text):
    # Define the file name based on URL_ID
    file_path = f"data/{url_id}.txt"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"{title}\n\n{text}")


for _, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
        
    try:
        title, text = fetch_article(url)
        save_article(url_id, title, text)
        print(f"Successfully saved article {url_id}")
    except Exception as e:
        print(f"Failed to process {url}: {e}")

import os
import nltk

def load_stopwords(folder_path):
    stop_words = set()
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file:
                stop_words.update(word.lower() for word in file.read().splitlines())
    return stop_words



# Function to clean text using stop words
def clean_text(text_path):
    with open(text_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    tokens = nltk.word_tokenize(text)
    
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    cleaned_text = ' '.join(filtered_tokens)
    return cleaned_text


# Load stopwords from the StopWords folder
stop_words = load_stopwords('StopWords')

positive_words=set()
with open('MasterDictionary/positive-words.txt', 'r') as file:
    tokens=nltk.word_tokenize(file.read())
for token in tokens:
    positive_words.add(token)

negative_words=set()
with open('MasterDictionary/negative-words.txt', 'r') as file:
    tokens=nltk.word_tokenize(file.read())
for token in tokens:
    negative_words.add(token)        


def positive_score(text):
    try:
        cleaned_text=clean_text(text)
        tokens = nltk.word_tokenize(cleaned_text)
    
        positive_score = sum(1 for word in tokens if word.lower() in positive_words)
        return positive_score
    except:
        return 0

def negative_score(text):
    try:
        cleaned_text=clean_text(text)
        tokens = nltk.word_tokenize(cleaned_text)
    
        negative_score = sum(1 for word in tokens if word.lower() in negative_words)
        return negative_score
    except:
        return 0

def polarity_score(text):
    try:
        return (positive_score(text)-negative_score(text))/(positive_score(text)+negative_score(text)+0.000001)
    except:
        return 0

def subjectivity_score(text):
    try:
        cleaned_text=clean_text(text)
        tokens=nltk.word_tokenize(cleaned_text)
        Subjectivity_Score = (positive_score(text) + negative_score(text))/ ((len(tokens)) + 0.000001)
        return Subjectivity_Score
    except:
        return 0


def average_sentence_length(text):
    try:
        cleaned_text=clean_text(text)
        tokens=nltk.word_tokenize(cleaned_text)
        nwords=len(tokens)
        nsentences=len(cleaned_text.split("."))
        return nwords/nsentences
    except:
        return 0

def syllable_count(word):
    word = word.lower()
    vowels = "aeiouy"
    count = 0

    if word.endswith("e"):
        word = word[:-1]
        
    if word[0] in vowels:
        count += 1
    
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1

    if word.endswith("es") or word.endswith("ed"):
        count -= 1
    
    if count == 0:
        count = 1
        
    return count

def syllable_per_word(text_path):
    try:
        with open(text_path, 'r', encoding='utf-8') as file:
            text = file.read()
        words=nltk.word_tokenize(text)
        return sum(syllable_count(word) for word in words)/len(words)
    except:
        return 0


def complex_word_percentage(text_path):
    try:
        with open(text_path, 'r', encoding='utf-8') as file:
            text = file.read()
        words = nltk.word_tokenize(text)
        complex_words_count = sum(1 for word in words if syllable_count(word) > 2)
        total_words = len(words)
        percentage = (complex_words_count / total_words) * 100 if total_words > 0 else 0
        return percentage
    except:
        return 0


def fog_index(text):
    try:
        fog_index = 0.4 * (average_sentence_length(text) + complex_word_percentage(text))
        return fog_index
    except:
        return 0


def complex_word_count(text_path):
    try:
        with open(text_path, 'r', encoding='utf-8') as file:
            text = file.read()
        words = nltk.word_tokenize(text)
        return sum(1 for word in words if syllable_count(word) > 2)
    except:
        return 0


def word_count(text):
    try:
        cleaned_text=clean_text(text)
        tokens=nltk.word_tokenize(cleaned_text)
        return len(tokens)
    except:
        return 0

import re

def count_personal_pronouns(text_path):
    try:
        with open(text_path, 'r', encoding='utf-8') as file:
            text = file.read()
        lower_text = text.lower()
        pronoun_pattern = r'\b(i|we|my|ours|us)\b'
        matches = re.findall(pronoun_pattern, lower_text)
        filtered_matches = [match for match in matches if not re.search(r'\bUS\b', text)]
        return len(filtered_matches)
    except:
        return 0

def average_word_length(text):
    try:
        with open(text, 'r', encoding='utf-8') as file:
            text = file.read()
        words = text.split()
        total_characters = sum(len(word) for word in words)
        total_words = len(words)
        if total_words > 0:
            avg_word_length = total_characters / total_words
        else:
            avg_word_length = 0
    
        return avg_word_length
    except:
        return 0

df1=pd.read_excel("Output Data Structure.xlsx")

df1['POSITIVE SCORE'] = df1['URL_ID'].apply(lambda url_id: positive_score(f"data/{url_id}.txt"))
df1['NEGATIVE SCORE'] = df1['URL_ID'].apply(lambda url_id: negative_score(f"data/{url_id}.txt"))
df1['POLARITY SCORE'] = df1['URL_ID'].apply(lambda url_id: polarity_score(f"data/{url_id}.txt"))
df1['SUBJECTIVITY SCORE'] = df1['URL_ID'].apply(lambda url_id: subjectivity_score(f"data/{url_id}.txt"))
df1['AVG SENTENCE LENGTH'] = df1['URL_ID'].apply(lambda url_id: average_sentence_length(f"data/{url_id}.txt"))
df1['PERCENTAGE OF COMPLEX WORDS'] = df1['URL_ID'].apply(lambda url_id: complex_word_percentage(f"data/{url_id}.txt"))
df1['FOG INDEX'] = df1['URL_ID'].apply(lambda url_id: fog_index(f"data/{url_id}.txt"))
df1['AVG NUMBER OF WORDS PER SENTENCE'] = df1['URL_ID'].apply(lambda url_id: average_sentence_length(f"data/{url_id}.txt"))
df1['COMPLEX WORD COUNT'] = df1['URL_ID'].apply(lambda url_id: complex_word_count(f"data/{url_id}.txt"))
df1['WORD COUNT'] = df1['URL_ID'].apply(lambda url_id: word_count(f"data/{url_id}.txt"))
df1['SYLLABLE PER WORD'] = df1['URL_ID'].apply(lambda url_id: syllable_per_word(f"data/{url_id}.txt"))
df1['PERSONAL PRONOUNS'] = df1['URL_ID'].apply(lambda url_id: count_personal_pronouns(f"data/{url_id}.txt"))
df1['AVG WORD LENGTH'] = df1['URL_ID'].apply(lambda url_id: average_word_length(f"data/{url_id}.txt"))


df1.to_excel('output.xlsx', index=False)
df1.head()