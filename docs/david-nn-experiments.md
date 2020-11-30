# David's experiments

base branch: `david` (the notebook is working locally)

## Reducing overfitting

branch: `david-combat_overfitting`

### Why?

In our base case, we see that the accuracy is going from `73% -> 82% -> 85% -> 89%`, while the validation accuracy decreases a little bit.

This is a textbook case of overfitting.

### What did I try in this branch?

#### Things I kept

1. Going from 128 neurons to 64 for all layers: did not change anything (which tells me that we can keep it at 64)
2. Cleanup: I removed the other `conv1D` layer, as there were two identical ones: no visible impact on performance, and it makes the model simpler.
3. Vanilla layer - went from 64 nodes to 8 nodes, using `softmax` -> same accuracies as with 64 nodes
4. Removed the `dropout` right after the vanilla layer: didn't change validation accuracy (when enabled, it made the val_accuracy worst at first, but made it to the same level after the 4th epoch)
5. Conv1D from 64 to 16 -> 


#### Things I didn't keep

1. Bumped the dropout value to `0.7`: Accuracy went down a bit (`70% - `), but the validation accuracy remained the same (around `79%`). Still overfits. -> Kept it at `50%`
2. Conv1D from 64 to 8 -> 10sec faster per epoch, slower to converge, but we also arrive at around 79% at the end of the 4th epoch

## Theory Q&A

### What are Recurrent Neural Networks (RNN)?

Networks that are used for "things" that happen recurrently, so one thing after the other (e.g. time series, but also words).

### What are Long Short-Term Memory networks (LSTM)?

Specific type of Recurrent Neural Network (RNN) that are capable of learning the relationships between elements in an input sequence.

In our case, the elements are words.

## Sources

https://www.liip.ch/en/blog/sentiment-detection-with-keras-word-embeddings-and-lstm-deep-learning-networks (made in Switzerland :D -> 90% accuracy on IMDB database)
https://colah.github.io/posts/2015-08-Understanding-LSTMs/ (quoted in the article above)

## Open questions

### Padding of inputs

Should we pad our inputs, so that they all have the same length all the time? (the maximum is 280 characters, but some tweets will be shorter than this...)

```python
# Truncate and pad the review sequences 
from keras.preprocessing import sequence 
max_review_length = 500 
X_train = sequence.pad_sequences(X_train, maxlen=max_review_length) 
X_test = sequence.pad_sequences(X_test, maxlen=max_review_length) 
```

## Things I want to try out

* LSTM
* In the article, they do a funny preprocessing: "It downloads the first 5000 top words for each review" -> We could do that for tweets as well maybe, but we might just not need it afterall...
* Stanford standard embedding table
