def chatbot(user_input):

    if "Hello" in user_input:
        return "Hi there! How can I help you?"
    elif "how are you" in user_input:
        return "Being a computer I'm fine ;)"
    elif "bye" in user_input:
        return "Goodbye! Have a great day:)"
    elif "what is your name" in user_input:
        return "I'm a chatbot."
    else:
        return "I'm sorry, can you repeat."


while True:
   
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("bot: Goodbye!")
        break
   
    response = chatbot(user_input)
    
    print("bot:", response)
