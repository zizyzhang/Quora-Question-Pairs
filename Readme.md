# Readme

## XGBoost

1. Install Required Libraries

   ```
   pip install pandas
   pip install numpy
   pip install scikit-learn
   pip install nltk
   pip install tqdm
   pip install pyemd
   pip install fuzzywuzzy
   pip install python-levenshtein
   pip install --upgrade gensim
   pip install xgboost
   ```

2. Download Required files

   ```
   mkdir data
   mkdir predictions
   cd data
   sudo python -m nltk.downloader stopwords
   download https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz and put the file in the data directory
   download train and test data from https://www.kaggle.com/c/quora-question-pairs/data
   ```

   ```
   -featurePreExtraction.py
   -predictions
   -data
   	-train.csv
   	-test.csv
   	-xgbBasic.py
   	-GoogleNews-vectors-negative300.bin
   ```

3. Run

   ``` 
   cd data
   cd ..
   python feature_engineering.py
   cd data
   python xgbBasic.py
   ```

4. Output

   ```
   model: data/XGB_leaky_add_feature_first.mdl
   prediction: predictions/XGB_leaky_add_feature_first.csv
   ```

# LSTM

## Prerequisites

- Download the pre-trained word vectors, namely glove.840B.300d, from <https://nlp.stanford.edu/projects/glove/> and put it into the project directory.

- Download the train and test data from <https://www.kaggle.com/c/quora-question-pairs/data>. 

- Install all the packages: 

  ```
  pip install pandas
  pip install numpy
  pip install scikit-learn
  pip install nltk
  pip install distance
  pip install fuzzywuzzy
  pip install networkx
  pip install keras
  ```

## Getting Started

- Create an account of Google Colab, and install the necessary libraries and perform authorization.
- Run nlp_feature_extraction.py and non_nlp_feature extraction.py to extract features, which are stored in the nlp_features_train.csv and non_nlp_features_train.csv.
- Run model.py, it will create 10 different predictions on the test set.
- Run postprocess.py to rebalance the prediction of test set.

## Software Requirement

- Python 3.6
- Google Colab



For more information about this project, please visit "https://github.com/zizyzhang/Quora-Question-Pairs/"