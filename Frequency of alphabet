# program that counts the number of times each alphabet is appearing in it, and displays the frequency of the occurrence of each alphabet.

text = open("input.txt", "r")
d = dict() # Create an empty dictionary
# Loop through each line of the file
for line in text:
    line = line.strip() ## Remove leading spaces newline character
    line = line.lower() #characters in line to lowercase
    for alpha in line:
        if alpha in d and alpha.isalpha(): #if the alphabet is already in dictionary
            d[alpha] = d[alpha] + 1 # Increment count of alpha by 1
        elif alpha.isalpha():
            # Add an alphabet to dictionary with count 1
            d[alpha] = 1
for key in list(d.keys()):
    print(key, ":", d[key])
