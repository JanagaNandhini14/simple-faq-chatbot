# Simple FAQ Chatbot
faq = {
    "hi": "Hello! How can I help you?",
    "how are you": "I'm an AI, I don't have feelings, but thanks for asking!",
    "your name": "I'm a simple chatbot.",
    "bye": "Goodbye! Have a nice day!"
}

while True:
    user_input = input("You: ").lower()
    if user_input in faq:
        print("Bot:", faq[user_input])
    else:
        print("Bot: Sorry, I don't know that.")
    if user_input == "bye":
        break
