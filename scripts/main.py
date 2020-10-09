from module.extractor import DataExtractor



DE = DataExtractor()

DE.load_timeseries_us(r'D:\covid\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_US.csv')
DE.calculate_daily_county_confirmed()
#DE.output_county_confirmed()
DE.output_province_confirmed(["Florida", "Arizona", "California", "Minnesota", "Texas"], 
                             [10, 30, 60],
                             [(50/255, 168/255, 82/255),
                              (23/255, 192/255, 230/255),
                              (230/255, 88/255, 23/255)])
