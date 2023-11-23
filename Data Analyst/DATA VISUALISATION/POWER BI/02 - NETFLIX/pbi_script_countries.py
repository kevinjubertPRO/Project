import pandas as pd 

dataset =  pd.read_csv('./data/dataset/movies.csv', encoding='utf-8')


# =============================== COPY CODE BELOW ====================================

raw_countries = dataset['country'].astype(str)

# Utilisez une approche de liste en compréhension pour créer la liste 'data'
data = [(country, element) for country in raw_countries for element in country.split(', ')]
data = sorted(list(set(data)))

# Créez directement le DataFrame à partir de la liste 'data'
df_countries = pd.DataFrame(data, columns=['country_combinaison', 'country'])
print(df_countries)