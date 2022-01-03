# Flask_IA_mnist

This is a small exercise to create a webapp with Flask, setup a DB connection and give access to an AI digit classification service (model trained with the. Keras'
MNIST digits dataset - https://keras.io/api/datasets/mnist/ -).

### To use the DB services:

Create a .env file at the project root directory and add
DB_USR=your_user
DB_PWD=you_password

(Don't forget to recheck the .gitignore file to add this .env file).

### To use the AI classification service:

Run the file train_digits.py. This will create a file called trained_digits.sav in folder /static.
This process can take several minutes, since it will download the dataset, train and export the trained model (~1,2GB).
When the .sav is created, you are ready to go!

#### Tested with

Python 3.9.7
(Check also the dependencies within the .py scripts)
