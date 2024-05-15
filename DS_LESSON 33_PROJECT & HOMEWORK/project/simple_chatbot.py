import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import random

nltk.download('averaged_perceptron_tagger')

# Define responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "farewell": ["Goodbye!", "See you later!", "Have a great day!"],
    "thanks": ["You're welcome!", "No problem!", "Happy to help!"]
}

# Define function for tokenization and part-of-speech tagging
def preprocess(text):
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    return pos_tags

# Define function to generate chatbot response
def generate_response(pos_tags):
    for word, tag in pos_tags:
        if tag == 'VB':
            return random.choice(responses["thanks"])
        elif tag == 'NN':
            return random.choice(responses["farewell"])
        elif tag == 'JJ':
            return random.choice(responses["greeting"])
    return random.choice(responses["greeting"])

# Main loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    else:
        processed_input = preprocess(user_input)
        response = generate_response(processed_input)
        print("Chatbot:", response)
