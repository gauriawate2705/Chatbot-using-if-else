# Simple Rule-Based Chatbot using If-Else

print("Chatbot: Hello! I am a simple rule-based chatbot.")
print("Chatbot: Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    # Exit condition
    if user == "bye":
        print("Chatbot: Goodbye! Have a great day.")
        break

    # Rule-based responses
    elif "hello" in user or "hi" in user:
        print("Chatbot: Hello! How can I help you today?")

    elif "how are you" in user:
        print("Chatbot: I'm just code, but I'm doing great! 😄")

    elif "your name" in user:
        print("Chatbot: I'm a simple chatbot created using Python if-else statements.")

    elif "help" in user:
        print("Chatbot: Sure! Ask me anything, or say 'bye' to exit.")

    elif "time" in user:
        print("Chatbot: I can’t tell time yet, but soon I will!")

    else:
        print("Chatbot: Sorry, I don’t understand that. I am still learning!")
