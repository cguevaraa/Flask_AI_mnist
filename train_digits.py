# Create and train a Random Forest ML model
# Reload this script if there is no 'trained_digits.sav' file
# within the project

import pickle
from keras.datasets import mnist
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load data
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Create X_train and X_test with flatten images
X_train = []
X_test = []
for i in range(train_images.shape[0]):
    X_train.append(train_images[i].flatten())
for i in range(test_images.shape[0]):
    X_test.append(test_images[i].flatten())

# Instantiate and train the model
rf = RandomForestClassifier(n_estimators=1000)
rf.fit(X_train, train_labels)

# Test the model
pred_labels = rf.predict(X_test)
print('********************************************')
print('*** THE TRAINED MODEL SHOW THESE RESULTS ***')
print('********************************************')
print(classification_report(pred_labels, test_labels))
print('********************************************')

# Serialize the model and save to disk
filename = 'finalized_model.sav'
pickle.dump(rf, open('trained_digits.sav', 'wb'))