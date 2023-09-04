import pandas as pd

dataset = pd.read_csv("../data/amazon_prime_titles.csv")

#Shape data
dataset.shape

#Dataset columns
dataset.columns

#Dataset info
dataset.info()


#Checking duplicates in dataset
dataset.duplicated().sum()

#Rename columns
dataset.rename(columns={'listed_in':'genre'},inplace=True)

#Handling null values
dataset.isnull().sum()

dataset['director'].fillna("Unavailable", inplace=True)
dataset['cast'].fillna("Unavailable", inplace=True)
dataset['country'].fillna("Unavailable", inplace=True)
dataset['rating'].fillna("Unavailable", inplace=True)
dataset['date_added'] = dataset['date_added'].ffill()

dataset['date_added']= pd.to_datetime(dataset['date_added'], format='%B %d, %Y')

#Saving processed dataset
dataset_clean = pd.DataFrame(dataset)
dataset_clean.to_csv("../data/amazon_prime_titles_clean.csv")



