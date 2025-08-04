import random

# Predefined responses
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but I'm doing well!",
    "bye": "Goodbye! Have a great day.",
    "help": "Sure! Ask me anything or say 'bye' to exit."
}

def chatbot():
    print("AI Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("AI Chatbot: Goodbye!")
            break
        elif user_input in responses:
            print("AI Chatbot:", responses[user_input])
        else:
            print("AI Chatbot: I'm not sure how to respond to that.")

if __name__ == "__main__":
    chatbot()