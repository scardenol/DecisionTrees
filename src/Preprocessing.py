import pandas as pd  # Imports the library "pandas" as "pd"
import numpy as np  # Imports the library "numpy" as "np"

"""
This function is based on the pandas library to read a csv file. It utilizes the read_csv,
convert_dtypes and columns functions of pandas. It handles the preprocessing proces of the
data by properly handling the filename, separator, na values and data types of the array
obtained using pandas.

Inputs:
    filename: string with filename in the following format "name.csv"
    sep: separator used in csv file. "," set as default.
    keep_default_na: choose to keep default na values. Set to true by default.

Outputs:
    data: pandas array properly preprocessed.
    col_names: pandas Index object that contains the column names of the data.
"""


def preprocess_data(filename, sep=",", keep_default_na=True):

    # Reads csv file with separator ";" without keeping the na values
    data = pd.read_csv(filename,
                       sep=";", keep_default_na=False)

    # Correction of column data types
    data = data.convert_dtypes()

    # Column names of data
    global col_names  # Variable set as global in order to be used in another module by foo()
    col_names = data.columns

    return data, col_names


"""
A basic function that converts the array obtained by using pandas into a list. It utilizes
the numpy function to handle it as a numpy array an then it uses the function tolist() to
finish the process.

Input:
    data: pandas array properly preprocessed.
Output:
    np.array(data).tolist(): the preprocessed dataset (list of listed rows).
"""


def convert_to_list(data):
    return np.array(data).tolist()


"""
Function with no input. Takes the global value col_names and returns it. The use of this
function is to be imported in the Decision_Tree module in order to use the variable
col_names when the function preprocess_data is called, using the current column names of
the preprocessed data set.

Output:
    col_names: current column names of the preprocessed data set of with the preprocess_data
    function.
"""


def foo():
    return col_names
