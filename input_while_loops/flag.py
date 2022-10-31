from email import message
from operator import truediv


active = True
prompt = "Enter your message"
prompt += "\ntype 'quit' to exit: "

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
