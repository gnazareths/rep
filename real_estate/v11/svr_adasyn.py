import pandas as pd
import numpy as np

from sklearn.svm import SVR

np.random.seed(42)

train_df = pd.read_csv("~/real_estate/data/v11/train_df_adasyn.csv")
test_df = pd.read_csv("~/real_estate/data/v11/test_df.csv")

features = train_df.columns[:-1]

X_train = train_df[features]
X_test = test_df[features]
y_train = train_df["target"]
y_test = test_df["target"]

svr = SVR()
svr.fit(X_train, y_train)

# Predict
yhat_train = svr.predict(X_train)
yhat_test = svr.predict(X_test)

df1 = pd.DataFrame({"label":y_train, "pred":yhat_train, "train":[1]*len(y_train)})
df2 = pd.DataFrame({"label":y_test, "pred":yhat_test, "train":[0]*len(y_test)})
df = pd.concat([df1,df2], axis=0)

df.to_csv("~/real_estate/data/v11/svr_adasyn_predictions.csv",index=False)