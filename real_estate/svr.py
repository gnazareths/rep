import sys

import pandas as pd
import numpy as np

from sklearn.svm import SVR
from sklearn.externals import joblib

np.random.seed(42)

train_filename = "~/real_estate/data/train_df_smote.csv"
test_filename = "~/real_estate/data/supervised_dfs/test_df_pca.csv"
output_filename = "~/real_estate/data/supervised_dfs/svr_smote.pkl"

def svr(train_df, test_df, output_filename):
    
    train_df = pd.read_csv(train_df)
    test_df = pd.read_csv(test_df)
    
    features = train_df.columns[:-1]
    X_train = train_df[features]
    X_test = test_df[features]
    y_train = train_df["target"]
    y_test = test_df["target"]
    
    svr = SVR()
    svr.fit(X_train, y_train)
    joblib.dump(svr, output_filename)
    
    return

svr(train_filename, test_filename, output_filename)