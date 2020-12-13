 #!/usr/bin/python3

from textblob import TextBlob

counter = 0
tweets = open("../data/test/test_data_wo_indices.txt", "r")
output = open("../data/test/test_data_wo_indices_textblob.txt", "w")
for tweet in tweets:
    output.write(str(TextBlob(tweet).correct()))
    counter += 1

    if counter % 10 == 0:
        print(counter)

tweets.close()
output.close()

# Verdict: Makes too many corrections: doesn't understand some lingo...a bit dangerous I'd say!
