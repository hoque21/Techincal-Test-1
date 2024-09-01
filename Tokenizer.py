import re

text = "Hello, I am Rafiul Hoque and i am the student of Innovative Skills."

def tokenize(text):
       
    method = r'\b\w+\b' 
    tokens = re.findall(method,text)
    return tokens
tokens = tokenize(text)
print("Tokens:", tokens)

