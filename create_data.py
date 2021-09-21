# Import modules
import requests
import json
from pytrends.request import TrendReq
from pytrends.exceptions import ResponseError
import pandas as pd
from datetime import date
from datetime import timedelta


# Global variables

# Parameters for pytrends payload
# Create lists of search terms
search_terms_1 = ['covid', 'corona virus', 'covid19', 'delta variant', 'vaccine']
search_terms_2 = ['covid variant', 'corona virus variant', 'corona variant']
list_of_term_lists = [search_terms_1, search_terms_2]
COUNTRY = 'US'

# Addresses for CDC and HealthData.gov data
hospitals_addy = 'https://healthdata.gov/resource/anag-cw7u.json'
covid_addy = 'https://data.cdc.gov/resource/n8mc-b4w4.json'
addy_list = []
addy_list.append(hospitals_addy)
addy_list.append(covid_addy)


def get_json_data(addy):
    return pd.read_json(addy)


def get_trends_data(terms_list, pytrend_obj, params_list):
    # Build payload one and load data
    pytrend_obj.build_payload(terms_list, timeframe=params_list[0], geo=params_list[1])
    # Load regional interest and interest over time data
    reg_int_terms_df = pytrend_obj.interest_by_region(inc_low_vol=True)
    iot_terms_df = pytrend_obj.interest_over_time()

    return reg_int_terms_df, iot_terms_df



def create_data():
    # Create Trend Request object
    pytrend = TrendReq()
    
    # Create parameters specific to creation of data
    date_interval_start = '2020-01-01'
    date_interval_end = str(date.today() - timedelta(days=1))   # Today's data probably isn't complete
    DATE_INTERVAL = date_interval_start + ' ' + date_interval_end
    params_list = [DATE_INTERVAL, COUNTRY]
    # Supposedly, Google returns 400 if search term (s?) is > 100 char's
    # I am not able to search more than 5 terms w/o the 400 error
    list_of_dfs = []
    for term_list in list_of_term_lists:
        list_of_dfs.extend(get_trends_data(term_list, pytrend, params_list))

    # Combine regional interest data from both builds
    reg_int_dfs = [list_of_dfs[0], list_of_dfs[2]]
    reg_int_df = pd.concat(reg_int_dfs, axis=1)

    # Combine interest over time from both builds
    # Change isPartial column names to reflect the respective search term list
    list_of_dfs[1].rename({'isPartial': 'isPartial1'}, axis=1, inplace=True)
    list_of_dfs[3].rename({'isPartial': 'isPartial2'}, axis=1, inplace=True)
    iot_dfs = [list_of_dfs[1], list_of_dfs[3]]
    iot_df = pd.concat(iot_dfs, axis=1)


    # TODO: Do I need to save snapshots of these data in order to create
    # a time series?? If so, how?
    # Load the hospital utilization and surveillance data
    # For loop through list of addresses from which json data is to be loaded
    list_of_dfs_from_json = []
    for addy in addy_list:
        list_of_dfs_from_json.append(get_json_data(addy))

    # Save data to pandas data frames
    hospitals_df = list_of_dfs_from_json[0]
    covid_df = list_of_dfs_from_json[1]

    # TODO: Convert index to datetime objects
    iot_df.index = pd.to_datetime(iot_df.index.date)
    #iot_df.index = pd.to_datetime(iot_df.index)
    #pd.to_datetime(hospitals_df, format="%Y/%m/%d")
    #pd.to_datetime(covid_df, format="%Y/%m/%d")

    # Save data as csv's
    reg_int_df.to_csv('assets/reg_interest.csv')
    iot_df.to_csv('assets/iot.csv')
    hospitals_df.to_csv('assets/hospitals.csv')
    covid_df.to_csv('assets/covid.csv')

    list_of_dfs_to_return = [reg_int_df, iot_df, hospitals_df, covid_df]

    # Return data frames
    return(list_of_dfs_to_return)