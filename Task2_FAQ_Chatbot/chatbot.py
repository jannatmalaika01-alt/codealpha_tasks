
import json
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    tokens = nltk.wordpunct_tokenize(text)
    return ' '.join(tokens)

def load_faqs():
    with open("faq_data.json", "r", encoding="utf-8") as file:
        return json.load(file)

faqs = load_faqs()

questions = [faq["question"] for faq in faqs]
processed_questions = [preprocess_text(q) for q in questions]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)

def get_response(user_question):
    processed_input = preprocess_text(user_question)

    user_vector = vectorizer.transform([processed_input])

    similarities = cosine_similarity(user_vector, faq_vectors)

    best_match_index = similarities.argmax()
    best_score = similarities[0][best_match_index]

    if best_score < 0.15:
        return "Sorry, I couldn't understand your question. Please contact our customer support team."

    return faqs[best_match_index]["answer"]

