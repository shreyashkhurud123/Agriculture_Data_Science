import pandas as pd
import numpy as np
import os

input_folder = '.\\Input\\' 

output_folder = '.\\Output\\'

if not os.path.isdir(output_folder):
    os.makedirs(output_folder)


def format_1(df):
    #df = agri_data
    
    table = df.iloc[ : , :14]
    
    table = table.dropna()
    
    table = table[table['Area Code (M49)'] == 840 ] 
    
    #table = table[table['Item'].str.strip() == 'Maize (corn)'] 
    
    table = table.drop(columns = 'Element Code')
    table = table.drop(columns = 'Area Code (M49)')
    table = table.drop(columns = 'Item Code (CPC)')
    table = table.drop(columns = 'Unit')
    table = table.drop(columns = 'Year Code')
    table = table.drop(columns = 'Domain Code')
    
    
    table_area_harvested = table[table['Element'] == 'Area harvested'] 
    table_area_harvested = table_area_harvested.drop(columns = 'Element')
    table_area_harvested.rename(columns = {'Value' : 'Area harvested'} , inplace= True)
    
    
    table_Yield = table[table['Element'] == 'Yield'] 
    table_Yield = table_Yield.drop(columns = 'Element')
    table_Yield.rename(columns = {'Value' : 'Yield'} , inplace= True)
    
    
    
    table_Production = table[table['Element'] == 'Production'] 
    table_Production = table_Production.drop(columns = 'Element')
    table_Production.rename(columns = {'Value' : 'Production'} , inplace= True)
    
    
    
    
    
    
    tb = pd.merge( table_area_harvested,table_Yield , how='inner')
    
    tb = pd.merge( tb,table_Production , how='inner')

    
    
    return tb
    
    




if __name__ == '__main__':
    
    file_name = 'USA Crop Data.csv'  # Replace with the actual file name
    file_path = input_folder + file_name

    agri_data = pd.read_csv(file_path)

    cleaned_agri_data = format_1(agri_data)
    
   
    
    cleaned_agri_data.to_csv(os.path.join(output_folder, 'Cleaned_USA_Crop_Data.csv'), index=False)