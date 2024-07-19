def get_response(user_input):
    responses = {
        "hi": "Hello! How can I assist you?",
        "hello": "Hello! How can I assist you?",
        "hey": "Hello! How can I assist you?",
        "how are you": "I'm just a bunch of code, but I'm functioning as expected!",
        "what's your name": "I'm just a simple chatbot created for demonstration purposes.",
        "what is your name": "I'm just a simple chatbot created for demonstration purposes.",
        "weather": "I can't check the weather, but I hope it's nice where you are!",
        "bye": "Goodbye! Have a great day!",
        "what can you do": "I can chat with you and answer some basic questions. Try asking me something!",
        "how old are you": "I don't have an age, but I was created recently!",
        "favorite color": "I don't have a favorite color, but I think all colors are beautiful!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "what's the time": "I'm not able to check the time, but it might be time for a break!",
        "help": "Sure, I can help! Ask me about the weather, my name, or just say hi!",
    }

    # Check for exact matches
    if user_input in responses:
        return responses[user_input]

    # Check if user input contains any of the keys as a substring
    for key in responses:
        if key in user_input:
            return responses[key]

    # Default response if no match is found
    return "I'm sorry, I don't understand that. Can you ask something else?"


def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")

    while True:
        user_input = input("You: ").lower()
        response = get_response(user_input)
        print(f"Chatbot: {response}")

        if user_input == "bye":
            break


chatbot()