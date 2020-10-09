from module.extractor import DataExtractor



DE = DataExtractor()
DE.load_timeseries_us(r'D:\covid\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_US.csv')

# Must execute this line in order to get basic info.
DE.calculate_daily_county_confirmed()

# Output daily confirmed csv(not necessary)
#DE.output_county_confirmed()

# Output visualized data, can output multiple province at once
# and you can set the scale of MA and its color
DE.output_province_confirmed(
                             provinces=["Florida", "Arizona", "California", "Minnesota", "Texas"], 
                             MAs=[10, 30, 60],
                             MAcolor=[(50/255, 168/255, 82/255),
                              (23/255, 192/255, 230/255),
                              (230/255, 88/255, 23/255)],
                             output_folder=r'D:\covid\daily_province_confirmed_chart')
