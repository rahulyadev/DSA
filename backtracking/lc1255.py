"""LC 1255. Maximum Score Words Formed by Letters
(https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/)
"""
from typing import List
from collections import Counter

class Solution:
    """Solution class for Maximum Score Words Formed by Letters."""

    def max_score_words(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """Function to find the maximum score that can be obtained by
        forming words from the given letters.
        """
        def get_word_score(word):
            """Function to find the score of a word."""
            return sum(score[ord(c) - ord('a')] for c in word)

        def can_form_word(word, available_letters):
            """Function to check if a word can be formed from the available letters."""
            word_count = Counter(word)
            for char, count in word_count.items():
                if available_letters[char] < count:
                    return False
            return True

        def backtrack(index, available_letters, current_score):
            """Function to find the maximum score that can be obtained by
            forming words from the given letters.
            """
            nonlocal max_score
            if index == len(words):
                max_score = max(max_score, current_score)
                return

            # Skip the current word
            backtrack(index + 1, available_letters, current_score)

            word = words[index]
            if can_form_word(word, available_letters):
                word_score = get_word_score(word)
                word_count = Counter(word)

                # Use the current word
                for char in word_count:
                    available_letters[char] -= word_count[char]

                backtrack(index + 1, available_letters, current_score + word_score)

                # Revert the changes (backtrack)
                for char in word_count:
                    available_letters[char] += word_count[char]

        max_score = 0
        available_letters = Counter(letters)
        backtrack(0, available_letters, 0)

        return max_score
