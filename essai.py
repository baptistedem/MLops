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
'''print(df.head())
print(df2.head())

df2 = df2.rename(columns=df.columns)
print(df.head())
print(df2.head())
'''

'''
créer une onction clean qui prend un dataframe et retourn un datafram
- mettre le nom des colonne en minuscule, remplace espace par under score
- caster la colonne order date en datetime (pd todatetime)
-renommer la colonne order_id en order number
creer la colonne chiffre d'affaire à maille order id
'''
def extract(data_dir, prefix, start_week, end_week):
    """ Extract a temporal slice of data for a given data source.
    
    Parameters
    ----------
    data_dir: str
        Data directory path.
    start_week: int
        First week number (included)
    end_week: int
        Last week number (included)
    prefix: str
        Data source identification (e.g. restaurant_1)
    """
    df = pd.DataFrame()
    
    for i in range(start_week, end_week+1):
        file_path = os.path.join(data_dir, 'data', f'{prefix}_week_{i}.csv')

        if os.path.isfile(file_path):
            batch = pd.read_csv(file_path)
            df = pd.concat([df, batch], sort=True)
    
    return df

def clean(df):
    """Clean dataframe."""
    
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df['order_date'] = pd.to_datetime(df['order_date'])
    df = df.rename(columns={'order_number': 'order_id'})
    df = df.sort_values('order_date')
    df['total_product_price'] = df['quantity'] * df['product_price']
    df['cash_in'] = df.groupby('order_id')['total_product_price'].transform(np.sum)
    df = df.drop(columns=['item_name', 'quantity', 'product_price', 
                          'total_products', 'total_product_price'],
                errors="ignore")
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    return df

df1 = extract(data_dir= "C:/Users/277775/MLops/data",
       prefix="restaurant_1" , start_week=108, end_week=110)
df1 = clean(df1)
df1.head()
