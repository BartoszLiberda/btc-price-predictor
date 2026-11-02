import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def engineer_features(df):
    # Calculates SMA, Bolatility and binary target variable
    df['Return'] = df['Close'].pct_change()
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['Volatility_20'] = df['Return'].rolling(window=20).std()

    df['Target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)
    df = df.dropna()

    features = ['Return', 'SMA_20', 'SMA_50', 'Volatility_20', 'Volume']
    return df[features], df['Target']

def transform_data(X_train, X_test):
    # Applies Z-score normalization and PCA
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    pca = PCA(n_components=3)
    X_train_pca = pca.fit_transform(X_train_scaled)
    X_test_pca = pca.fit_transform(X_test_scaled)

    return X_train_pca, X_test_pca, pca
    