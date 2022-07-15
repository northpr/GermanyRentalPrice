# Due to the development of the work please check the Colab link below instead.

## Click Google Colab badge below:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1biEgivJEOUVS8KbeTXyb1lNgsVtbitYj)

# Project Overview: Rental Price in Germany Prediction, Entire Data Science Process
- Create virtualization to have a better understanding of the data of the rental cost in Germany.
Engineered features from the original variable to create a better model and understanding of the factor that impacts the rental price cost in Germany.
- Using LGBM (Similar to XGBoost but faster!) for creating the model by which has an accuracy of more than 80% from basic factors and can boost up to more than 95%, but I used only basic parameters for the users who does not sound familiar with rental in Germany.

**Warning** I have deleted some files such as dataset, ipynb and model file because it is over the limit of Github. You can get my notebook files (.ipynb) and model (.pickle) in the links below.
https://www.kaggle.com/northpatawee/germany-rental-clean-eda-lgbm-99-acc

## Purpose from this project

I've traveled from SEA and I don't know how much an apartment in Berlin should cost and it's tough to find an apartment at a reasonable price while I'm staying in Germany for my Master Degree. Furthermore, I need something for my Data Science Portfolio for the job application after graduation. So why not build something from scratch with the dataset on the Kaggle.

So this kernel will be well written than my previous kernel for other people and use what I've learned in my master course and other online resources to produce something that will be practical for the real environment.

## What we expected from this kernel.
Data cleaning to clear the outliers and remove columns that don't correlate highly to the prediction.
- Create virtualization to have a better understanding of the data of the rental in Germany.
- Feature engineering from the original variable to create a better model.
- Create a tool that estimates the house cost predicted by many variables.

## Code and Resources Used
**Requirement**: Python, Flask, Basic web interface for deploying model.
**Program**: Jupyter notebook for Data Science process, Visual Studio Code for HTML, CSS, JavaScript to build an interface for users.
**Packages**: np, pandas, plotly, matplotlib, lightgbm, flask, json and more.

# Data Clearning

## Missing Values
After scraping the data, I needed to clean it up to be usable for the model. I made many changes to make the data have a better understanding.
- Removes rows that don't contain Rental Price.
- Adding new columns: Price Per Square Meter, Additional Cost.
- Eliminate outliers.
- Fill in missing numerical values by using categorical as the reference. I could know what could be the best reference by using Correlation Matrix(Heatmap) to find the best correlation to the dataset
- Fill in categorical missing value by using mode and other factors.


## Feature Engineering
- Create 'Price Per Square Meter' by using Rental and Living Space
- Create 'Addition Cost' or cost of electricity, heating, water and other miscellaneous.
```Python
df['Pricepm2'] = df['baseRent'] / df['livingSpace']
df['additioncost'] = df['totalRent'] - df['baseRent']
df = df[(df['serviceCharge'] < 1000)]
```

**Some example after removing outleirs**
![01totalbase](link)
```Python
fig = px.scatter(df, x='totalRent', y='baseRent')
fig.show()
```

![02totalservice](link)
```Python
fig = px.scatter(df, x='totalRent', y='serviceCharge')
fig.show()
```

# EDA
To understand the model that we want to create the prediction model. We should analyze for better understanding and might clean to have a better dataset. I cannot illustrate all of the data in this overview. Instead, I will show some of the virtualizations from the notebook files.

## Data Virtualization
Normally, I love to start from the distribution for the basic understanding. Distribution Plot of 'totalRent.'
![03distribution](link)



Heatmap to check the correlation between variables
![04correlationmap](link)


Data ratio of the city that in this dataset.
![05cityratio](link)

Average rental per month and group by condition.
![06rentalsqm](link)
```Python
f, ax = plt.subplots(figsize=(12, 12))
sns.heatmap(df.corr().sort_values(by='totalRent',ascending=False), square = True,fmt='.2f' ,annot = True)
```

Average rental per month and group by city.
![07rentalsqm](link)

We could do more virtualization to understand more in a specific city or room type depending on what purpose you're trying to use this work in, such as focusing in only Berlin.

# Machine Learning
I would transform and scale categorical variables and numerical variables to make it fit to the model for the best result of the data.


## Light Gradient Boost
I've found this model is like Xgboost, and it's run much faster, so now I'm trying as much as I can to use this library to improve my skills.
**For anyone who is interest in documentation:** https://lightgbm.readthedocs.io/en/latest/Python-Intro.html
```Python
d_train = lgb.Dataset(x_train, label=y_train) # Load the dataset and test

# parameters for this model
params = {
 'n_estimators': 10000,
 'objective': 'regression',
 'metric': 'rmse',
 'boosting_type': 'gbdt',
 'max_depth': -1,
 'learning_rate': 0.01,
 'subsample': 0.72,
 'subsample_freq': 4,
 'feature_fraction': 0.4,
 'lambda_l1': 1,
 'lambda_l2': 1,
 'seed': 46,
 }

clf = lgb.train(params, d_train, 100)
```

## Model performance.
We could use other type of machine learning such as linear regression or random forest to calculate and might suitable than LGBM but I want to train myself more in this technique.
- LGBM: RMSE ~ 130-140
Which has a very good precision rate of around 80%, and we could increase the model's accuracy by inputting more factors in the models, but I choose not to because it would be difficult for newcomers to find all of the information.

# Productionization
In the last step, I build a flask API and use other web applications (CSS,HTML,JS) that I've little knowledge about to build. So it might not work perfectly but I could show you and explain the basic concept of the work.

This is the basic function of the web when you input all the variables and select all type of apartments, heating etc. and click estimate price.
![03distribution](link)

It will use the LGB model we've trained before to generate the estimated price we have to pay per month. If we've a better dataset, we might do it more precisely.
![03distribution](link)

# Summary
We could do a lot more such as specified in one city such as Berlin, or create other variables for the users to input. This work could develop more such as improving the interface or others, and I will try to put this work into AWS for the others to use this model for their reference in apartment finding in the future.

This is all of this project. If you love it, you can star or if you're looking for collaboration. I'm always open to that.
