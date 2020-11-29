import Preprocessing as p


"""
This function finds the unique values  for a specific column of a given data set and
returns them as a set.

Inputs:
    dataset: is the preprocessed training data set (list of listed rows).
    column: is the desired column (int).
Output:
    Set of the unique column values (i.e. ignores repeated values).
"""


def unique_colvalues(dataset, column):
    return set([row[column] for row in dataset])


"""
This function counts the unique values for a specific column of a given data set and
returns a dictionary of the results. The default column value is set to -1 as usually the
column of interest for this function is the last, but it could be used with any column.

Inputs:
    dataset: is the preprocessed training data set (list of listed rows).
    column: is the desired column (int). Default value is -1.
Output:
    counts: Dictionary of label -> count.
"""


def count_colvalues(dataset, column = -1):
    counts = {}  # a dictionary of label -> count.
    for row in dataset:
        # in our data set format, the label of interest is the last column
        label = row[column]  # Hence -1
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


"""
This function tests if a value is numeric or not and returns the boolean for each case.

Input:
    value: any input data type.
Output:
    True in case the input is an integer or float, False otherwise.
"""


def is_numeric(value):
    return isinstance(value, int) or isinstance(value, float)


class Question:
    """
    This class is created because the idea is to use a Question to partition the dataset.

    The class takes a given column number and a value and stores them. Then it uses the 
    "match" function to compare the given value with the value stored in the question,
    returning the resulting boolean value. Notice the "match" function considers both
    numerical and categorical questions.
    """

    """
    Constructor for a Question, which is constructed with a column number and a value
    (numerical or categorical), i.e., Question(column,value).
    """

    def __init__(self, column, value):
        self.column = column
        self.value = value

    """
    Compares an example value with the value stored in the question. It makes a call to
    the is_numeric() function and it returns the boolean value of the stated comparison
    for each case.

    Inputs:
        self: the instance of the class, in other words, a stored question.
        example: a value to confront the question.
    Output:
        Boolean value of the comparison (numerical or categorical).
    """

    def match(self, example):
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    """
    Method or function to represent the question in the format "is ... ?"
    """

    def __repr__(self):
        condition = "=="
        col_names = p.foo()
        if is_numeric(self.value):
            condition = ">="
        return "is %s %s %s?" % (
            col_names[self.column], condition, str(self.value))


"""
The function makes a partition of the given data set based on a given question. For each
row in the dataset it checks if it matches the question, if it does the matched row is
added to the "true dataset" list, if it doesn't is added to the "false dataset" list.

Inputs:
    dataset: is the preprocessed training data set (list of listed rows).
    question: an instance of the class Question, i.e., a question.
Outputs:
    true_dataset: list of rows that matched the question asked.
    flase_dataset: list of rows that didn't match the question asked.
"""


def partic(dataset, question):
    true_dataset, false_dataset = [], []
    for row in dataset:
        if question.match(row):
            true_dataset.append(row)
        else:
            false_dataset.append(row)
    return true_dataset, false_dataset


"""
This function calculates the Gini Impurity for a given dataset.

Input:
    dataset: is the preprocessed training data set (list of listed rows).
Output:
    impurity: numeric value of the Gini Impurity of the dataset; a numeric value between
    0 and 0.5 which indicates the likelihood of new random data being misclassified if it
    were given a random class label according to the class distribution in the dataset.
"""


def gini(dataset):
    counts = count_colvalues(dataset)
    impurity = 1
    for lbl in counts:
        pi = counts[lbl] / float(len(dataset))
        impurity -= pi**2
    return impurity


"""
This function calculates the information gain, which is definied as the uncertainty of
the starting or parent node minus the weighted impurity (gini impurity) of the two child
nodes. Its use is usually to calculate how much information we gain when partitioning the
data by a given question.

Inputs:
    left: left child node.
    right: right child node.
    current_uncertainty: uncertainty of the parent node.
Output:
    Information gain, a numeric value within the range 0-1 where 0 means the node is the
    purest possible and 1 means the opposite.
"""


def info_gain(left, right, current_uncertainty):
    """Information Gain.

    The uncertainty of the starting node, minus the weighted impurity of
    two child nodes.
    """
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)


"""
This function finds the best question to ask that splits the data with the most
information gain. It does this by iterating over every column (feature) over every row
(value) of the dataset. Over each column it uses the unique column values and for each of
them it asks a question to split the data set keeping track of the information gain.

Input:
    dataset: is the preprocessed training data set (list of listed rows).
Outputs:
    best_gain: best information gain obtained by spliting the data using the best
    question (float).
    best_question: question that better splits the data, i.e., that results in the
    best information gain (Question instance).
"""


