
from chatbot import get_response

print("===== CUSTOMER SUPPORT CHATBOT =====")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = get_response(user_input)
    print("Chatbot:", response)
