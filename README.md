# sales
### Data Description  
Total number of companies=896  
### Initial Dataset (creation):  
A web scrapper for scrapping LinkedIn pages was implemented using selenium and beautifulsoup (linkedIn_company.py)    
The scrapper was able to collect data = 202 companies ([snippet of the scrapped data](https://github.com/Pahulpreet86/sales/blob/master/example.png))    
The data scraped included number of employees in the organisation, defined in range example: 51-200 employees.The upper limit of the range was used as a deciding factor to assign size category label.
1) SME (small and medium-sized enterprises): < 250 employees 
2) LE (large enterprise): >= 250 employees  

### Modelling: 
[Modelling](https://github.com/Pahulpreet86/sales/blob/master/Modelling.ipynb)   
For modelling the Category and Country attribute were used, with the size category label as the target variable. All the categorical variable were label encoded before model fitting.The train and test size selected was 70:30 (70% for training and 30% for testing phase).
Autoslearn was used to select the best ensemble model for the dataset. The model was then saved as [automl.dump.pkl](https://github.com/Pahulpreet86/sales/blob/master/automl.dump.pkl)
#### Note:   
Since, the model is dependent on the scrapped data, therefore the model is applicable only for the countries and categories mentioned in the label encoder instance.(this short-coming will be resolved as soon as more data becomes available for training)

### Prediction: 
[Prediction](https://github.com/Pahulpreet86/sales/blob/master/Prediction.ipynb)   
The saved model was then used for predicting = 496 companies size category label (untrained data).   
The remaining 197 companies for which prediction couldn't be made include 186 companies with partial data (either the country or the category was missing) and remaining 11 instances consist of those categories or countries for which model was not trained.
