from module.extractor import DataExtractor



DE = DataExtractor(r'D:\covid\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_US.csv')

DE.load_timeseries_us()
DE.calculate_daily_county_confirmed()
DE.output_daily_county_confirmed()