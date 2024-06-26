def single_root_words(root_word, *other_word):
    same_words = []
    for i in other_word:
        if root_word.lower() in i.lower():
            same_words.append(i)
    return same_words

result1 = single_root_words('снег', 'снеговик', 'снежный', 'снегурочка')
result2 = single_root_words('бег', 'бежать', 'Беглый', 'беглец')

print(result1)
print(result2)




