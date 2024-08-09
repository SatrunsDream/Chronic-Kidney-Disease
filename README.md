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
2.    The categorical columns were examined for inconsistencies in their values. For example, columns like 'diabetes_mellitus', 'coronary_artery_disease', and 'class' contained variations such as extra spaces or tab characters that could lead to incorrect interpretations.
3.    The 'class' column, which originally contained categorical labels ('ckd' and 'not ckd' for kidney desease), was mapped to numeric values (0 and 1). This step is important for machine learning models that require numerical input rather than categorical labels.
5.    We observed missing values in several columns, To address these missing values, we first need to understand the missing mechanism behind them. This will involve determining if the missing values are missing completely at random (MCAR), missing at random (MAR), or missing not at random (MNAR). Once we understand the missing mechanism, we can use imputation techniques such as mean imputation, mode imputation, or more advanced methods like multiple imputation or predictive imputation to replace the missing values. We will explain these steps in more depth later in our analysis.

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

#### Observations

1. Age Looks a Bit Left Skewed, Observation: The age distribution is left-skewed, meaning that there are fewer younger individuals compared to older individuals.
2. Blood Glucose Random is Right Skewed: Blood glucose levels are right-skewed, indicating that most individuals have lower glucose levels, with a few having significantly higher levels.
3. Blood Urea is Also a Bit Right Skewed: Blood urea levels exhibit right skewness, similar to blood glucose, where most values are on the lower end, and higher values are less frequent.
4. Rest of the Features Are Lightly Skewed: Other features show light skewness, indicating that their distributions are relatively close to normal.

  <iframe
  src="assets/features_distribution2_plot.html"
  width="700"
  height="1200"
  frameborder="0"
></iframe>

#### Correlations

The correlations you've identified can provide insights into the relationships between various biological factors and their potential implications for chronic kidney disease (CKD). 

  <iframe
  src="assets/features_heat_map.html"
  width="800"
  height="800"
  frameborder="0"
></iframe>

<span style="color: green;">**Positive Correlations:**</span>

* *Specific Gravity → Red Blood Cell Count, Packed Cell Volume, and Hemoglobin:*

Significance: Specific gravity is a measure of the concentration of solutes in the urine. Higher specific gravity may indicate dehydration, which can lead to an increase in red blood cell count, packed cell volume, and hemoglobin as the body attempts to conserve water by concentrating the urine.
Biological Implication: These correlations could suggest that as kidney function deteriorates, the body's ability to concentrate urine changes, which might be linked to alterations in blood parameters.

* *Sugar → Blood Glucose Random:*

Significance: This is an expected positive correlation, as blood glucose levels directly reflect the amount of sugar in the blood. High blood sugar levels are a key indicator of diabetes, which is a major risk factor for CKD.
Biological Implication: Elevated blood glucose levels can damage the kidneys over time, contributing to the development or worsening of CKD.

* *Blood Urea → Serum Creatinine:*

Significance: Both blood urea and serum creatinine are waste products filtered by the kidneys. An increase in these levels typically indicates impaired kidney function.
Biological Implication: High levels of these markers are often used to diagnose CKD, as they signify a reduction in the kidneys' ability to filter waste from the blood.

* *Hemoglobin → Red Blood Cell Count ← Packed Cell Volume:*

Significance: Hemoglobin is a protein in red blood cells that carries oxygen. Packed cell volume (or hematocrit) is the proportion of blood that consists of red blood cells. These positive correlations indicate that as red blood cell count increases, so do hemoglobin levels and packed cell volume.
Biological Implication: These parameters are critical for assessing anemia, which is common in CKD patients due to reduced erythropoietin production by the kidneys.

<span style="color: purple;">**Negative Correlations:**</span>

* *Albumin, Blood Urea → Red Blood Cell Count, Packed Cell Volume, Hemoglobin:*

Significance: Albumin is a protein that can leak into the urine when kidneys are damaged (albuminuria). Blood urea levels, as mentioned earlier, rise when kidney function is impaired. A negative correlation with red blood cell count, packed cell volume, and hemoglobin could indicate that as kidney function worsens, anemia becomes more severe.
Biological Implication: The development of anemia in CKD patients is multifactorial, involving reduced erythropoietin production, blood loss, and nutritional deficiencies, all of which can be exacerbated by kidney damage.

* *Serum Creatinine → Sodium:*

Significance: A negative correlation between serum creatinine and sodium may indicate that as kidney function deteriorates (with rising creatinine levels), the kidneys' ability to maintain sodium balance is compromised.
Biological Implication: This imbalance can lead to conditions like hyponatremia (low sodium levels), which can have serious consequences, including confusion, seizures, and even coma.

