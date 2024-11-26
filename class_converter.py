import pandas as pd
payments_df = pd.read_csv("loan_payments.csv")

class DataTransform():
    def __init__(self, dataframe, *args):
       # args used to convert  different numbers of columns at once each time. 
        self.dataframe = dataframe
        self.columns_to_convert = args
        
    # convert dates into datetime objects 
    def date_converter(self):
        
        for column in self.columns_to_convert:
            self.dataframe[column] = pd.to_datetime(self.dataframe[column], errors='coerce')  
   

    # convert objects such as 36 months or 10 years into integers, 36, 10 so analysis can be performed 
    def num_converter(self):
        for column in self.columns_to_convert:
            self.dataframe[column] = self.dataframe[column].str.replace('month','')
            self.dataframe[column] = self.dataframe[column].str.replace('year','')
            self.dataframe[column] = self.dataframe[column].str.replace('s','')
            self.dataframe[column] = self.dataframe[column].str.replace('+','')
            self.dataframe[column] = self.dataframe[column].str.replace('<','')
            self.dataframe[column] = self.dataframe[column].str.replace('>','')
            self.dataframe[column] = pd.to_numeric(self.dataframe[column], errors='coerce')