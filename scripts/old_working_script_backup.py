# Autoreload the data_cleaning library, for faster tests
%load_ext autoreload
%autoreload 1
%aimport data_cleaning

# Import the raw data
raw_train_pos = pd.read_table("data/train/train_pos.txt", names=["tweet"], sep = "\n", header=None,quoting=3)
raw_train_neg = pd.read_table("data/train/train_neg.txt", names=["tweet"], sep = "\n", header=None, quoting=3)

# Drop duplicates
raw_train_pos = raw_train_pos.drop_duplicates()
raw_train_neg = raw_train_neg.drop_duplicates()

# Construct the preprocessed version of the tweets on the fly.
pre_train_pos = pd.DataFrame(columns = ['tweet'])
pre_train_neg = pd.DataFrame(columns = ['tweet'])
pre_train_pos.tweet = raw_train_pos.tweet.apply(data_cleaning.preprocess_tweet)
pre_train_neg.tweet = raw_train_neg.tweet.apply(data_cleaning.preprocess_tweet)

### --------------------
batch_size = 64

raw_train_pos['pred'] = 1
raw_train_neg['pred'] = 0

#########################################################################
########### TESTING ONLY - Take only 25% of the whole dataset ###########
#########################################################################
# pos_total = len(raw_train_pos)
# neg_total = len(raw_train_neg)
# raw_train_pos = raw_train_pos[:int(pos_total * .25)]
# raw_train_neg = raw_train_neg[:int(neg_total * .25)]
#########################################################################
#########################################################################
#########################################################################

# Form training data
raw_train = pd.concat((raw_train_neg,raw_train_pos))

# Separating training and validation data
raw_train_tr,raw_train_val  = split_set(raw_train.sample(frac=1,random_state=0))

target_train_tr = raw_train_tr.pop('pred')
target_train_val = raw_train_val.pop('pred')

print(np.squeeze(raw_train_tr.tweet.values))
print(target_train_tr.values)

# Turning Pandas dataframes into Tensorflow datasets
raw_train_ds = tf.data.Dataset.from_tensor_slices((np.squeeze(raw_train_tr.values), target_train_tr.values))
raw_val_ds = tf.data.Dataset.from_tensor_slices((np.squeeze(raw_train_val.values),target_train_val.values))

# Batchify data
raw_train_ds = raw_train_ds.batch(batch_size=batch_size)
raw_val_ds = raw_val_ds.batch(batch_size=batch_size)

print(
    "Number of batches in raw_train_ds: %d"
    % tf.data.experimental.cardinality(raw_train_ds)
)
print(
    "Number of batches in raw_val_ds: %d" % tf.data.experimental.cardinality(raw_val_ds)
)

######################################
### Construct the embedding layer ####
######################################

max_words_in_vocab = 10000
embedding_dim = 32
sequence_length = 280

vectorize_layer = TextVectorization(
    max_tokens=max_words_in_vocab, # We only consider the top "max_words_in_vocab" words for the vocabulary
    output_mode="int",
    output_sequence_length=sequence_length, # We pad our outputs to 280 characters
)

# Keep only text
text_ds = raw_train_ds.map(lambda x, y: x)

vectorize_layer.adapt(text_ds)

####################################
########### FUN TUTORIAL ###########
####################################

# Print the top 10 words of our vocabulary
# vectorize_layer.get_vocabulary()[:10]

# Test the vectorizer
# output = vectorize_layer([["the cat sat on the mat"]])
# output.numpy()[0, :6]
### --------------------
def vectorize_text(text, label):
    text = tf.expand_dims(text, -1)
    return vectorize_layer(text), label

# Vectorize the data.
train_ds = raw_train_ds.map(vectorize_text)
val_ds = raw_val_ds.map(vectorize_text)
# test_ds = raw_test_ds.map(vectorize_text)

# Do async prefetching / buffering of the data for best performance on GPU.
train_ds = train_ds.cache().prefetch(buffer_size=10)
val_ds = val_ds.cache().prefetch(buffer_size=10)
# test_ds = test_ds.cache().prefetch(buffer_size=10)
### --------------------
embedding_layer = layers.Embedding(max_words_in_vocab, embedding_dim, input_length=sequence_length)
### --------------------
model = tf.keras.Sequential()
model.add(embedding_layer)
model.add(layers.Flatten())
model.add(layers.Dense(1, activation='sigmoid', kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01)))
model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy']) 
print(model.summary())
### --------------------
epochs = 4
# Fit the model using the train and test datasets.
model.fit(train_ds, validation_data=val_ds, epochs=epochs)
### --------------------
