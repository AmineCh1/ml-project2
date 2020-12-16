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

## Results of experiments

```shell
# What I've tried to far
#
# Main Goal: I cannot explain why we use most of the things...I want to make the model easier to understand but KEEP the accuracy.
#
# All tests done on small dataset (100k pos / 100k neg)

# RNN with custom embedding (max_tokens=10'000, embedding_dim = 200, sequence_length = 60) - GRU(200), LSTM(200) -> max at 3rd epoch: 0.8125
# RNN with custom embedding (max_tokens=10'000, embedding_dim = 100, sequence_length = 60) - GRU(100), LSTM(100) -> max at 3rd epoch: 0.8089
# RNN with custom embedding (max_tokens=10'000, embedding_dim = 100, sequence_length = 280) - GRU(100), LSTM(100) -> max at 4th epoch: 0.8112
# RNN with custom embedding (max_tokens=10'000, embedding_dim = 100, sequence_length = 280) - LSTM(100) -> max at 7th epoch: 0.8114
# RNN with custom embedding (max_tokens=10'000, embedding_dim = 100, sequence_length = 280) - LSTM(400) -> max at 3rd epoch: 0.7939
# RNN with custom embedding (max_tokens=10'000, embedding_dim = 100, sequence_length = 280) - LSTM(50) -> max at 10th epoch: 0.8130
# RNN with custom embedding (max_tokens=10'000, embedding_dim = 100, sequence_length = 280) - GRU(50), LSTM(50) -> max at 5th epoch: 0.8146
# RNN with custom embedding (max_tokens=10'000, embedding_dim = 200, sequence_length = 280) - GRU(50), LSTM(50) -> max at 5th epoch: 0.8103
# RNN with custom embedding (max_tokens=10'000, embedding_dim = 200, sequence_length = 280) - GRU(200), LSTM(200) -> max at 3rd epoch: 0.8159
# RNN with custom embedding (max_tokens=15'000, embedding_dim = 200, sequence_length = 280) - GRU(200), LSTM(200) -> max at Xth epoch: XXX
#
# * Pause to try to generate actual predictions
# * If good, continue experiments
# * When done with experiments, generate a full example, and submit to AIcrowd
# * Once done, write report, and run more tests maybe to have even more numbers with the final config (decide what is fixed, and what is variable)
```
