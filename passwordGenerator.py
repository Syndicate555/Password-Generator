import random
lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "[]{}()*;/_-&%$#@!<>?"
mix = lowerCase + upperCase + numbers + symbols
length = 16
password = "".join(random.sample(mix,length))
print(password)
