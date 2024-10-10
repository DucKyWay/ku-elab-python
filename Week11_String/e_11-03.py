# Slicing

subject = 'Fundamental Programming Concept'
text = subject[12:23]
print(text)
print(subject)

subject = 'Fundamental Programming Concept'
text = subject[-19:-8]
print(text)
print(subject)

# Slicing with step

subject = "Fundamental Programming Concept"
print(1, subject[12:23])
print(2, subject[12:23:1])
print(3, subject[12:23:2])

subject = "Fundamental Programming Concept"
print(1, subject[-19:-8])
print(2, subject[-19:-8:1])
print(3, subject[-19:-8:2])

# Slicing with Negative Step

subject = "Fundamental Programming Concept"
print(1, subject[12:23])
print(2, subject[12:23:-1])
print(3, subject[12:23:-2])

subject = "Fundamental Programming Concept"
print(1, subject[22:11])
print(2, subject[22:11:-1])
print(3, subject[22:11:-2])

# start, stop, step can be omitted

subject = "Fundamental Programming Concept"
print(1, subject[:23:])
print(2, subject[:23:2])
print(3, subject[22::-1])