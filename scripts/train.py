import torch

with open("data/input.txt", "r", encoding="utf-8") as f:
  text = f.read()

print("Length of text is: ", len(text))

print(text[:1000])

# Get all unique characters from text
chars = sorted(list(set(text)))
vocab_size = len(chars)
print("".join(chars))
print(vocab_size)

# Tokenize - mapping from string to integers, 
# Note: this maps things naively as it is character level. Industry uses sub-word level encoding
stoi = { ch:i for i, ch in enumerate(chars)}
itos = { i:ch for i, ch in enumerate(chars)}
encode = lambda s: [stoi[c] for c in s] # encoder: take a string output a list of integers
decode = lambda nums: "".join(itos[i] for i in nums) # decoder: take a list of integers, output a string

print(encode("hello world"))
print(decode(encode("hello world")))
