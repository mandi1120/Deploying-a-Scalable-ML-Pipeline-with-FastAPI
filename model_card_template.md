# Model Card  

## Model Details  
This model was created by Amanda Hanway for the Udacity   
Machine Learning DevOps course. It utilizes the scikit-learn   
RandomForestClassifier model with default hyperparameters.  

## Intended Use  
This model is intended for use in predicting the salary range   
of an individual based on their census data attributes.  

## Data  
The data file "census.csv" was provided in the course. The file   
contains 32,561 rows of data collected in the census and is   
comprised of the following 15 columns:  
- age
- workclass
- fnlgt
- education
- education-num
- marital-status
- occupation
- relationship
- race
- sex
- capital-gain
- capital-loss
- hours-per-week
- native-country
- salary

## Training Data   
80% of the dataset was used for training the model.   

## Evaluation Data   
20% of the dataset was reserved for testing and evaluating    
the trained model.    

## Metrics  
The model was evaluated using Precision, Recall, and F1 scores.  
The results were as follows:  
- Precision: 0.7440  
- Recall: 0.6365  
- F1: 0.6861  

## Ethical Considerations
Given that the census.csv file includes only a 32.5K sample of the  
population, the model's predictions should not be taken as absolute   
for the entire population. Additional work is needed to identify   
potential bias in the dataset and to ensure all included features    
accurately reflect the larger population.  

## Caveats and Recommendations
A caveat for this project is that the year of the data collection  
was unknown. It is recommended to attain data from recent years  
to re-train and test the model in order to better predict modern  
salary ranges. As mentioned in the Ethical Considerations section  
it is recommended that the data be reviewed in depth, and any       
features found to be biased are removed from the training data for  
the model to be re-trained.  






