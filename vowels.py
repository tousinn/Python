#vowels = ['a','e','i','o','u']
#word="Milliways"
vowels = set("aeiou")
word= input("Please provide a word to search for vowels: ")
found = vowels.intersection(set(word))
print(found)
##found={}
##for letter in word:
##    if letter in vowels:
##        found.setdefault(letter,0)
##        found[letter]+=1
##
##for k,v in sorted(found.items()):
##    print(k, " was found ",v, " times")
##
##
