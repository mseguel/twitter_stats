from itertools import count
import pandas as pd
import json
import re


def retweeted(dataset):  # 1. Los top 10 tweets más retweeted.
    print('Los 10 tweets más retweeted son:')
    dataset.set_index(['retweetCount'])
    print(dataset.nlargest(n=10, columns=['retweetCount'])[['retweetCount', 'content']])


# 2. Los top 10 usuarios en función a la cantidad de tweets que emitieron.
def usuarios(dataset):
    print("Los 10 usuarios que mas tweets emitieron son:")
    list_users = []
    for i in range(len(dataset)):
        data_user = dataset.iloc[i]['user']
        list_users.append(data_user['username'])
    data_usernames = pd.DataFrame(list_users, columns=['Username'])
    count_usernames = data_usernames['Username'].value_counts()
    top_username = pd.DataFrame({'Username': count_usernames.index, 'Frecuencia': count_usernames.values})
    print(top_username.nlargest(n=10, columns=['Frecuencia'])[['Username', 'Frecuencia']].to_string(index=False))
        


def dias(dataset):  # 3. Los top 10 días donde hay más tweets.
    print("Los 10 días donde hay más tweets son:")
    dataset['fecha'] = [d.date() for d in dataset['date']]
    fechas_count = dataset['fecha'].value_counts()
    top_fechas = pd.DataFrame({'Fecha':fechas_count.index, 'Frecuencia':fechas_count.values})
    print(top_fechas.nlargest(n=10, columns=['Frecuencia'])[['Fecha', 'Frecuencia']].to_string(index=False))


def usados(dataset):  # 4. Top 10 hashtags más usados
    print("Los 10 hashtags más usados son:")
    list_hashtags = []
    for i in range(len(dataset)):
        list_hashtags += re.findall(r"#(\w+)", dataset.iloc[i]['content'])
    data_hashtags = pd.DataFrame(list_hashtags, columns=['Hashtag'])
    count_hashtag = data_hashtags['Hashtag'].value_counts()
    top_hashtag = pd.DataFrame({'Hashtag': count_hashtag.index, 'Frecuencia': count_hashtag.values})
    print(top_hashtag.nlargest(n=10, columns=['Frecuencia'])[['Hashtag', 'Frecuencia']].to_string(index=False))


# "url": "https://twitter.com/ShashiRajbhar6/status/1376739399593910273", 
# "date": "2021-03-30T03:33:46+00:00", 
# "content": "Support \ud83d\udc47\n\n#FarmersProtest", 
# "renderedContent": "Support \ud83d\udc47\n\n#FarmersProtest", 
# "id": 1376739399593910273, 
# "user": {"username": "ShashiRajbhar6", "displayname": "Shashi Rajbhar", "id": 1015969769760096256, "description": "Satya presan \ud83e\udd14ho Sakta but prajit\ud83d\udcaa nhi\njhuth se samjhauta kbhi nhi\nJai Shree Ram \ud83d\udd49 \ud83d\ude4f\ud83d\udd49 followed by hon'ble @ArunrajbharSbsp", "rawDescription": "Satya presan \ud83e\udd14ho Sakta but prajit\ud83d\udcaa nhi\njhuth se samjhauta kbhi nhi\nJai Shree Ram \ud83d\udd49 \ud83d\ude4f\ud83d\udd49 followed by hon'ble @ArunrajbharSbsp", "descriptionUrls": [], "verified": false, "created": "2018-07-08T14:44:03+00:00", "followersCount": 1788, "friendsCount": 1576, "statusesCount": 14396, "favouritesCount": 26071, "listedCount": 1, "mediaCount": 254, "location": "Azm Uttar Pradesh, India", "protected": false, "linkUrl": null, "linkTcourl": null, "profileImageUrl": "https://pbs.twimg.com/profile_images/1354331299868237825/eDzdhZTD_normal.jpg", "profileBannerUrl": "https://pbs.twimg.com/profile_banners/1015969769760096256/1613727783", "url": "https://twitter.com/ShashiRajbhar6"}, 
# "outlinks": [], 
# "tcooutlinks": [], 
# "replyCount": 0, 
# "retweetCount": 0, 
# "likeCount": 0, 
# "quoteCount": 0, 
# "conversationId": 1376739399593910273, 
# "lang": "en", 
# "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>", 
# "sourceUrl": "http://twitter.com/download/android", 
# "sourceLabel": "Twitter for Android", 
# "media": null, 
# "retweetedTweet": null, 
# "quotedTweet": null, 
# "mentionedUsers": null}



if __name__ == "__main__":
    # with open('farmers-protest-tweets-2021-03-5.json', 'r') as file:
    #     data = file.readlines()

    # with open('data/farmers-protest-tweets-2021-03-5.json') as json_file:
    #     data = json.load(json_file)
    # print(data)


    # Reading from file
    # f = open('data/farmers-protest-tweets-2021-03-5.json', "r")
    # data = json.loads(f.read())

    # data = pd.read_json('data/farmers-protest-tweets-2021-03-5.json', lines=True)
    data = pd.read_json('data/test.json')
    # print(data['user'].iloc[3])

    retweeted(data)
    # usuarios(data)
    # dias(data)
    # usados(data)
