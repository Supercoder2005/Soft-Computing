# loading the dataset 
from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target 
#print(x)
#print(y)

# Splitting the dataset into training and testing set
from sklearn.model_selection import train_test_split 
x_train,x_test,y_train,y_test = train_test_split(x, y)

# Training of the model 
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(x_train,y_train)

# Testing the model 
y_pred = model.predict(x_test)
print(y_pred)

# Evaluation of the model 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report 
print("Accuracy Score : ",accuracy_score(y_test, y_pred))
print("Confusion Matrix : \n",confusion_matrix(y_test, y_pred))
print("Classification Report : \n",classification_report(y_test, y_pred))

# Displaying the Decision Tree 
from sklearn.tree import plot_tree 
plot_tree(model)