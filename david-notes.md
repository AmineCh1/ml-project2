# Tutorial on word embeddings (*Tensorflow*)

## Cool resources

Tutorial: [https://www.tensorflow.org/tutorials/text/word_embeddings](https://www.tensorflow.org/tutorials/text/word_embeddings)

Glossary for ML terms: [https://developers.google.com/machine-learning/glossary/](https://developers.google.com/machine-learning/glossary/)

Another article that helped me understand the ***Embedding layer*** a bit better: [https://machinelearningmastery.com/use-word-embedding-layers-deep-learning-keras/](https://machinelearningmastery.com/use-word-embedding-layers-deep-learning-keras/)

## Cool tips

[https://www.tensorflow.org/tutorials/keras/text_classification#prepare_the_dataset_for_training](https://www.tensorflow.org/tutorials/keras/text_classification#prepare_the_dataset_for_training)

The end of that part is neat, because you have a demo of going **from a string** to a **list of integers** with the **Vectorize** layer (search for `As you can see above, each token has been replaced by an integer.`).

`vectorize_layer.get_vocabulary()` will give you **the vocabulary of your inputs**! (I think it's what we get by running ***adapt***)

## What is the relationship between Keras and TensorFlow?

Tensorflow: End-to-end open-source ***Machine Learning platform***

Keras: High-level ***Neural Network*** library, built *on top of Tensorflow*

## How can we have performance if we need to go to the disk for *each individual file*?

`train_ds.cache().prefetch(buffer_size=AUTOTUNE)`

## Keras - What is the *embedding layer*?

Lookup table that maps from *integer indices* (these integer indices ***represent words***) to *dense vectors* (a.k.a. *their embeddings*).

## What does `tf.keras.layers.Embedding(1000, 5)` actually do?

It's a ***NN layer*** as well.

Inputs: *integers indices* representing ***words (*the output of the *TextVectorization* layer*)***

Outputs: Embedding Vectors (you get those by training the model: ***they are the weights of that layer***!)

## Keras - Do we always have to construct the embedding vectors from scratch, or can we use existing embeddings?

Two options:

1. `model.add(Embedding(vocab_size, 8, input_length=max_length))` will add an `embedding layer` with ***random weights***, and ***it will learn the embeddings from the inputs and previous layers** (the embeddings are actually **the weights in that layer**)**.***

2. 

`model.add(Embedding(vocab_size, 100, weights=[embedding_matrix], input_length=4, trainable=False))`

Here, we use an existing `embedding matrix` that we constructed from open-source word embeddings (i.e. the one from `GloVe` for Twitter).

By passing the `weights` directly, and marking the layer as **non-trainable**, it will be used directly in the NN!

## What does *`TextVectorization`* do?

It is a **NN layer** that will ***normalize (e.g. remove <br />, padding, ...),*** and ***map strings*** to ***integers***.

Once you have constructed the vocabulary for that layer with *adapt (see below)*, **you can use that layer as the input layer to the embedding layer**!

## What does *`TextVectorization.adapt`* do?

Given ***text data*** (i.e. *data without the labels*), it ***constructs the vocabulary*** for the layer (Not 100% sure of why that's useful at that stage...)

You can then get it with `vectorize_layer.get_vocabulary()`.

## Idea for later optimization

1. **Use glove embeddings** (they already trained the NN for us here!)
2. If using *glove embeddings*, **remove the words that we don't have in our vocabulary** (since we have the training data, and the test inputs from the challenge, we have *all of our vocabulary!*)
    1. Would be interesting to test ***without filtering words**,* and with the filtering (in particular, *dataset size* vs *accuracy*) → Accuracy should be identical, and ideally, dataset size should be *much smaller*.
