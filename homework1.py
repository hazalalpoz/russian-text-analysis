import re
from collections import Counter
import os

file_path = os.path.join(os.path.dirname(__file__), "metin.txt")

with open(file_path,'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

russian_words = re.findall(r'[а-яА-ЯёЁ]+', text)
num_words = len(russian_words)
average_length = sum(len(word) for word in russian_words) / num_words if num_words > 0 else 0
print("Total word count:", num_words)
top_10_freq_words = Counter(russian_words).most_common(10)
print("\nTop 10 most frequent words:")
for word, freq in top_10_freq_words:
    print(f"{word}: {freq} times")
top_10_longest_words = sorted(russian_words, key=lambda x: len(x), reverse=True)[:10]
print("\nTop 10 longest words:")
for word in top_10_longest_words:
    print(f"{word} ({len(word)} letters)")
letters = re.findall(r'[а-яА-ЯёЁ]', text.lower())
top_10_letters = Counter(letters).most_common(10)
print("\nTop 10 most frequent letters:")
for letter, freq in top_10_letters:
    print(f"{letter}: {freq} times")

print("\nAverage word length:", round(average_length, 2))