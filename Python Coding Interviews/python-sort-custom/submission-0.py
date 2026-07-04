from typing import List

def word_length(words: str) -> int:
    return len(words)

def num_length(numbers:int)->int:
    return abs(numbers)


def sort_words(words: List[str]) -> List[str]:
    words.sort(key=word_length, reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=num_length)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
