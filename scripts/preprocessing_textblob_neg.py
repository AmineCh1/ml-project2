 #!/usr/bin/python3

from textblob import TextBlob

counter = 0

# Positive tweets only for now
tweets = open("train_neg.txt", "r")
output = open("train_neg_textblob.txt", "w")
for tweet in tweets:
    output.write(str(TextBlob(tweet).correct()))
    counter += 1

    if counter % 10 == 0:
        print(counter)

tweets.close()
output.close()

# Verdict: Makes too many corrections: doesn't understand some lingo...a bit dangerous I'd say!
