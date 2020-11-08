import pandas as pd # Importa el paquete pandas como pd
# Lectura del archivo como un csv
data = pd.read_csv("0_train_balanced_15000.csv",sep=";")
# Imprime la "cabeza" del archivo
data.head()