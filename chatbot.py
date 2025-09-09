print("Patrick: Hi! I'm your study assistant. Type 'bye' to exit.")

while True:
    # Get user input, remove extra spaces, and convert to lowercase
    user_input = input("You: ").strip().lower()

    # Check if the user wants to exit
    if user_input == "bye":
        print("Patrick: Goodbye! 👋")
        break

    # Respond to keywords
    elif "hello" in user_input:
        print("Patrick: Hello there! How can I help you with AI, Data Science, or Python?")
    elif "ai" in user_input:
        print("Patrick: AI stands for Artificial Intelligence — making machines think and learn like humans.")
    elif "data science" in user_input:
        print("Patrick: Data Science is about analyzing data to find insights and make predictions.")
    elif "python" in user_input:
        print("Patrick: Python is a popular programming language used in AI and Data Science.")
    elif "luxdev" in user_input:
        print("Patrick: LuxDev is a development agency that supports projects in various countries.")  
    else:
        print("Patrick: I don't understand. Try typing hello, AI, Data Science, Python, or LuxDev.")
