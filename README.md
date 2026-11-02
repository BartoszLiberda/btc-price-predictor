# Bitcoin Price Predictor (Data Science Portfolio)

Predicting financial market movements is one of the most challenging and data-dense problems in computational finance. This project aims to bridge traditional quantitative technical analysis with Natural Language Processing (NLP).

The core objective is to design, train, and deploy an end-to-end data pipeline that ingests historical market data and real-time textual sentiment data to predict short-term Bitcoin (BTC/USD) price direction using machine learning.

## Tech Stack
- **Language:** Python 3.10+
- **Data Manipulation:** `pandas`, `numpy`
- **Machine Learning:** `scikit-learn` (PCA, Scalers, Logistic Regression), `xgboost`
- **Financial Data:** `yfinance`

## Setup & Installation

### 1. Clone this repository
```bash
git clone https://github.com/BartoszLiberda/btc-price-predictor.git
```

### 2. Navigate to the project directory
```bash
cd btc-price-predictor
```

### 3. Create a virtual enviroment and install required packages
```bash
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```