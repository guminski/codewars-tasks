from unittest import TestCase
"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with out own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""

def generate_hashtag(string):
    return '#' + ''.join(str(word).capitalize() for word in string.split(' ')) if 0 < len(string) < 140 else False


TestCase().assertEqual(generate_hashtag(''), False, 'Expected an empty string to return False')
TestCase().assertEqual(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
TestCase().assertEqual(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
TestCase().assertEqual(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
TestCase().assertEqual(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
TestCase().assertEqual(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
TestCase().assertEqual(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
TestCase().assertEqual(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
TestCase().assertEqual(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
TestCase().assertEqual(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')