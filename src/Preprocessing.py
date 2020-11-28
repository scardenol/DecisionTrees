import pandas as pd  # Imports the library "pandas" as "pd"
import numpy as np  # Imports the library "numpy" as "np"


def preprocess_data(filename, sep=",", keep_default_na=True):

    # Reads csv file with separator ";" without keeping the na values
    data = pd.read_csv(filename,
                       sep=";", keep_default_na=False)

    # Correction of column data types
    data = data.convert_dtypes()

    # Column names of data
    global col_names
    col_names = data.columns

    return data, col_names


def convert_to_list(data):
    return np.array(data).tolist()


def foo():
    return col_names
