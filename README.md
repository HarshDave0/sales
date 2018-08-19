# sales
### Data Description  
Total number of companies=896  
### Initial Dataset (creation):  
A web scrapper for scrapping LinkedIn pages was implemented using selenium and beautifulsoup (linkedIn_company.py)    
The scrapper was able to collect data = 202 companies ([snippet of the scrapped data](https://github.com/Pahulpreet86/sales/blob/master/example.png))      

#### 1) Size Category (target variable)
The data scraped included number of employees in the organisation (defined in range example: 51-200 employees) and number of employees available on LinkedIn .The upper limit of the range or number of employees available on LinkedIn was used as a deciding factor to assign size category.                                      
There are two choice for segregation and labelling.([refrence](http://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Enterprise_size))                          

##### Two Categorical variable:                        
1) SME (small and medium-sized enterprises): < 250 employees           
2) LE (large enterprise): >= 250 employees           
##### Four Categorical variable:           
1) Micro enterprises : <10            
2) Small enterprises: 10 -  49           
3) Medium-sized enterprises: 50 - 249          
4) Large enterprises: >= 250               

For selecting the best segregation method, Silhouette analysis was done for the above two labelling choice. 
Silhouette coefficients near +1 indicate that the sample is far away from the neighbouring clusters. A value of 0 indicates that the sample is on or very close to the decision boundary between two neighbouring clusters and negative values indicate that those samples might have been assigned to the wrong cluster.                  
1) Two Category Score:  0.57                   
2) Four Category Score:  0.55                    
Therefore, two category classification was chosen as the method for segregation and labelling for the size.      

###### Note:
Since there was large variation in the size range, log scaling was done before Silhouette analysis.     

#### 2) Country Category
The dataset included countries (company location) which were mapped according to income level. ([reference](http://www.un.org/en/development/desa/policy/wesp/wesp_current/2014wesp_country_classification.pdf))    
The income level were as follow: High Income , Upper Middle Income , Lower Income

#### 3) Category
The dataset included company category which were as follow: H - hotel, CH - the chain of hotels, TB - tourism board, TO - tourism organisation, TA - travel agency, WP - wedding planner, EP - event planner, R - resort, CB -convention bureau, CC - congress centre)

#### 4) Rank 
Since the dataset is related to the tourism industry, the ranking of the countries on the basis international tourism also plays an important role. Therefore, ranking of countries was taken and valued in such a way that the top-ranked country is assigned the highest value and so on in the dataset.([refrence](https://www.indexmundi.com/facts/indicators/ST.INT.ARVL/rankings))


### Modelling: 
[Modelling](https://github.com/Pahulpreet86/sales/blob/master/Modelling.ipynb)   
For modelling the Category,Country Category and Rank attribute were used, with the size category as the target variable. All the categorical variable were label encoded before model fitting.The train and test size selected was 70:30 (70% for training and 30% for testing phase).
Autoslearn was used to select the best ensemble model for the dataset. The model was then saved as [automl.dump.pkl](https://github.com/Pahulpreet86/sales/blob/master/automl.dump.pkl)

### Prediction: 
[Prediction](https://github.com/Pahulpreet86/sales/blob/master/Prediction.ipynb)   
The saved model was then used for predicting = 496 companies size category label (untrained data).   
The remaining 197 companies for which prediction couldn't be made include 186 companies with partial data (either the country or the category was missing) and remaining 11 instances consist of those categories or countries for which model was not trained.
