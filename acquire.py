import os
import pandas as pd
import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def create_zillow_data():
    '''
    puts zillow data into a csv
    '''
    query = '''
SELECT *
FROM properties_2017
JOIN predictions_2017 using(parcelid)
WHERE transactiondate between "2017-05-01" and "2017-08-31" and propertylandusetypeid in (260,261,263,265,266,275)
    '''
    df = pd.read_sql(sql_query, get_connection("zillow"))
return df

def get_zillow_data():
    '''
    gets our zillow csv and reads it into a pandas dataframe
    '''
    if os.path.isfile("zillow.csv"):
        df = pd.read_csv("zillow.csv",index_col = 0)
    else:
        df = create_zillow_data()
        df.to_csv("zillow.csv")
    return df


def clean_zillow_data(df):
    '''
    this function takes in an unclean zillow df and does the following:
    - keeps only columns we need for the project
    - renames columns
    - drops nulls
    '''
    #selecting the features
    features = ['calculatedfinishedsquarefeet', 'bathroomcnt', 'bedroomcnt', 'taxvaluedollarcnt','yearbuilt','taxamount','fips']
    df = df[features]

    #rename columns
    df = df.rename(columns={
                            'calculatedfinishedsquarefeet': 'sqft',
                            'bathroomcnt': 'bathroomss',
                            'bedroomcnt': 'bedrooms',
                            'taxvaluedollarcnt':'tax_value',
                            'yearbuilt':'year_built',
                            'taxamount': 'tax_amount'
        
    })
    #drop nulls
    df = df.dropna()
    
    return df