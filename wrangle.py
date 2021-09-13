from acquire import get_zillow_data, clean_zillow_data
from prepare import remove_outliers,train_validate_test,standard_scaler

def wrangle_zillow(target):
    '''
    This function will get our data ready for modeling all within this one function by combining my functions
    from acquire, and prep.
    '''
    # acquire our data
    df = get_zillow_data()
    # clean the data
    clean_zillow_data(df)
    # remove outliers
    df = remove_outliers(df)
    # split the data
    train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test = train_validate_test(df,target)
    # scale the data
    scaler, X_train_scaled, X_validate_scaled, X_test_scaled = standard_scaler(X_train,X_validate,X_test)
    return train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test, scaler, X_train_scaled, X_validate_scaled, X_test_scaled