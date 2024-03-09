word = input()
wordSet = set()

for i in range(len(word)):
    for j in range(i+1, len(word)+1):
        wordSet.add(word[i:j])
        
print(len(wordSet))
