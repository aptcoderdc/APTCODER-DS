# Simple Chatbot

## Overview
This project implements a simple chatbot using NLTK (Natural Language Toolkit) in Python. The chatbot responds to user input based on the part-of-speech tags of the words in the input.

## Concepts Covered
- Tokenization
- Part-of-speech tagging
- Chatbot response generation

## Required Libraries
- nltk

## Setup
1. Install Python if you haven't already. You can download it from [python.org](https://www.python.org/downloads/).
2. Install NLTK by running `pip install nltk`.
3. Open a Python environment and run the following commands:
    ```python
    import nltk
    nltk.download('averaged_perceptron_tagger')
    ```

## How to Run
1. Clone or download the project repository to your local machine.
2. Navigate to the project directory in your terminal or command prompt.
3. Run the `simple_chatbot.py` file using Python:
    ```
    python simple_chatbot.py
    ```
4. Start chatting with the chatbot! Type your message and press Enter. To exit the chat, type "exit" and press Enter.

## Example

You: Hello
Chatbot: Hey! How can I help you?

You: What is your name?
Chatbot: Goodbye!

You: Thanks
Chatbot: Happy to help!

You: exit
Chatbot: Goodbye!


## Acknowledgements
- NLTK (Natural Language Toolkit) library for NLP tasks.