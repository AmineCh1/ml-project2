import argparse


def main(file, batches):
    tweets_batches= []
    with open(file) as txt_file:
        
        batch_size = len(txt_file.readlines())//batches
        txt_file.seek(0)

        for j in range(batches):
            batch = []
            for i in range(batch_size):
                batch.append(txt_file.readline())
            print(batch)
            tweets_batches.append(batch)

    for i, batch in enumerate(tweets_batches):
        with open("../data/batches/{}_small{}.txt".format(file,i),'w') as to_write:
            to_write.writelines("%s" % tweet for tweet in batch)


parser = argparse.ArgumentParser(
    prog='Gensmall', description=" Generate a smaller file because my computer cannot handle it.")
parser.add_argument("--file")
parser.add_argument("--batches", help= " Number of batches to generate",type=int)
args = parser.parse_args()

main(args.file,args.batches)