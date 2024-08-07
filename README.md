<style>
    body {
        text-align: center;
    }
</style>
# Predicting Chronic Kidney Disease
By: Sardor Sobirov

# Introduction
In this project, we focus on developing a prediction model for chronic kidney disease (CKD) using a dataset obtained from the UCI Machine Learning Repository. The dataset can be accessed at this link. This dataset is designed to aid in predicting the occurrence of CKD and was collected from hospital records over a period of approximately two months.

## Dataset Characteristics
Type: Multivariate
Subject Area: Other
Associated Tasks: Classification
Feature Type: Real
Number of Instances: 400
Number of Features: 24
The dataset encompasses a variety of attributes related to patient health, allowing for the development of robust models to predict the presence of chronic kidney disease. This will involve exploring and preprocessing the data, selecting appropriate features, and applying classification algorithms to achieve accurate predictions.

| id | age | bp  | sg    | al | su | rbc   | pc      | pcc       | ba        | bgr   | bu   | sc  | sod | pot | hemo | pcv | wc   | rc  | htn | dm  | cad | appet | pe  | ane | classification |
|----|-----|-----|-------|----|----|-------|---------|-----------|-----------|-------|------|-----|-----|-----|------|-----|------|-----|-----|-----|-----|-------|-----|-----|----------------|
| 0  | 48  | 80  | 1.020 | 1  | 0  | NaN   | normal  | notpresent| notpresent| 121   | 36   | 1.2 | NaN | NaN | 15.4 | 44  | 7800 | 5.2 | yes | yes | no  | good  | no  | no  | ckd            |
| 1  | 7   | 50  | 1.020 | 4  | 0  | NaN   | normal  | notpresent| notpresent| NaN   | 18   | 0.8 | NaN | NaN | 11.3 | 38  | 6000 | NaN | no  | no  | no  | good  | no  | no  | ckd            |
| 2  | 62  | 80  | 1.010 | 2  | 3  | normal| normal  | notpresent| notpresent| 423   | 53   | 1.8 | NaN | NaN | 9.6  | 31  | 7500 | NaN | no  | yes | no  | poor  | no  | yes | ckd            |
| 3  | 48  | 70  | 1.005 | 4  | 0  | normal| abnormal| present   | notpresent| 117   | 56   | 3.8 | 111 | 2.5 | 11.2 | 32  | 6700 | 3.9 | yes | no  | no  | poor  | yes | yes | ckd            |
| 4  | 51  | 80  | 1.010 | 2  | 0  | normal| normal  | notpresent| notpresent| 106   | 26   | 1.4 | NaN | NaN | 11.6 | 35  | 7300 | 4.6 | no  | no  | no  | good  | no  | no  | ckd            |

## Key Steps

### Comprehensive EDA Process:

Gain a thorough understanding of the EDA process using a machine learning dataset.
Extract valuable insights from the dataset through mathematical analysis and visualization.

### Data Visualization:

Utilize visualization techniques to gain a better understanding of the data.
Identify patterns and trends that are crucial for making accurate predictions.

### Feature Engineering:

Explore different approaches to feature engineering.
Enhance the dataset by creating new features that can improve model performance.

# Data Cleaning and Exploration
The first step is to clean the data to ensure it is suitable for effective analysis. Data cleaning is crucial because it helps remove inconsistencies, errors, and inaccuracies that can skew results and lead to incorrect conclusions.

## Cleaning

1.    First step in our data cleaning process was to replace ambiguous column names with more descriptive ones. Clear and descriptive column names make the dataset easier to understand and work with.
2.    We observed missing values in several columns, To address these missing values, we first need to understand the missing mechanism behind them. This will involve determining if the missing values are missing completely at random (MCAR), missing at random (MAR), or missing not at random (MNAR). Once we understand the missing mechanism, we can use imputation techniques such as mean imputation, mode imputation, or more advanced methods like multiple imputation or predictive imputation to replace the missing values. We will explain these steps in more depth later in our analysis.

## Exploring Data
In this step, we perform both univariate and bivariate analyses to understand the distribution and relationships of our data, as well as examine interesting aggregates

### Univariate Analysis

We examined the distributions of individual columns by using DataFrame operations and creating relevant plots. 

  <iframe
  src="assets/features_distribution_plot.html"
  width="700"
  height="1200"
  frameborder="0"
></iframe>

