**Names:** Danilo de Jesús Toro Echeverri, Salomón Cardeño Luján

**Context:**
The given context is to make predictions on the academic success (*éxito académico*) in
higher education (*educación superior*) using decision trees. The academic success in
this scope is defined as the probability that a student gets a total score superior to his
cohort's average, in the *Pruebas Saber Pro* test.

**Problem:**
Design an algorithm based on decision trees and the *Saber 11* data to predict whether a
student will have a total score, in the *Pruebas Saber Pro*, above average or not.

**About the data:**
The datasets in https://github.com/mauriciotoro/ST0245-Eafit/tree/master/proyecto/datasets
were the ones assigned to the project, where the training and test data are available as
different ```.csv``` files.

**General description:** 
The program takes a ```.csv``` file of training data, builds a decision tree based
on the CART algorithm and classifies a ```.csv``` file of testing data, making predictions
for the column with label *exito* (success).

**Code execution:**
To run the code simply execute the ```main.py``` file, which is the run script for the code.
A flow of the execution process as well as the main functions called is shown in the image below.

![Imgur](https://i.imgur.com/l5hJKf6.png)

The functions in orange represent the functions loaded from the ```Preprocessing.py``` module,
while the ones in green are loded from the ```Decision_Tree.py```. An example is already programmed
in the main script, and as the execution flow shows the output is seen in terminal. Generally
speaking, each function's role is as follows:

```preprocess_data``` This function is based on the pandas library to read a csv file. It utilizes
the read_csv, convert_dtypes and columns functions of pandas. It handles the preprocessing process of
the data by properly handling the filename, separator, na values and data types of the array
obtained using pandas.

```convert_to_list``` A basic function that converts the array obtained by using pandas into a list.
It utilizes the numpy function ```array()``` to handle it as a numpy array an then it uses the function
```tolist()``` to finish the process.

```build_tree``` This function constructs the decision tree of a given dataset based on the CART algorithm.
It has control over the maximum depth allowed for the tree; by default it has no value so
it grows the whole tree, but it can be changed to any positive integer to determine the
depth to stop building. To keep track of the depth it uses a level parameter with initial
value 0 that isn't supposed to be changed by the user, but it's necessary when making the
recursion calls. Since the algorithm is recursive, we'll get a Question node or an instance
of a Decision_Node after each recursive call until the base case is reached, and when this
happens, we'll get a Leaf.

```print_tree``` This function is used to print the tree previously built. It's implemented recursively
and prints the tree by printing it node by node.

```classify``` This function takes a row of the data set and the instance of Decision_Node resulted when
building the tree. It decides whether to follow the true-branch or the false-branch, compares
the feature and value stored in the node (Tree) to the example (row) we're considering. The
base case is reached when we've reached a leaf, in that case we return the attribute predictions
of the Leaf instance. This function is usually used within a for cycle that goes through the
testing dataset.

```print_leaf``` This function takes the output of the classify function (counts dictionary) and constructs
a dictionary with the proportion (probability) instead of counts.

**How to use program:**
To use, look at the example below and input the following:

**1.** Call the ```preprocess_data``` function for the training and testing data with adequate input parameters
as follows:
```
train, col_names = p.preprocess_data(
    "0_train_balanced_15000.csv", sep=";", keep_default_na=False)

test, _ = p.preprocess_data(
    "0_test_balanced_5000.csv", sep=";", keep_default_na=False)
```

**2.** followed by the ```convert_to_list``` function for each dataset
```
ltrain = p.convert_to_list(train.iloc[0:150, :])
ltest = p.convert_to_list(test.iloc[0:50, :])
```

**3.** build the tree with ```build_tree``` and print it with ```print_tree```
```
T = d.build_tree(ltrain, max_depth=2)
d.print_tree(T)
```

**4.** use the functions ```classify``` and ```print_leaf``` with the following code:
```
correct_predictions = 0
for row in ltest:
    print("Actual: %s. Predicted: %s" %
          (row[-1], d.print_leaf(d.classify(row, T))))
    leaf = d.classify(row, T)
    if leaf[row[-1]] > leaf[abs(row[-1] - 1)]:
        correct_predictions += 1

success_of_tree = correct_predictions / len(ltest) * 100
print("Success of Tree's predictions: %s %%" % (success_of_tree))
```
**Operating system version:** Microsoft Windows 10 Home Single Language

**Python version:** 3.9.0
