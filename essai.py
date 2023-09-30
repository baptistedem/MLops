import pandas as pd
import os
# df = pd.read_csv("data/restaurant_1_week_002.csv")

# Répertoire contenant les fichiers CSV
directory = 'data'

# Obtenez la liste des fichiers CSV dans le répertoire
csv_files = [f for f in os.listdir(directory) if f.startswith('restaurant_1') and f.endswith('.csv')]
csv2_files = [f for f in os.listdir(directory) if f.startswith('restaurant_2') and f.endswith('.csv')]

# Créez une liste vide pour stocker les DataFrames chargés à partir de chaque fichier
dfs = []

# Boucle pour charger chaque fichier et l'ajouter à la liste des DataFrames
for file in csv_files:
    file_path = os.path.join(directory, file)
    df = pd.read_csv(file_path)
    dfs.append(df)


    

# Concaténez les DataFrames en utilisant pd.concat
concatenated_df = pd.concat(dfs, axis=0)  # Par lignes

# Enregistrez le DataFrame concaténé dans un nouveau fichier CSV
concatenated_df.to_csv('fichiers_concatenes.csv', index=False)

#restaurant 2
dfsd = []
for file in csv2_files:
   file_path = os.path.join(directory, file)
   df = pd.read_csv(file_path)
   dfsd.append(df)

concatenated_df = pd.concat(dfsd, axis=0)  # Par lignes
concatenated_df.to_csv('fichiers_concatenes2.csv', index=False)




# Maintenant, vous pouvez effectuer diverses opérations sur le DataFrame, par exemple, afficher les premières lignes :
df = pd.read_csv('fichiers_concatenes.csv')
df2 = pd.read_csv('fichiers_concatenes2.csv')
# Utilisez la fonction head() pour afficher un aperçu des premières lignes du DataFrame

# Affichez l'aperçu
print(df.head())
print(df2.head())

df2 = df2.rename(columns=df.columns)
print(df.head())
print(df2.head())

