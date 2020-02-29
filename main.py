# %% Read csv from file
import pandas as pd

data = pd.read_csv("starter_startup.csv", sep=";")

# %% Utils
import math


def normalize_twitter_name(twitter_url):
    if isinstance(twitter_url, str):
        return re.split(r'twitter.com/', twitter_url)[-1].lower()
    if math.isnan(twitter_url):
        return None
    raise Exception('not valid values for Twitter Handler')



# %% Work with the csv
# data["Company name"] = data["Company name"].str.strip()
# data["Company Twitter"] = data["Company Twitter"].apply(normalize_twitter_name)
# data["Nb. of Employees"] = data["Nb. of Employees"].astype('category')
# data["What do they do (Verbatim - 10 words max.)   "]
data[data["Link to website"].str[:8] != "https://"]["Link to website"].head()
# %% Experiments
import re

cosa = "https://twitter.com/Bitnami"
cosa = re.split(r'twitter.com/', cosa)[-1]
