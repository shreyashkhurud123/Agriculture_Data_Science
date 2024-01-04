import pandas as pd
import numpy as np
import os

input_folder = '.\\Input\\' 

output_folder = '.\\Output\\'

if not os.path.isdir(output_folder):
    os.makedirs(output_folder)


def format_2(df):
    #df = agri_data
    cols = {'PS': 'Surface Pressure' ,'WS10M':'Wind Speed at 10 Meters' ,'MO': 'Month','DY':'Day' ,'PRECTOTCORR' : 'Precipitation Corrected' ,  'QV2M' : 'Specific Humidity at 2 Meters' , 'TS':'Earth Skin Temperature'  }
    
    table = df.rename(columns=cols)

    table = table[table['Surface Pressure'] != -999]
        
    table = table.dropna()
    
    return table
    
    

if __name__ == '__main__':
    
    file_name = 'USA Weather Data.csv'  
    file_path = input_folder + file_name
 
    weather_data = pd.read_csv(file_path, skiprows=13 ,delimiter=',')
    
    cleaned_weather_data = format_2(weather_data)
    
    cleaned_weather_data.to_csv(os.path.join(output_folder, 'Cleaned_USA_Weather_Data.csv'), index=False)
    
    