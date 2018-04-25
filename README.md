# Viz-Similar
Cis 192 Final Project

Calculates and visualizes various similarity metrics between two pieces of text, such as hamming distance, Euclidian distance, Manhattan distance, and "meaning" distance (calculated using non-stopword vector embeddings).

## Project Requirements
The custom class, SenLen, is found in distances.py and represents the length of sentence inputs. Magic methods for operators are used to perform computations. There is also a method that returns the maximum sentence length of two arguments.

We use the modules math, flask, numpy, and scipy. 

We use a decorator for the `/` route and its methods GET and POST.

## Routes and Usage
Calculate similarity with GET parameters at `/`

Type two sentences into in input areas and click 'Go!' to visualize the similarity between them.

## Group Members
Made by Valencia and Arun