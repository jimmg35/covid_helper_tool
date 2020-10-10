from module.extractor import DataExtractor



provinces = ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California',
             'Colorado', 'Connecticut', 'Delaware', 'Diamond Princess', 'District of Columbia',
             'Florida', 'Georgia', 'Grand Princess', 'Guam', 'Hawaii', 'Idaho', 'Illinois',
             'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
             'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
             'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
             'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio',
             'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island',
             'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
             'Virgin Islands', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin','Wyoming']


DE = DataExtractor()
DE.load_timeseries_us(r'D:\covid\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_US.csv')


# Must execute this line in order to get basic info.
DE.calculate_daily_county_confirmed()


# Output daily confirmed csv(not necessary)
#DE.output_county_confirmed()


# Output visualized data, can output multiple province at once
# and you can set the scale of MA and its color
# DE.province_confirmed(
#                    provinces=provinces, 
#                    MAs=[10, 30, 60],
#                    MAcolor=[(50/255, 168/255, 82/255),
#                    (23/255, 192/255, 230/255),
#                    (230/255, 88/255, 23/255)],
#                    output_folder=r'D:\covid\daily_province_confirmed_chart')


DE.province_bollinger(provinces, 
                      20, 
                      r'D:\covid\bollinger_confirmed_chart')

