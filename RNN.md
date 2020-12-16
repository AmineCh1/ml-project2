# Recurrent Neural Networks

## Hyperparameters

### Vectorize Layer

* max_tokens (fixed it to 10'000 - number of words to consider in our vocabulary)
* output_sequence_length (fixed it to 280, need to try 60)
* ngrams (1,2,3,4,5)

### Embedding layer

* custom (trainable) or preprocessed (from GloVe)
* embedding_dim (64, 100, 200, 300)

### Kinds of layers: Dropout (right after embedding), GRU Layer, LSTM layer, etc

Try to add/remove some, and see the impact on accuracy

### Dropout layer

* percentage (0.2 - 0.5 seems to be good values online)

### GRU Layer

* ???

### LSTM Layer

* Number of nodes (100, 200, 300, 400, ...)
* Other ones???
