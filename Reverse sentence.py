# takes a sentence as input from user and reverses the words in the sentence.

sentence = input ("Enter the sentence to be reversed")
words = sentence.split()
rev = " ".join(reversed(words))
print(rev)
