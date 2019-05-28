import pandas as pd
import re

df = pd.read_csv('tweet_datas/tweets.csv')

tweets = df['text']

replypattern = '@[\w]+'
retweetpattern = 'RT'
urlpattern = 'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+'

processedtweets = []

for tweet in tweets:
    # RTは省く
    if retweetpattern in tweet:
        continue
    # リプライは、@マークだけ省いて文章のみ含める
    i = re.sub(replypattern, '', tweet)
    # URLも消す
    i = re.sub(urlpattern, '', i)
    if isinstance(i, str) and not i.split():
        pass
    else:
        processedtweets.append(i)

processedtweetsDataFrame = pd.Series(processedtweets)
newDF = pd.DataFrame({'text': processedtweetsDataFrame})
# 前処理後のツイート
newDF.to_csv('tweet_datas/processedtweets.csv')