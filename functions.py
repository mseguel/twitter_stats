import pandas as pd
import json


def retweeted(dataset):  # 1. Los top 10 tweets más retweeted.
    print('Los 10 tweets más retweeted son:')
    print(dataset)
    # print(dataset.head())


# 2. Los top 10 usuarios en función a la cantidad de tweets que emitieron.
def usuarios(dataset):
    print("Los 10 usuarios que mas tweets emitieron son:")


def dias(dataset):  # 3. Los top 10 días donde hay más tweets.
    print("Los 10 días donde hay más tweets son:")


def usados(dataset):  # 4. Top 10 hashtags más usados
    print("Los 10 hashtags más usados son:")


if __name__ == "__main__":
    # with open('farmers-protest-tweets-2021-03-5.json', 'r') as file:
    #     data = file.readlines()

    # with open('data/farmers-protest-tweets-2021-03-5.json') as json_file:
    #     data = json.load(json_file)
    # print(data)

    f = open('data/farmers-protest-tweets-2021-03-5.json', "r")

    # Reading from file
    data = json.loads(f.read())

    # data = pd.read_json(
    # 'data/farmers-protest-tweets-2021-03-5.json', lines=True)

    # retweeted(data)
    # usuarios(datsa)
    # dias(data)
    # usados(data)
