prompt = "hello, give some msg "
prompt += "\nenter 'quit' to end message: "
message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)



