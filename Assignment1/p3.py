"""
Word2vec algorithm
In this question you will implement the continuous bag of words / word2vec algorithm presented in the lecture.

Your code should:

Look up the vectors for the tokens provided

Average the vectors

Compute the dot product with the provided matrix

Normalise the distribution with softmax as shown in the lecture

Return the highest probability token, the probability of that token, and the complete distribution

Note, both the matrix and the vector dictionary we provide have dimensionality VxN, where V is the size of vocabulary and N is the dimensionality of the word vectors. The slide in the lecture showed a matrix with N rows and V columns, which is how it needs to be for linear algebra to work. We have provided it to you transposed because it makes the code simpler.

Example
Inputs:

vector_dictionary = [[1, 1], [0, 0.2], [1.1, 1.2]]
matrix = [[1.2, 1.2], [1, 0.9], [1.1, 1.01]]
words = [0, 1] # These are the context words that you need to use to guess the missing word
Output:

(0, 0.3839470563421029, [0.3839470563421029, 0.2901809427631469, 0.3258720008947502])
"""

def predict_word_and_dist(vector_dictionary: list[list[float]], matrix: list[list[float]], words: list[int]) -> tuple[int, float, list[float]]:
    """Predict a word given its context.

    Args:
        vector_dictionary (list[list[float]]): the vectors for each word in the vocabulary
        matrix (list[list[float]]): the weight matrix, arranged so that there are |vocab| vectors, all the same length
        words (list[int]): the token IDs for the words/tokens in the document

    Returns:
        tuple[int, float, list[float]]: A tuple containing the ID of the highest probability word, the probability of that word, and the distribution of probabilities
    """
    # TODO
    return 0, 0.0, []


if __name__ == "__main__":
    main()
