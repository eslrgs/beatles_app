from gensim.models import Word2Vec

# Sample dataset of sentences
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "The dog slept in the sunlight",
    "The red fox chased the rabbit under the fence",
    "Dogs and foxes belong to the same family",
]

# Preprocess the data: Tokenize the sentences into words
tokenized_sentences = [sentence.lower().split() for sentence in sentences]

# Initialize and train the Word2Vec model
model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)

# Get the vector for a word (example: 'fox')
word_vector = model.wv['fox']
print("Vector representation for 'fox':")
print(word_vector)

# Find words similar to 'fox'
similar_words = model.wv.most_similar('fox', topn=5)
print("\nWords similar to 'fox':")
print(similar_words)
