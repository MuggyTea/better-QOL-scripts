from TextGenerator.PrepareChain import *
import pandas as pd
from tqdm import tqdm
import sys
import csv
from datetime import datetime

# 書き込み用のタイムスタンプ
time = datetime.now().strftime("%Y_%m_%d_%H:%M:%S")

def storeTweetstoDB():

    if len(sys.argv) > 2:
        df = pd.read_csv(sys.argv[1])
    else:
        csvfilepath = input('tweet_datas/processedtweets.csv filepath : ')
        df = pd.read_csv(csvfilepath)


    tweets = df['text']

    print(len(tweets))

    chain = PrepareChain(tweets[0])
    triplet_freqs = chain.make_triplet_freqs()
    chain.save(triplet_freqs, True)

    with open('/Users/user/python-tips/tweet_generation/bot_tweet/' + time + '.csv', 'w') as f:
        for i in tqdm(tweets[1:]):
            chain = PrepareChain(i)
            triplet_freqs = chain.make_triplet_freqs()
            chain.save(triplet_freqs, False)
            print(triplet_freqs)
            f.write(str(triplet_freqs)+'\n')



if __name__ == '__main__':
    storeTweetstoDB()