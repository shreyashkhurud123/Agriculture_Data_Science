import pandas as pd
import numpy as np
import os

input_folder = '.\\Input\\' 

output_folder = '.\\Output\\'

if not os.path.isdir(output_folder):
    os.makedirs(output_folder)


def format_3(data):
    table = data.iloc[7: , 1:]
    tb = table
    table = tb
    
    table = table.drop(table.columns[[1, 2,3]], axis=1)
    
    table = table.loc[[7, 10,11,14,17]]
    
    table = table.transpose()
    
    
    
    table.columns = table.iloc[0]
    table = table[1:]
    
    table.rename(columns={'Indicator': 'Year'}, inplace=True)
    
    return table
    
    

if __name__ == '__main__':
    
    for filename in os.listdir(input_folder):
            
        file_path = os.path.join(input_folder, filename)
        
        if filename.endswith('.csv'):
            df = pd.read_csv(file_path)
            
            cleaned_df = format_3(df)
            cleaned_df.to_csv(os.path.join(output_folder, filename), index=False)
            
        elif filename.endswith('.xlsx'):
            
            data = pd.read_excel(file_path, header=None)
            
            
            
            
            cleaned_df = format_3(data)
            
            
            cleaned_df.to_excel(os.path.join(output_folder, filename), index=False)
            
            
        
        
            
    