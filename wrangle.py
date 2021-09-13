import env
import os
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LinearRegression

from acquire import get_zillow_data, clean_zillow_data
import prepare

def wrangle_zillow(target):
    '''
    This function will get our data ready for modeling all within this one function by combining my functions
    from acquire, and prep.
    '''
    # acquire our data
    df = get_zillow_data()
    # clean the data
    df = clean_zillow_data(df)
    # remove outliers
    df = prepare.remove_outliers(df)
    # split the data
    train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test = prepare.train_validate_test(df,target)
    # scale the data
    scaler, X_train_scaled, X_validate_scaled, X_test_scaled = prepare.standard_scaler(X_train,X_validate,X_test)
    return train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test, scaler, X_train_scaled, X_validate_scaled, X_test_scaled