import Preprocessing as p
import Decision_Tree as d

# Preprocess data
train, col_names = p.preprocess_data(
    "0_train_balanced_15000.csv", sep=";", keep_default_na=False)

test, _ = p.preprocess_data(
    "0_test_balanced_5000.csv", sep=";", keep_default_na=False)

# Convert data to list
ltrain = p.convert_to_list(train.iloc[0:150, :])
ltest = p.convert_to_list(test.iloc[0:50, :])

print(d.count_colvalues(ltrain))
T = d.build_tree(ltrain, max_depth=2)
print("-----------------------------Tree-----------------------------")
d.print_tree(T)
print("--------------------------------------------------------------")

# Print actual values vs predictions
for row in ltest:
    print("Actual: %s. Predicted: %s" %
          (row[-1], d.classify(row, T)))


# Print to text file "test.txt"
#sys.stdout = open("test.txt", "w")

#---------------- code

# #sys.stdout.close()
