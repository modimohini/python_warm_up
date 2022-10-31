#from multiprocessing.sharedctypes import Value


person = {
    "first_name": "Jerry", 
    "last_name" : "Smith",
    "age" : 30,
    "city" : "utha"
}

print(person["first_name"])
print(f'key: {person}')


person['hair_color'] = 'black', 'red'
print(person)

# using get() to access value 
person_info = person.get('age','no age found')
print(person_info)

person_info = person.get('state','no state found')
print(person_info)

# looping through dictionary all key and values 
for key, value in person.items():
    print(f'Key: {key}')
    print(f'Value: {value}\n')

skills = {
    "ade":"Hebrew",
    "kim":"korean",
    "Ajay":"Hindi",
    "jerry":"English",
    "rilly":"English"
}

for name, language in skills.items():
    print(f"{name.title()} speak's fluent {language.capitalize()}")

# looping through all keys 
print("\nlooping through all keys ")
for name in skills.keys():
    print(f' person names {name.title()}')

# looping through all keys is default behaviour, using key() method makes it more readable 
for name in skills:
    print(f'{name.title()}')

# dictionary with condition
friends = ['jade', 'kim']
new_folks = ['lilly', 'gloria']
for name in skills.keys():
    print(f'hey! {name.title()}')
    if name in friends:
        language = skills[name].title()
        print(f'hey, {name.title()} you love to speak {language.title()}')
print("\n")        

if "Jim" not in skills.keys():
    print(f"Jim, what is your fav language?\n")

#ordering keys in dictionary
for name in sorted(skills.keys()):
    print(f"{name.title()}, you are awesome!")

# looping through all values
print("\n--looping through all values \n ")
for language in sorted(skills.values()):
    print(f"{language.title()}, is a cool language!")

print("\n--using set to remove duplicate values\n ")
for language in set(skills.values()):
    print(f"{language.title()}, is a cool language!")

