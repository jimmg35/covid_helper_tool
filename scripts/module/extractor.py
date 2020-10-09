import pandas as pd 
import numpy as np
import os
from os import listdir

import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.dates import MonthLocator, DateFormatter
import matplotlib.ticker as mticker

class DataExtractor():
    def __init__(self):
        self.province_to_county = {}
        self.county_confirmed = []
        self.unique_province = []
        self.province = []
        self.county = []
        self.timeseries = []
    
    def load_timeseries_us(self, data_path):
        
        '''
            Load .csv and require some basic info
            such as county, province...etc.
        '''
        
        # Load csv
        data = pd.read_csv(data_path)
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

    def output_county_confirmed(self):
        
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
                
    def output_province_confirmed(self, provinces, MAs, MAcolor, output_folder):
        
        '''
            ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California',
             'Colorado', 'Connecticut', 'Delaware', 'Diamond Princess', 'District of Columbia',
             'Florida', 'Georgia', 'Grand Princess', 'Guam', 'Hawaii', 'Idaho', 'Illinois',
             'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
             'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
             'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
             'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio',
             'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island',
             'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
             'Virgin Islands', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin','Wyoming']
        '''
        
        for province in provinces: 
            
            confirmed_timeseries = []
            total_province_confirmed = 0
            # Get specific province and transpose
            interval_county_confirmed = []
            interval_county_confirmed = self.get_province_data(province)
            a = np.array(interval_county_confirmed)
            
            # Calculate daily confirmed
            for i in range(0, len(self.timeseries)):
                total_confirmed_per_d = 0
                for j in a.T.tolist()[i]:
                    total_confirmed_per_d += j
                confirmed_timeseries.append(total_confirmed_per_d)
                
            # Plot the daily confirmed
            d_color = (101/255, 107/255, 255/255, 0.9)
            fig, ax = plt.subplots(figsize=(16, 8))
            ax.plot(self.timeseries, confirmed_timeseries, label="daily confirmed", color=(190/255, 190/255, 190/255))
            
            # Calculate MA
            for m in range(0, len(MAs)):
                ma_list = []
                for i in range(MAs[m], len(self.timeseries)):
                    d = 0
                    for j in range(1, MAs[m]+1):
                        for k in a.T.tolist()[i-j]:
                            d += k
                    ma_list.append(int(d / MAs[m]))
                ax.plot(ma_list, label="{}MA".format(MAs[m]), color=MAcolor[m])
                
            plt.xticks(np.arange(10, len(self.timeseries), 31.0), rotation=40)
            plt.title("Daily confirmed trend of {}".format(province))
            plt.legend()
            plt.savefig(os.path.join(output_folder, province+"_confirmed.png"))   
            
    def get_province_data(self, province):          
        interval_county_confirmed = []
        for i in range(0, len(self.province)):
            if self.province[i] == province:
                interval_county_confirmed.append(self.county_confirmed[i])
        return interval_county_confirmed
                    
                    
                
        
        
    
        
        
    