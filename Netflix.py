import pandas as pd
import numpy as np
df = pd.read_csv(r'C:\python projects\Netflix\netflix_titles.csv')
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['main_country'] = df['country'].apply(lambda x: x.split(',')[0].strip())
df.dropna(subset=['rating'], inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'].str.strip())
df['duration_season'] = df['duration'].str.extract(r'(\d+)\s+Season', expand=False).astype(float)
df['duration_min'] = df['duration'].str.extract(r'(\d+) min').astype(float)
rating_map = {
    'TV-Y': 'Kids', 'TV-Y7': 'Kids', 'TV-Y7-FV': 'Kids', 'G': 'Kids', 'TV-G': 'Kids',
    'PG': 'Kids', 'TV-PG': 'Kids',
    'PG-13': 'Teens', 'TV-14': 'Teens',
    'R': 'Adults', 'TV-MA': 'Adults', 'NC-17': 'Adults',
    'NR': 'Unrated', 'UR': 'Unrated'
}
df['rating_category'] = df['rating'].map(rating_map)
df.drop_duplicates(subset=['title', 'type','release_year'], keep='last', inplace=True)

df.to_csv(r'C:\python projects\Netflix\cleaned_netflix.csv', index=False, encoding='utf-8')
