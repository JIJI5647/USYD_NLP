"""
Word Analogy Task
In this question, you will implement the word analogy evaluation task.

You will be provided with vectors for all words in the vocabulary and the IDs of the words for the equation:

word1 - word2 + word3 = query

You should use the vectors to do that calculation, then find the word with a vector closest to the query vector, according to cosine distance (excluding the three input words as possible answers). Return the similarity of that word with query vector and the word's ID.

Example
Inputs:

vector_dictionary = [[1, 1, 1], [0, 0, 1], [0, 1, 0], [1, 2, 0], [0, 1, 1]]
word1 = 0
word2 = 1
word3 = 2
Output:

(0.9999999999999998, 3)

"""

# This is the function you need to implement
def word_analogy(vector_dictionary: list[list[float]], word1: int, word2: int, word3: int) -> tuple[float, int]:
    """Predict a word given its context.

    Args:
        vector_dictionary (list[list[float]]): the vectors for each word in the vocabulary
        word1 (int): the first word in the equation
        word2 (int): the second word in the equation
        word3 (int): the third word in the equation

    Returns:
         tuple[float, int]: A tuple containing the similarity of the closest answer and the token ID of that answer
    """
    # TODO
    return 0.0, 0

if __name__ == "__main__":
    main()
