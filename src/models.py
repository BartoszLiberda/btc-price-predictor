from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

def train_logistic_baseline(X_train, y_train):
    # Trains the baseline Logistic Regression model
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    return model

def train_xgboost(X_train, y_train):
    # Trains the primary XGBoost classifer
    model = XGBClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
    model.fit(X_train, y_train)
    return model