def find_best_split(dataset):
    best_gain = 0  # keep track of the best information gain
    best_question = None  # keep train of the feature / value that produced it
    current_uncertainty = gini(dataset)
    n_features = len(dataset[0]) - 1  # number of columns

    for column in range(n_features):  # for each feature
        values = unique_colvalues(dataset, column)  # unique values in the column

        for val in values:  # for each value

            question = Question(column, val)

            # try splitting the dataset
            true_dataset, false_dataset = partic(dataset, question)

            # Skip this split if it doesn't divide the
            # dataset.
            if len(true_dataset) == 0 or len(false_dataset) == 0:
                continue

            # Calculate the information gain from this split
            gain = info_gain(true_dataset, false_dataset, current_uncertainty)

            if gain >= best_gain:
                best_gain, best_question = gain, question
    return best_gain, best_question


class Leaf:
    """
    A leaf node classifies data. It creates a dictionary of the form:
        class -> number of times it appears in the dataset form
                 the training data that reach this leaf.

    """

    # Constructor with dataset parameter.

    def __init__(self, dataset):
        self.predictions = count_colvalues(dataset)


class Decision_Node:
    """
    A Decision Node asks a question. It creates a reference to the question and to the
    two child nodes
    """

    # Constructor with parameters: question, true_branch, false_branch.

    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch


"""
This function constructs the decision tree of a given dataset based on the CART algorithm.
It has control over the maximum depth allowed for the tree; by default it has no value so
it grows the whole tree, but it can be changed to any positive integer to determine the
depth to stop building. To keep track of the depth it uses a level parameter with initial
value 0 that isn't supposed to be changed by the user, but it's necessary when making the
recursion calls. Since the algorithm is recursive, we'll get a Question node or an instance
of a Decision_Node after each recursive call until the base case is reached, and when this
happens, we'll get a Leaf.

Inputs:
    dataset: is the preprocessed training data set (list of listed rows).
    max_depth: maximum depth allowed to build the tree.
    level: it's a control parameter to keep track of the depth for each recursive call.

Outputs:
    Decision_Node(question, true_branch, false_branch): Return a Question node. This
    records the best feature / value to ask at this point, as well as the branches to
    follow depending on the answer.
    Leaf(dataset): Base case, i.e., no further info gain. Since we can ask no further
    questions, we'll return a leaf.
"""


def build_tree(dataset, max_depth=None, level=0):
    """
    Try partitioing the dataset on each of the unique attribute, calculate the
    information gain, and return the question that produces the highest gain.
    """
    gain, question = find_best_split(dataset)

    """
    Base case: no further info gain or maximum depth has been reached. Since we
    can ask no further questions, we'll return a leaf.
    """
    if gain == 0 or level == max_depth:
        return Leaf(dataset)

    """
    If we reach here, we have found a useful feature / value to partition on.
    """
    true_dataset, false_dataset = partic(dataset, question)

    # Recursively build the true branch. Add 1 to the recursion level on each call.
    true_branch = build_tree(true_dataset, max_depth, level=level + 1)

    # Recursively build the false branch. Add 1 to the recursion level on each call.
    false_branch = build_tree(false_dataset, max_depth, level=level + 1)

    return Decision_Node(question, true_branch, false_branch)


"""
This function is used to print the tree previously built. It's implemented recursively
and prints the tree by printing it node by node.

Input:
    node: Decision_Node instance, a.k.a "the built Tree".
    spacing: spacing for printing. "" as default.
"""


def print_tree(node, spacing=""):
    """World's most elegant tree printing function."""

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        print(spacing + "Predict", node.predictions)
        return

    # Print the question at this node
    print(spacing + str(node.question))

    # Call this function recursively on the true branch
    print(spacing + '--> True:')
    print_tree(node.true_branch, spacing + "  ")

    # Call this function recursively on the false branch
    print(spacing + '--> False:')
    print_tree(node.false_branch, spacing + "  ")


"""
This function takes a row of the data set and the instance of Decision_Node resulted when
building the tree. It decides whether to follow the true-branch or the false-branch, compares
the feature and value stored in the node (Tree) to the example (row) we're considereing. The
base case is reached when we've reached a leaf, in that case we return the attribute predictions
of the Leaf instance. This function is usually used within a for cycle that goes through the
testing dataset.

Inputs:
    row: row of the preprocessed testing data set (list of listed rows).
    node: Decision_Node instance, a.k.a "the built Tree".
Output:
    node.predictions: prediction of the input node, which is the dictionary obtained by
    the count_colvalues function applied to the leaf when reaching the base case, i.e, a
    dictionary of the predicted number of 1's and 0's (counts dictionary).
"""


def classify(row, node):

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        return node.predictions

    # It decides whether to follow the true-branch or the false-branch and compares
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)


"""
This function takes the output of the classify function (counts dictionary) and constructs
a dictionary with the proportion (probability) instead of counts.

Input:
    counts: counts dictionary obtained by the classify function.

Output:
    probs: probability dictionary obtained by showing proportion instead.
"""


def print_leaf(counts):
    """A nicer way to print the predictions at a leaf."""
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs
