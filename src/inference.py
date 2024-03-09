from joblib import dump, load
import pandas as pd
import numpy as np
# from .data_processor import log_txf, remap_emp_length

def get_prediction(**kwargs):
    clf = load('models/mdl.joblib')
    features = load('models/raw_features.joblib')
    pred_df = pd.DataFrame(kwargs, index=[0])
    # pred_df = log_txf(pred_df, ['annual_inc'])
    # pred_df['emp_len'] = pred_df['emp_length'].map(remap_emp_length)
    pred = clf.predict(pred_df[features])
    missing_cols = set(features) - set(pred_df.columns)
    if missing_cols:
        raise ValueError(f"Missing columns in input data: {missing_cols}")
    
    # Reorder or select columns in pred_df to match the training features order
    pred_df = pred_df[features]
    
    # Predict and return the result
    pred = clf.predict(pred_df)
    return pred[0]
