# 1
numbers = [5, 10, 21, 70]
triples = []
for num in numbers:
    triples.append(num * 3)
print(triples)


numbers = [5, 10, 21, 70]
triples = [ _*3 for _ in numbers]
print(triples)

# 2
celcius = [15.0, 88.75, 120.0, 37.0]
fahrenheit = []
for C in celcius:
    fahrenheit.append(9 / 5 * C + 32)
print(fahrenheit)


celcius = [15.0, 88.75, 120.0, 37.0]
fahrenheit = [ 9 / 5 * C + 32 for C in celcius]
print(fahrenheit)

#3
numbers = [5, 10, 21, 70]
triples = []
for num in numbers:
    if num % 2 == 0:
        triples.append(num * 3)
print(triples)


numbers = [5, 10, 21, 70]
triples = [ num*3 for num in numbers if num % 2 == 0]
print(triples)

# 4
text = input()
isVowels = []
for ch in text:
    if ch.lower() in "aeiou":
        isVowels.append(1)
print(sum(isVowels))


text = input()
print(sum(1 for ch in text if ch.lower() in "aeiou"))