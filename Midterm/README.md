# CS506 Midterm

## Starter Code Instructions

1. Download the `train.csv` and `test.csv` files from Kaggle into the `data/` folder
2. Run `test_setup.py` to make sure you can load the files and print the first few rows of `train.csv` and `test.csv` and view their shapes + some visualization
2. `feature_extraction.py` will help you to generate features as well as generate `X_test.csv` which is `test.csv` but with the features from `train.csv` and whatever other features you added.
3. Run `predict-constant.py` to predict the same score for all rows in the test set
5. Run `predict-knn.py` to predict the score using KNN

Good luck!


# Dataset
File descriptions:
* train.csv - 1,697,533 unique reviews from Amazon Movie Reviews, with their associated star ratings and metadata. It is not necessary to use all reviews, or metadata for training. Some reviews will be missing a value in the 'Score' column. That is because, these are the scores you want to predict.
* test.csv - Contains a table with 300,000 unique reviews. The format of the table has two columns; i) 'Id': contains an id that corresponds to a review in train.csv for which you predict a score ii) 'Score': the values for this column are missing since it will include the score predictions. You are required to predict the star ratings of these Id using the metadata in train.csv.
* sample.csv - a sample submission file. The 'Id' field is populated with values from test.csv. Kaggle will only evaluate submission files in this exact same format.

Data fields:
* ProductId - unique identifier for the product
* UserId - unique identifier for the user
* HelpfulnessNumerator - number of users who found the review helpful
* HelpfulnessDenominator - number of users who indicated whether they found the review helpful
* Score - rating between 1 and 5
* Time - timestamp for the review
* Summary - brief summary of the review
* Text - text of the review
* Id - a unique identifier associated with a review
Note: Some of the rows of the table may have some of these values missing.

Dataset Citation

J. McAuley and J. Leskovec. From amateurs to connoisseurs: modeling the evolution of user expertise through online reviews. WWW, 2013