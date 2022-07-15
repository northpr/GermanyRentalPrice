# 🇩🇪 Germany Rental Analysis, Prediction and Modelling.

## 🧐 Project Overview 
- Create virtualization to have a better understanding of the data of the rental cost in Germany.
Engineered features from the original variable to create a better model and understanding of the factor that impacts the rental price cost in Germany.
- Comparison between multiple models such as Ridge Regression and Light Gradient Boost (Similar to XGBoost but faster🔥) for creating the model by which has an accuracy of more than 80% from basic factors and can boost up to more than 95%.

**❗️ Warning** I have deleted some files because it is over the limit of Github. You can get my notebook files (.ipynb) and model (.pickle). You could check my Colab links for further information.

## 🤰🏼 What we expected from this kernel.
- Data cleaning to clear the outliers and remove columns by using statistics method.
- Create virtualization to have a better understanding of the data trend of the rental in Germany.
- Feature engineering from the original variable to create a improve model performance.
- Create a tool that estimates the house cost predicted by using only basic variables.

## 👨‍💻 Code and Resources Used
**Requirement**: Python, Flask, Basic web interface for deploying model.
**Program**: Jupyter notebook for Data Science process, Google Colab, Visual Studio Code for HTML, CSS, JavaScript to build an interface for users.
**Packages**: np, pandas, plotly, matplotlib, lightgbm, flask, json and more.

## 📕 Contents:
You could check all of the notebook work by using Colab link below.
- Part 1: Cleaning and Visualization
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1biEgivJEOUVS8KbeTXyb1lNgsVtbitYj)
- Part 2: Using PyCaret for Model Hyperparameters Tuning
  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lXJhdH3rGnKQ_LjBGMh8ZK-Lf2VcfLW5)
- Part 3: Create Model
  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/14XIC90Lss_izdw-PE1cgIe4eECsXrHbY)

# 🧼 Data Clearning

## Missing Values
After scraping the data, I needed to clean it up to be usable for the model. I made many changes to make the data have a better understanding.
- Removes rows that don't correlate to the Rental Price.
- Adding new columns: Price Per Square Meter, Additional Cost.
- Eliminate outliers by using statistic method such as empirical rule.
- Fill in missing numerical values by using categorical as the reference. I could know what could be the best reference by using Correlation Matrix(Heatmap) to find the best correlation to the dataset
- Fill in categorical missing value by using mode and other factors.


## Feature Engineering
- Create 'Price Per Square Meter' by using Rental and Living Space
- Create 'Addition Cost' or cost of electricity, heating, water and other miscellaneous.

Example:
```Python
# Create new variables such as  `Price Per Square Meter`
df['Pricepm2'] = df['baseRent'] / df['livingSpace']
df['additioncost'] = df['totalRent'] - df['baseRent']

# Remove outliers from service charge cost more than 1,000 euro
df = df[(df['serviceCharge'] < 1000)]
```
```Python
# Empirical Rule
for cols in df.columns:
    if df[cols].dtype == 'int64' or df[cols].dtype == 'float64':
        upper_range = df[cols].mean() + 3 * df[cols].std()
        lower_range = df[cols].mean() - 3 * df[cols].std()
        
        indexs = df[(df[cols] > upper_range) | (df[cols] < lower_range)].index
        df = df.drop(indexs)
```

# 📷 EDA
To understand the model that we want to create the prediction model. We should analyze for better understanding and might clean to have a better dataset. I cannot illustrate all of the data in this overview. Instead, I will show some of the virtualizations from the notebook files.

## Data Virtualization
Normally, I love to start from the distribution for the basic understanding. Distribution Plot of 'totalRent.'
![03distribution](https://github.com/northpr/GermanyRentalPrice/blob/main/model/data/markdown_image/distribution.png)



Heatmap to check the correlation between variables
![04correlationmap](https://github.com/northpr/GermanyRentalPrice/blob/main/model/data/markdown_image/correlation.png)


Average rental per month by using city to seperate
![05cityratio](https://github.com/northpr/GermanyRentalPrice/blob/main/model/data/markdown_image/average_rental_per_month.gif)

Average rental per month by using Postleitzahl to seperate.
![06rentalsqm](https://github.com/northpr/GermanyRentalPrice/blob/main/model/data/markdown_image/germany_map.png)

![07rentalsqm](https://github.com/northpr/GermanyRentalPrice/blob/main/model/data/markdown_image/germany_average_map.gif)

We could do more virtualization to understand more in a specific city or room type depending on what purpose you're trying to use this work in, such as focusing in only Berlin.

# 🤖 Machine Learning
I would transform and scale categorical variables and numerical variables to make it fit to the model for the best result of the data.

## Ridge Regression
One of my favorite model when I've to create any machine learning model. It reduces the parameter estimates in an effort to reduce variance, improve prediction accuracy, and simplify interpretation.
```Python
# Hyperparameters for 'Ridge Regression'
from sklearn.linear_model import Ridge
ridge = Ridge(alpha=2.81, copy_X=True, fit_intercept=False, max_iter=None,
      normalize=True, random_state=123, solver='auto', tol=0.001)

# Fit the data
ridge.fit(x_train,y_train)
```
## Light Gradient Boost
I've found this model is like Xgboost, and it's run much faster, so now I'm trying as much as I can to use this library to improve my skills.

**For anyone who is interest in documentation:** https://lightgbm.readthedocs.io/en/latest/Python-Intro.html
```Python
d_train = lgb.Dataset(x_train, label=y_train) # Load the dataset and test

# Hyperparameters for this model
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
We could use other type of machine learning such as linear regression or random forest to calculate and might suitable than my but I want to train myself more in this technique.
- LGBM: RMSE ~ 130-140
Which has a very good precision rate of around 80%, and we could increase the model's accuracy by inputting more factors in the models, but I choose not to because it would be difficult for newcomers to find all of the information.

# 🎇 Productionization
In the last step, I build a flask API and use other web applications (CSS,HTML,JS) that I've little knowledge about to build. So it might not work perfectly but I could show you and explain the basic concept of the work.

This is the basic function of the web when you input all the variables and select all type of apartments, heating etc. and click estimate price. 
It will use the Ridge Regression model we've trained before to generate the estimated price we have to pay per month. If we've a better dataset, we might do it more precisely.
![07page](https://github.com/northpr/GermanyRentalPrice/blob/main/model/data/markdown_image/prediction.png)


# Summary
We could do a lot more such as specified in one city such as Berlin, or create other variables for the users to input. This work could develop more such as improving the interface or others, and I will try to put this work into AWS for the others to use this model for their reference in apartment finding in the future.

This is all of this project. If you love it, you can star or if you're looking for collaboration. I'm always open to that.
