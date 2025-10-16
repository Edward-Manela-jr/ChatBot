import random

# Simple Predefined Chatbot with Personality
# Created by [Your Name]

greetings = [
    "Hello there! I'm Mark — your friendly chatbot.",
    "Hey! Mark here, ready to chat!",
    "Hi! I'm Mark. Let's talk about something interesting!"
]

print(random.choice(greetings))
print("You can ask me a few predefined questions.")
print("Try asking things like:\n- What is your name?\n- How are you?\n- What can you do?\n")
print("Type 'bye' or 'exit' to end the chat.\n")

# Different moods or random responses for "how are you"
moods = [
    "I’m just a program, but feeling energized today!",
    "I'm great — ready to help you learn new things!",
    "Doing fine, just running a few code loops in my head!",
    "Feeling curious! What about you?",
    "Superb! Every day is a great day to chat."
]

# Predefined responses
responses = {
"what is your name": "My name is Max! Nice to meet you.",
    "what can you do": "I can answer a few simple questions for now. Try asking me something!",
    "what is latitude": "These are imaginary lines that cross horizontally on the earth.",
    "what is democracy": "It’s a government of the people, by the people, and for the people.",
    "what is a monarchy": "This is a country ruled by a king or queen.",
    "what is a continent": "This is a large piece of land on the earth’s surface.",
    "what is an island": "This is a body of land surrounded by water.",
    "what is a peninsula": "This is a piece of land that connects to an ocean or sea.",
    "what is a plateau": "This is a land area that is higher than the land around it.",
    "what is a valley": "This is a depression between two ridges.",
    "what is the longest mountain": "The Andes Mountains are the longest mountain range in the world."
}

while True:
    user_input = input("You: ").strip().lower().replace("?", "")

    # Exit condition
    if user_input in ["bye", "exit", "quit"]:
        print("Mark: Goodbye! It was nice chatting with you.")
        break

    # Special case for “how are you”
    if user_input == "how are you":
        print(f"Mark: {random.choice(moods)}")
        continue

    # Normal responses
    response = responses.get(user_input, "Sorry, I don’t understand that. Try asking another question!")
    print(f"Mark: {response}")    # Normal responses
    response = responses.get(user_input, "Sorry, I don’t understand that. Try asking another question!")
    print(f"Mark: {response}")
