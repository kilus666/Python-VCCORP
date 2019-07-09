import os
import fnmatch
import pandas as pd
from multiprocessing import Pool



Dataset_location= "C:/Users/Admin/Desktop/Dataset/uber-pickups-in-new-york-city"
def get_file_location(folder_location):
    file_list= []
    for filename in os.listdir(folder_location):
        if fnmatch.fnmatch(filename, 'uber-raw-data-*14.csv'):
            full_path= os.path.join(folder_location,filename)
            file_list.append(full_path)
    return(file_list)



def read_csv_to_datetime(file):
    monthly_data= pd.read_csv(file,delimiter=",",header=0)
    monthly_data["Date/Time"]=pd.to_datetime(monthly_data["Date/Time"])
    return monthly_data

if __name__=="__main__":
    print("Starting")
    list_of_files= get_file_location(Dataset_location)
    pool= Pool(processes=6)
    list_monthly_data= pool.map(read_csv_to_datetime,list_of_files)
    print(list_monthly_data[0])
    print("Ending")

# list_of_files= get_file_location(Dataset_location)
# df= merge_csv(list_of_files)
# print(df.head(10))
# print(df.tail(10))
# print(df.head(10))
        
# pd.read_csv()
