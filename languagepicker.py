# Selects a language for a day for advent of code.
import random

languages = ["Python", "JavaScript", "C", "Java"]

weights = [0.4, 0.4, 0.05, 0.15]

selected_language = random.choices(languages, weights)[0]
print(selected_language)
