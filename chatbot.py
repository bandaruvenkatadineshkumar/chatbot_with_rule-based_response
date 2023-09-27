def respond_to_user_input(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I assist you today?"
    elif "help" in user_input.lower():
        return "I can provide information, answer questions, or generate simple charts. What do you need?"
    elif "generate chart" in user_input.lower():
        return "Sure! What type of chart would you like? (e.g., bar chart, pie chart)"
    elif "bar chart" in user_input.lower():
        return generate_bar_chart()  # You would define the generate_bar_chart function separately
    elif "pie chart" in user_input.lower():
        return generate_pie_chart()  # You would define the generate_pie_chart function separately
    else:
        return "I'm not sure how to respond to that. Type 'help' for assistance."

def generate_bar_chart():
    # Add code to generate a bar chart here
    return "Here is your bar chart: [Sample Bar Chart]"

def generate_pie_chart():
    # Add code to generate a pie chart here
    return "Here is your pie chart: [Sample Pie Chart]"

# Main loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = respond_to_user_input(user_input)
    print("Bot:", response)