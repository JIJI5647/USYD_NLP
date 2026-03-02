"""
Semantle
In this question, you will implement a command-line version of the game Semantle (https://semantle.com/).

In the game, there is a target word that you need to work out. You can guess words and will be told their cosine similarity with the target word.

Your code should:

Read the word vectors from vectors-for-common-words.txt, storing them in two dictionaries. One that maps from words to vectors and the other that maps from word IDs to words.

Print Please provide a number:

Read a number from the user, W

If W is a valid word ID, continue, otherwise go back to 2.

Print Please guess the word:

Go into a loop where:

The user provides a word

If the word is not in the provided data, tell the user Word not present

If the word is in the provided data, give the cosine similarity of the word to the target word.

If the word matches the target word, say they win

The format of vectors-for-common-words.txt is one line per word, with the a word ID, followed by the word, followed by a series of numbers to define the vector. For example:

2811 sharply 0.62834 0.11174 0.13459 0.06958 -0.46444 0.28391 -0.15170 -1.42786 -0.88062 -0.26507 0.91592 0.88818 0.42208 0.19925 0.29360 0.03673 -0.86947 -0.37088 -0.23092 -0.61915 0.48975 0.15930 0.97192 -0.23112 1.13015 0.33021 0.72386 -0.63382 0.00518 -0.51525 0.36127 -0.17736 -0.89132 -0.01298 1.56973 -0.05750 0.60534 3.23923 -1.10415 -1.00973 0.17423 0.83658 1.07896 0.15548 1.16576 0.11272 -0.58910 0.13570 0.38173 -0.70836
2812 cool -0.39868 -0.07622 -0.07499 0.41020 0.34091 0.03268 -0.18765 0.18384 -0.70171 -1.26253 -1.28388 0.64459 -0.36795 -0.67205 -0.58175 0.30123 -0.55345 -0.66791 0.37790 0.98425 -0.46339 -0.13352 0.07039 -0.39494 0.95329 -0.88572 -0.24220 -0.65505 -0.25921 -0.34013 -0.10558 0.48821 -0.29263 -0.06019 0.24826 0.07303 0.44765 3.33359 -0.80419 0.35622 0.73982 0.86403 0.53742 1.13977 -0.05469 0.02157 0.62167 -0.79953 0.09684 0.75924
2813 manufacturers -0.06524 -0.32576 0.31422 -0.34237 0.39901 -0.14560 0.74069 -0.79222 -0.43274 -0.21133 -1.02904 0.80437 0.19003 1.23884 -0.15667 -0.12580 -0.92106 0.77828 0.26790 -2.07163 -0.10490 -0.67936 -0.13560 -0.14290 -0.00190 -0.38669 -0.31105 -0.65221 0.82651 -1.12805 1.17825 0.25825 0.06635 -0.16209 0.41851 0.40547 -0.75343 3.56735 -0.10465 -0.34192 -0.49016 0.18290 0.84356 -0.13881 0.80807 0.16861 0.19844 0.78638 -0.90743 0.25419
Here, sharply has word ID 2811 and the vector [0.62834, 0.11174, ..., 0.38173, -0.70836]

Example
Here, system output is in bold. Note that word 2681 is 'apple'

Please provide a number:
2681
Please guess the word:
chocolate
0.5943329469366123
mango
Word not present
apple
1.0000000000000002
You win!

"""

def play_semantle():
    """Play an interactive game of Semantle."""
    # TODO
    pass

if __name__ == "__main__":
    main()
