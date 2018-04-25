# Phrase Similarity Visualizer
CIS 192 S18 Final Project, by Valencia and Arun

Calculates and visualizes various similarity metrics between two pieces of text: Hamming distance, Euclidian distance, Manhattan distance, and "meaning" distance (calculated using non-stopword vector embeddings).

## Project Requirements
The custom class, `SenLen`, is found in `distances.py` and handles string manipulation logic. Magic methods for operators are used to perform computations. There is also a method that returns the maximum sentence length from two sentences given as arguments.

We use the modules `math`, `flask`, `numpy`, `nltk`, and `gensim` (Python implementation of Word2Vec model). 

We use a decorator for the `/` route and its methods GET and POST.
 
## Routes and Usage
To run the server, install the packages listed above and run `main.py`.

Type two sentences into in input areas and click 'Go!' to visualize the similarity between them. You can hover over
the bar graph visualization to view exact percentages for similarity.

## Project Implementation

The Flask server is instantiated and served in `main.py`. In addition, we developed a `DistanceCalculator` class that
computes distance calculations and sends the similarities to the Flask template rendering.

Traditional string manipulation technique implementations are in `distances.py` which we `import` into `main.py`. These include
Hamming distance, Euclidian distance, and Manhattan distance. To determine similarity, these distances are computed and then
divided by the length of the larger string in order to yield a value between 0 and 1. Finally, we take the compliment of this value to 
represent the similarity. In `distances.py`, we also implemented a class named `SenLen` to handle certain string manipulation logic—namely padding strings in case of differing lengths. We use magic methods to handle comparisons.

The "meaning" distance heuristic is implemented in `nlp.py` and is imported into `main.py`. First, we remove all stopwords from 
the input (e.g. words like "the" and "for" that yield no meaning) using the `nltk` package (English).
We use the word2vec model implemented in the `gensim` package to generate word embeddings (numpy vectors). The model is currently
trained on a corpus of Barack Obama's speeches (Donald Trump's speeches were getting a bit out of hand). Then, we
average the vectors to determine a centralized meaning for the phrase. Finally, we calculate the distance between the two vectors
by normalizing each vector and computing the cosine distance. 