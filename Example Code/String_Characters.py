# Introduction to Python Strings and Characters

#Character Strings
message = 'Hello World'
print(message)

# Length of String
print(len(message))

# Indexing of String
print(message[:5])
print(message[6:])

# Convert Upper or Lower Case
print(message.lower())
print(message.upper())

# Count Number of Instances
print(message.count('l'))

# Replace String Function
new_message = message.replace('World', 'Universal Universe')
print(new_message)

# Greetings Message # Formate String
greeting = 'Hello'
name = 'William'

# welcomeMessage = greeting + ', ' + name + '. Welcome! '
welcomeMessage = '{}, {}. Welcome!'.format(greeting,name)
print(welcomeMessage)

# Print Different Attributes & Methods to be used on Message
# print(dir(message))
# print(help(str))
