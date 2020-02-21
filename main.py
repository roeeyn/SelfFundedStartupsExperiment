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
    raise Exception('valio vrg')


# %% Work with the csv
# data["Company name"] = data["Company name"].str.strip()
data["Company Twitter"].apply(normalize_twitter_name)

# %% Experiments
import re

cosa = "https://twitter.com/Bitnami"
cosa = re.split(r'twitter.com/', cosa)[-1]
