import pandas as pd 

dataset =  pd.read_csv('./data/dataset/movies.csv', encoding='utf-8')


# =============================== COPY THE CODE BELOW ====================================

raw_country_movie_gender = dataset['genres'].astype(str)


data  =  [(gender, element) for gender in raw_country_movie_gender for element in gender.split(', ')]
data = sorted(list(set(data)))

df_movie_gender = pd.DataFrame(data, columns=['movie_gender_combinaison', 'movie_gender'])
print(df_movie_gender)