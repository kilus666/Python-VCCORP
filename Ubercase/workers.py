import pandas as pd

def read_csv_to_datetime(file):
    monthly_data= pd.read_csv(file,delimiter=",",header=0)
    monthly_data["Date/Time"]=pd.to_datetime(monthly_data["Date/Time"])
    return monthly_data

