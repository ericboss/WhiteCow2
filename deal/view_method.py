from .config import *
import requests, json
import logging
import pandas as pd
import numpy as np

logger = logging.getLogger('django')


def property_search_query(url, query_params):

        # header
        headers = {
            "x-rapidapi-host": host,
            "x-rapidapi-key": api_key
        }
       
        # response

        response = requests.get(url, headers=headers, params=query_params)
        if response.ok:
            return response
        else:
            logger.error(f"Error in making API request ")
            return None
 
def process_query_response(response):
    if response is not None:  
        content = json.loads(response.content)
        df = pd.DataFrame.from_dict(content['data']['results'])
        return df 
    else:
        return None


def get_estimate_value(property_id):
    try:
        url = url_estimate
        querystring = {"property_id":property_id}
        headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': host
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.content)
        return data
    except:
        return None


def calculate_deal(list_property_id, df):
    deal_dict = {}
    for_cast = None
    for list_ in list_property_id:
        data = get_estimate_value(list_)
        try:
            for_cast= data['data']['forecast_values'][0]['estimates'][-1]['estimate']
        except:
            for_cast= 0
        df2 =df[df["property_id"] == list_]["list_price"]
        initial=df2.to_list()[0]
        percentage_change = ((for_cast - initial)/initial) *100
        deal_dict[list_] = percentage_change
    return deal_dict

def get_deal_datafrane(deal_dict, df):
    sort_deal = sorted(deal_dict.items(), key=lambda x: x[1], reverse=True)
    property_id_deal = [k[0] for k in sort_deal][:3]
    df_deal = df[df['property_id'].isin(property_id_deal) ]
    return df_deal


























def filter_sold_data(params, period):
        """
        Filter dataframe to return values for the last x months.

        Gets the current data, and computes the months difference date bwtween current and what values entered as argument(by), then filters the data to return the desired dataframe

        Parameters
        ----------


        Returns
        -------
        [dataframe] Filtered Dataframe

        """
        df = get_sold_data(params=params)
        # Grap the last_update column
        if df is not None:
            logger.debug(
                f"Filtering the dataframe to return data for the last {period} months")

            df["last_update"] = pd.to_datetime(df["last_update"], utc=True)

            # Get the current time"
            now = pd.to_datetime("now", utc=True)
        # Compute the diffrence in month between current and dates in the last update column and create a new column
            df["monthDiff"] = abs(
                (now - df["last_update"]) / np.timedelta64(1, 'M'))

            # Filters he dataframe based on monthDiff column
            if period != '':

                df_new = df[df["monthDiff"] <= period]
            else:
                df_new = df
        else:
            logger.error("No dataframe to filter")
            df_new = None
        return df_new


def average_price_sold(params, period):
        """
        Computes Average Sold price
        """

        df_hist = filter_sold_data(params=params, period=period)
        if df_hist is not None:
            avp = df_hist['price'].mean()
        else:
            avp = None

        return avp


def convert_add_price_for_rent( data):
        """
        Process the data to add a column price. This is for rent returned data
        """
        data['community'] = data['community'].astype('str')
        data['community'] = data.community.apply(eval)
        price = []
        for i in range(data['community'].size):
            price.append(data['community'][i]['price_max'])

        data['price'] = pd.DataFrame(price)
        return data


def get_data_for_rent(params):
        """
        Make ApI call to get for rent data. The response json data is processed 
        to return dataframe
        """
        data = property_search_query(url=url_for_rent,query_params=params)
        data_json = response_json(data)

        data = process_json_response(data_json)
        if data is not None:
            data = convert_add_price_for_rent(data)
            return data
        else:
            return None

def get_data_for_sale(params):
        """
        Make ApI call to get for sale data. The response json data is processed 
        to return dataframe
        """
        data = property_search_query(url=url_for_sale,query_params=params)
        data_json = response_json(data)

        data = process_json_response(data_json)
        if data is None:
            logger.debug("No for sale data returned")
            return None
        return data


def percentage_average_market_data(property_status, params, period, compare,percentage):

        """
        Filters dataframe to return a new data frame based on below/above/equals average market price of sold properties
        Parameters
        ----------

        Returns
        -------
        [dataframe] Filtered Dataframe
        """
        if period != '':
            period = int(period)
        if property_status == 'For Rent':
            data = get_data_for_rent(params=params)
        else:
            data = get_data_for_sale(params=params)

        # Computes the percentage value of the avp
        average_price = average_price_sold(params=params, period=period)
        print("average price is ", average_price)
        compare_value = compare
        percentage = int(percentage)

        p_value = average_price - ((percentage/100) * average_price)
        # Filters data based on p_value
        if compare_value == "below" and data is not None:

            df = data[data["price"] < p_value]
        elif compare_value == "above" and data is not None:
            df = data[data["price"] > p_value]
        elif compare_value == "equals" and data is not None:
            df = data[data["price"] == p_value]
        else:
            df=data
        
        return df


def formatting(property_status, params, period, compare,percentage):
        df = percentage_average_market_data(property_status=property_status, params=params, period=period, compare=compare, percentage=percentage) 
        df = df.where(df.notnull(), None)
        if df is None:
            return None 
        df["address"] = df["address"].apply(json.dumps) 
        df["address"] = df["address"].apply(json.loads)  
        #df["community"] = df["community"].apply(json.dumps) 
        
        if property_status == 'For Rent' : 
            df["community"] = df["community"].apply(json.dumps) 
            df["community"] = df["community"].apply(json.loads)

            df["photos"] = df["photos"].apply(json.dumps) 
        if property_status == 'For Sale':
            df["branding"] = df["branding"].apply(json.dumps) 
            df["branding"] = df["branding"].apply(json.loads)  

            df["office"] = df["office"].apply(json.dumps)
            df["office"] = df["office"].apply(json.loads)

            df["lot_size"] = df["lot_size"].apply(json.dumps)
            df["lot_size"] = df["lot_size"].apply(json.loads)

            df["building_size"] = df["building_size"].apply(json.dumps)
            df["building_size"] = df["building_size"].apply(json.loads)

            df["agents"] = df["agents"].apply(json.dumps)
            df["agents"] = df["agents"].apply(json.loads)

            df["office"] = df["office"].apply(json.dumps)
            df["office"] = df["office"].apply(json.loads)

            df["client_display_flags"] = df["client_display_flags"].apply(json.dumps)
            df["client_display_flags"] = df["client_display_flags"].apply(json.loads)

            df["lead_forms"] = df["lead_forms"].apply(json.dumps)
            df["lead_forms"] = df["lead_forms"].apply(json.loads)

            df["lot_size"] = df["lot_size"].apply(json.dumps)
            df["lot_size"] = df["lot_size"].apply(json.loads)

            df["mls"] = df["mls"].apply(json.dumps)
            df["mls"] = df["mls"].apply(json.loads)



        return df
