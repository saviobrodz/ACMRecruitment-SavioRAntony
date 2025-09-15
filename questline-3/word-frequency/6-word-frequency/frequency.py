paragraph = input("Enter a paragraph:\n")
paragraph = paragraph.lower()
words = paragraph.split()
cleaned_words = []
for word in words:
    word = word.strip(".,!?;:\"'()[]{}")
    cleaned_words.append(word)

freq = {}
for word in cleaned_words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print("\nWord -- Count")
for word, count in sorted_freq:
    print(f"{word} -- {count}")
