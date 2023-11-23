import sys
import pandas as pd 

dataset =  pd.read_csv('./data/dataset/movies.csv', encoding='utf-8')


# =============================== COPY THE CODE BELOW ====================================

raw_country_movie_directors = dataset['director'].astype(str)

for e in raw_country_movie_directors:
    try:
        # Écrire la chaîne encodée en UTF-8
        sys.stdout.buffer.write(f'{e}\n'.encode('utf-8'))
        
        # Récupérer une chaîne de caractères à partir des octets
        encoded_bytes = e.encode('utf-8')
        decoded_string = encoded_bytes.decode('utf-8')
        
        # Imprimer la chaîne de caractères
        print(decoded_string)

    except UnicodeEncodeError:
        print(f"Erreur d'encodage pour la valeur : {e}")