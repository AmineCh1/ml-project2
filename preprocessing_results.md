# Raw dataset (without duplicates)

## 1/5th of the full dataset

Epoch 1/4
7092/7092 [==============================] - 18s 3ms/step - loss: 0.4825 - accuracy: 0.7830 - val_loss: 0.4494 - val_accuracy: 0.7991
Epoch 2/4
7092/7092 [==============================] - 16s 2ms/step - loss: 0.4368 - accuracy: 0.8076 - val_loss: 0.4371 - val_accuracy: 0.8032
Epoch 3/4
7092/7092 [==============================] - 14s 2ms/step - loss: 0.4250 - accuracy: 0.8124 - val_loss: 0.4320 - val_accuracy: 0.8046
Epoch 4/4
7092/7092 [==============================] - 14s 2ms/step - loss: 0.4183 - accuracy: 0.8152 - val_loss: 0.4296 - val_accuracy: 0.8060

# Cleaned-up dataset (without duplicates)

## 1/5th of the full dataset

Epoch 1/4
6944/6944 [==============================] - 17s 2ms/step - loss: 0.4879 - accuracy: 0.7791 - val_loss: 0.4559 - val_accuracy: 0.7955
Epoch 2/4
6944/6944 [==============================] - 15s 2ms/step - loss: 0.4443 - accuracy: 0.8020 - val_loss: 0.4434 - val_accuracy: 0.8004
Epoch 3/4
6944/6944 [==============================] - 14s 2ms/step - loss: 0.4327 - accuracy: 0.8067 - val_loss: 0.4383 - val_accuracy: 0.8025
Epoch 4/4
6944/6944 [==============================] - 15s 2ms/step - loss: 0.4261 - accuracy: 0.8096 - val_loss: 0.4359 - val_accuracy: 0.8032

# Q&A

## Why have we removed the duplicates?

We had a better validation score, but that would lead to overtraining.

## What else have we tried?

Grammar corrections worked quite fine, but were impractical: too slow, correcting too much, ...
