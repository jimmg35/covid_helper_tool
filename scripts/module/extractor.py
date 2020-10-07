import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import os
from os import listdir



class DataExtractor():
    def __init__(self, data_path):
        self.data_path = data_path
        self.province_to_county = {}
        self.county_confirmed = []
        self.unique_province = []
        self.province = []
        self.county = []
        self.timeseries = []
    
    def load_timeseries_us(self):
        
        '''
            Load .csv and require some basic info
            such as county, province...etc.
        '''
        
        # Load csv
        data = pd.read_csv(self.data_path)
        # Drop Unassigned and Out of Province
        unassigned_index_list = data[data['Admin2']=='Unassigned'].index
        outof_index_list = data[data['Admin2'].astype(str).str.contains("Out of")].index
        data.drop(unassigned_index_list , inplace=False)
        data.drop(outof_index_list , inplace=False)
        # Get all province and county
        self.province = list(data["Province_State"])
        self.county = list(data["Admin2"])
        # Get unique province
        for i in self.province:
            if i not in self.unique_province:
                self.unique_province.append(i)
        # Construct the mapping of province and county
        for i in self.unique_province:
            self.province_to_county[i] = []
        for i in range(0, len(self.county)):
            self.province_to_county[self.province[i]].append(self.county[i])
            self.county_confirmed.append([])
        # Get time label (it works!! sooooo weird!!!)
        self.timeseries = list(data.columns[11:])
        self.data = data

    def calculate_daily_county_confirmed(self):
        
        '''
            The main algorithm goes here,
            calculating daily confirmed cases based on aggregated cases
        '''
        
        # Insert first day confirmed data
        for i in range(0, len(self.county)):
            self.county_confirmed[i].append(self.data[self.timeseries[0]][i]) 

        # Calculate the daily confirmed cases
        for i in range(1, len(self.timeseries)):
            for j in range(0, len(self.county)):
                daily_confirmed = self.data[self.timeseries[i]][j] - self.data[self.timeseries[i-1]][j]
                self.county_confirmed[j].append(daily_confirmed)

    def output_daily_county_confirmed(self):
        
        d = {
            "Province":self.province,
            "County":self.county, 
        }
        
        a = np.array(self.county_confirmed)
        
        for i in range(0, len(self.timeseries)):
            d[self.timeseries[i]] = a.T.tolist()[i]
        
        self.processed_data = pd.DataFrame(data=d)
        self.processed_data.to_csv(r'output.csv')
        print("Output Complete!")
                
        
        
        
    
        
        
    