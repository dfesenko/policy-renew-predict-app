import pickle
import pandas as pd

from joblib import load


def load_model_and_train_cols():
    classifier = load('static/rf_classifier1.joblib')

    with open('static/train_cols.pkl', 'rb') as file:
        train_cols = pickle.load(file)

    return classifier, train_cols


def predict(file, clf, train_cols):
    df = pd.read_csv(file, sep=';')

    x_ohe_encoded = pd.get_dummies(df)

    # add missing columns that were present in training dataset but not presented here (due to OneHotEncoding)
    missing_cols = set(train_cols) - set(x_ohe_encoded.columns)

    for c in missing_cols:
        x_ohe_encoded[c] = 0

    x_ohe_encoded = x_ohe_encoded[train_cols]

    predictions = clf.predict(x_ohe_encoded)
    pred_probabilities = clf.predict_proba(x_ohe_encoded)[:, 1]
    policy_ids = df['POLICY_ID']

    results_dict = {'POLICY_ID': policy_ids,
                    'POLICY_IS_RENEWED': predictions,
                    'POLICY_IS_RENEWED_PROBABILITY': pred_probabilities}

    result_df = pd.DataFrame(results_dict,
                             columns=['POLICY_ID', 'POLICY_IS_RENEWED', 'POLICY_IS_RENEWED_PROBABILITY'])
    return result_df
