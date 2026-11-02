# Project Log - Data Science Portfolio

### Week 1 (Oct 12 – Oct 18)
- Setup the enviroment
- Wrote a script using `yfinance` to get daily historical OHLCV data for Bitcoin (BTC-USD)
- Looked over the data to check for missing values and see the overall structure

### Week 2 (Oct 19 – Oct 25)
- Data prep and figuring out features
- Added technical indicators like daily returns, 20-day and 50-day moving averages and a rolling volatility metric
- Setup up the target variable as a simple binary outcome (1 if the price goes up the nect day & 0 if it drops)
- Tested out Z-score normalization to scale everything properly and rand Principal Component Analysis (PCA) to shrink down redundant features.

### Week 3 (Oct 26 – Nov 2)
- Built the actual models
- Used a sequential 80/20 train-split instead of a random one to avoid accidentally leaking future data into the training set
- Trained a basic Logistic Regression model as a baseline, and then got the XGBoost classifer to work
- Checked the acuracy scores and classificatio reports, organized into the modular `src/` directory structure, and finished the notebook and documents for the draft submission