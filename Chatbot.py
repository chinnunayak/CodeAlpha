import nltk
from nltk.chat.util import Chat, reflections


#Define a list of patterns and respons for the chatbot
#You can add more patterns and responses to make the chatbot more conversational
patterns = [
      (r'hi|hello|hey', ['Hello!' , 'Hi there!', 'Hey!']),
      (r'how are you',['I\'m just a computer program, so I don\'t have feelings, but thanks for asking!']),
      (r'What is your name',['I am a chatbot created with NLTK. You can call me Chatboot']),
      (r'who are you',['I am a chatbot created with NLTK.You can call me Chatboot']),
      (r'what can you do', ['I am have basic conversations with you and answer questions.']),
      (r'bye|goodbaye',['Goodbye!', 'See you later!']),
      (r'default', ["I'm not sure I understand. can you rephrase your question?"])
]

#Created a chatbot using the patterns and reflection
chatbot = Chat(patterns, reflections)

#Start the conversion
print("Hello! I am your chatbot. You can start a conversation with me 'quit' to exit.") 
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    if"bye" in user_input.lower():
        print("Chatbot: Goodbye!")
        break
    