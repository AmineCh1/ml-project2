from gingerit.gingerit import GingerIt
from datetime import datetime

parser = GingerIt()

counter = 0

start = datetime.now()

# Positive tweets only for now
tweets = open("../data/train/train_neg_5000.txt", "r")
output = open("../data/train/train_neg_5000_ginger.txt", "w")

for tweet in tweets:
    parser_result = parser.parse(tweet)
    if 'result' in parser_result:
        output.write(parser_result['result'])
    else:
        print('Woops, there was a problem here...', parser_result)

    counter += 1

    if counter % 10 == 0:
        print(counter)
        print(datetime.now() - start)

tweets.close()
output.close()

# 67% to 72% for 3.3k tweets, very impressive...
#
# But slow and unreliable...Also seems to call a web API :D
