# Zillow Regression Project

### Executive Summary
I was able to create a regression model that beat out the baseline for predicting homes in the california area. It preformed with an R^2 value of 0.3859 and an RMSE on out of sample data of 294674.89

##### Top Predictors:
- Square Footage
- Number of bathrooms
- Number of bedrooms
##### Model Information:
- Type: Linear regression
- Alpha = 1
- RMSE: 294683.58
- R^2: 0.3859
##### Background Info:
- Single unit properties
- Data gathered between May-Aug 2017
- Counties: Los Angeles, Orange, Ventura
##### Our main predictors for house prices
- 1) Square footage
- 2) Number of bathrooms
- 3) Number of bedrooms

##### Linear Regression Model vs Baseline
- The RMSE was 294674.89763495134
- The baseline RMSE was 378143.31047048484
- RMSE difference of 83468

## Project Description
- I will be running zillow data through the data science pipeline. I am trying to build a model that will predict house prices, using a linear regression model. I will be preparing the data and making decisions on what data will be applicable to my model and finding leading drivers for home pricing. I will also create a csv returning the county, and state for each residence in the given data.

## Project Goals
- Break down and analyze the zillow, giving documentation and explination through that process.
- Construct a model to predict home prices using regression modeling.
- Deliver a 5 minute presentation on my findings in slides.

## Buisness Goals
- Deliver a model that will beat out the baseline model for predicting house prices.
- Highlight some of the key indicators of home pricing.

## Audience
- Zillow data science team.

## Project Deliverables
- Deliver .py files that can be used to replicate the model, and recreate the project.
- Run statistical modeling (Atleast 2) and deliver visualizations on the data.
- Present a slide show, summarizing the finding on drivers of single unit property values, visualizing main points, and giving incite into the modeling used.
- Return the county, state and tax rate for the homes found in the data.

## Project Context
- Im using the zillow dataset from the codeup sql database, I am using the 2017 dataset, and filtering for the ("hot") months for selling between "2017-05-01" and "2017-08-31", and I am also selection for single-unit properties.
- This dataset originally contained 62 columns and 38619 rows after all tables were joined together.
- after cleaning the dataset we are left with 7 columns and 37928

## Data Dictionary
|Target|Datatype|Definition|
|:-------|:--------|:----------|
|tax_value|dtype('Float64')|Gives the home value after tax|

|Feature|Datatype|Definition|
|:-------|:--------|:----------|
|sqft|dtype('Float64')|The total square footage of the house|
|bathrooms|dtype('Float64')|The number of bathrooms|
|bedrooms|dtype('Float64')|The number of bedrooms|
|year_built|dtype('Float64')|The year the house was built|
|tax_amount|dtype('Float64')|The amount that was paid in tax|
|fips|dtype('Float64')|Indentifies geographic areas|
|lot_size_sqft|dtype('Float64')|Gives total square footage of the lot|

## Hypotheses
### Alpha
- ?? = .05

- 1) The higher the square footage, the higher the price.
- 2) The older a house, the price will lower.
- 3) The more bedrooms a house has, the higher the price.
- 4) The more bathrooms a house has, the higher the price.
- 5) The location will have an affect on the price.
- 6) The size of the lot will affect the price.

## Data Science Pipeline
#### Planning
- Make a README.md that will hold all of the project details including a data dictionary, key finding, initial hypotheses, and explain how my process can be replicated
- Create a MVP, originally and work through the iterative process of making improvements to that MVP.
- Make hypotheses that are tested though statistical analysis.
- Create visualizations throughout the process both in the explore stage and visualizing my findings after modeling.
#### Acquire
- Create an acquire.py that will take the data from sql and put it into a pandas dataframe. I saved the zillow data to a .csv for easier access
#### Prepare
- Create a prepare.py that will clean and remove outliers from the data.
- While cleaning the data I removed any outliers that fell far outside of the expected for square footage, bathrooms, bedrooms, and tax value.
#### Explore
- Awnser my initial hypotheses that was asked in my planning phase, and test those hypotheses using statistical tests, either accepting or rejecting the null hypothesis.
- Continue using statistical testing and visualizations to discover variable relationships in the data, and attempt to understand "how the data works".
- Summarize my conclusions giving clear awnsers to the questions I posed in the planning stage and summarize any takeaways that might be useful.
#### Modeling and Evaluation
- Train and evaluate  models comparing those models to the baseline on different evaluation metrics, but focusing on root mean squared error.
- Validate the models and choose the best model that was found in the validation phase.
- Test the best model found and summarize the performance and document the results, and visualize those results.
#### Delivery
- Deliver a presentation to the Zillow datascience team.
- Summarize my findings, and build a narrative around the data, pulling from my knowledge on story telling.
- End with key takeaways and reccomendations, giving an explination of what I would do with more time given.

## Modules

#### acquire.py
- Acquires the data from the CodeUp SQL database and puts the table into a pandas dataframe
#### prepare.py
- Cleans my data and gets it ready for use in modeling and explore.
#### explore.py
- Contains functions that I used to help visualize the data.

## Project Reproduction
- Random state or seed = **174**, and is used in my models and my split functions.
- In replication making use of the user defined function, in cunjunction with my documented process, and presaved models should give a good guide.The functions that will make the process faster.
- Create and use your own env file that connects you to the sql database.
- Run the zillow_final jupyter notebook with all the .py files.

## Conclusion

### Key takeaways
- Square footage seems to have the largest relationship on prices, followed by bathrooms, bedrooms.
- The year built has a relationship with the data although it was small.
- All three counties have similar tax rates, but LA has the highest.
### Model takeaways
- Type: Lasso lars model
- My alpha was set to 1
- R^2: 0.386
- RMSE: 294683.58
### Moving forward
- I will continue to master regression modeling and attempt to make better models that can beat out my model set as the new baseline.
##### If given more time
- I would continue exploring other factors that might play a role in house pricing.
- I would create a more efficent model using my current model as the baseline.
- I would create new columns of data attempting to find bivariate relationships within the data.
