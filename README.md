**Exploratory Data Analysis of Customer Loans**

Purpose of the project:
Gain an understanding of the data in the loan payments table. An insight into this data is useful so decisions regarding future loan approvals can be made and risks can be effectively managed.

Steps in carrying out this project and key things I learnt during each step:

1. Extracting data from the RDS data base:
   - Needed to create a RDS Database Connector Class which was meant to take in valaues from a dictionary contained in a YAML file to connect to the database to extract the data.
   - At the start of the project I could not get this to work and instead manually input the credentials into the connector to extract the data.
   - Managed to fix the connector class so it would use the dictionary from the YAML file to connect instead which meant I could keep the credentials confidential as intended.
2. Converting columns:
   - Learnt more about the different pandas datatypes and how to convert from one type to another.
3. Getting information about the dataframe:
   - Improved my OOP knowledge.
   - Improved my knowledge of data exploration of pandas data frames.
4. Imputing data:
   - Learnt more about creating methods for visualising data.
   - Used the distribution of the columns to decide how to impute the missing data or if rows/columns can be deleted.
   - In future projects I should try and use more sophisticated imputation methods such as regression imputation or KNN
5. Transforming skewed columns:
   -  Learnt a lot about data visualisation such as using qq plots and histograms to correct skew and compare before and after transformation.
   -  I need to improve my understanding of how to use the transformed columns during data analysis. 
6. Removing outliers
7. Removing overly correlated columns:
   - Using a mixture of visual and quantative analysis to see which columns were overly correlated.
   - Intially struggled to create comprehensible correlation matrix but after tweaking the parameters I managed to generate one.
8. Analysis and visualisation:
   - This is arguably the most import part of the project. Doing this part of the project I learnt even more about using different methods to visualise and quantatively analyse the data.
   - Learnt how to create various graphs using different python modules.
   - Improved my ability to manipulate dataframes to gain insights to specific subsets of the data.
   - Learnt how to create various functions which incorporated built in pandas functions to gain insights into the data and perform more in depth analysis.
   - One thing I want to improve future projects is familiarising myself with the data before analysis for example I intially coded a method to calculate the monthly payment amount but this was already part of the data frame as the 'instalment' column.
   - Improving my understanding of the raw data for future projects will increase the validity of future data analysis.


 

