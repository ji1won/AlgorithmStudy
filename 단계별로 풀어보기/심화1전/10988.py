word = str(input())
word2 = ''.join(reversed(word))
if word == word2 :
    print(1)
else:
    print(0)