import random
import difflib
import re

BOT_NAME = "Mark"  # NEW: single source of truth for bot name used in responses

greetings = [
    "Hello there! I'm Mark — your friendly chatbot.",
    "Hey! Mark here, ready to chat!",
    "Hi! I'm Mark. Let's talk about something interesting!"
]

print(random.choice(greetings))
print("You can ask me a few predefined questions.")
print("Try asking things like:\n- What is your name?\n- How are you?\n- What can you do?\n")
print("Type 'bye' or 'exit' to end the chat.\n")

moods = [
    "I'm just a program, but feeling energized today!",
    "I'm great — ready to help you learn new things!",
    "Doing fine, just running a few code loops in my head!",
    "Feeling curious! What about you?",
    "Superb! Every day is a great day to chat."
]

responses = {
    "what is your name": f"My name is {BOT_NAME}! Nice to meet you.",
    "what can you do": "I can answer a few simple questions for now. Try asking me something!",
    "what is latitude": "These are imaginary lines that run east-west across the Earth.",
    "what is democracy": "It's a government of the people, by the people, and for the people.",
    "what is a monarchy": "A country ruled by a king or queen.",
    "what is a continent": "A large piece of land on the Earth's surface.",
    "what is an island": "A body of land surrounded by water.",
    "what is a peninsula": "A piece of land that connects to an ocean or sea on most sides.",
    "what is a plateau": "A land area that is higher than the surrounding land.",
    "what is a valley": "A low area between hills or mountains.",
    "what is the longest mountain": "The Andes Mountains are the longest mountain range in the world."
}

EXIT_KEYWORDS = {"bye", "exit", "quit"}  # NEW: set of exit keywords to gracefully end the chat

def normalize(text: str) -> str:
    """
    NEW: normalize user input for matching.
    - lowercase
    - strip punctuation (keeps alphanumerics and spaces)
    - collapse multiple spaces
    """
    text = text.lower()
    # remove punctuation except keep spaces and alphanumerics
    text = re.sub(r"[^a-z0-9\s]", "", text)
    # collapse whitespace
    return re.sub(r"\s+", " ", text).strip()

try:
    while True:
        user_input = input("You: ")
        # NEW: ignore empty raw input (helps when user just hits Enter)
        if not user_input:
            continue

        norm = normalize(user_input)

        # NEW: if normalization removed everything (e.g., only punctuation), skip
        if not norm:
            continue

        # NEW: check for exit keywords after normalization
        if norm in EXIT_KEYWORDS:
            print(f"{BOT_NAME}: Goodbye! It was nice chatting with you.")
            break

        # handle a special-case question
        if norm == "how are you":
            print(f"{BOT_NAME}: {random.choice(moods)}")
            continue

        # direct match against the canned responses
        response = responses.get(norm)

        # NEW: fuzzy matching - try to find a close key if no direct match
        if response is None:
            match = difflib.get_close_matches(norm, responses.keys(), n=1, cutoff=0.6)
            if match:
                # NEW: if fuzzy match found, return the matched canned response
                response = responses[match[0]]

        if response is None:
            response = "Sorry, I don't understand that. Try asking another question!"

        print(f"{BOT_NAME}: {response}")
except KeyboardInterrupt:
    # NEW: handle Ctrl+C gracefully instead of showing a stack trace
    print(f"\n{BOT_NAME}: Goodbye! (interrupted)")
