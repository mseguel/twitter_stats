import pandas as pd
import re


def retweeted(dataset):  # 1. Los top 10 tweets más retweeted.
    print('Los 10 tweets más retweeted son:')
    top_retweeted = dataset.nlargest(n=10, columns=['retweetCount'])[['retweetCount', 'content']]
    top_retweeted = top_retweeted.set_index(['retweetCount'])
    top_retweeted['content'] = top_retweeted['content'].str.slice(0,50)
    print(top_retweeted)


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


if __name__ == "__main__":
    # data = pd.read_json('data/farmers-protest-tweets-2021-03-5.json', lines=True)
    data = pd.read_json('data/test.json')

    # retweeted(data)
    # usuarios(data)
    dias(data)
    # usados(data)
