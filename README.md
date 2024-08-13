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
In this step, both univariate and bivariate analyses to understand the distribution and relationships of our data, as well as examine interesting aggregates

### Univariate Analysis

Examine the distributions of individual columns by using DataFrame operations and creating relevant plots. 

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

The correlations can provide insights into the relationships between various biological factors and their potential implications for chronic kidney disease (CKD). 

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

### Bivariate Analysis

The violin plots below compare key biomarkers between CKD and non-CKD patients. These differences are crucial for understanding the extent of kidney dysfunction and are essential for the diagnosis and monitoring of chronic kidney disease.

  <iframe
  src="assets/bivariate_class.html"
  width="700"
  height="1200"
  frameborder="0"
></iframe>

**We can draw the following conclusion from the plots above**

* *Serum Creatinine:*

CKD: Mean = 4.41, Median = 2.25, Range = 0.5 to 76.0
Non-CKD: Mean = 0.87, Median = 0.9, Range = 0.4 to 1.2

Significance: Serum creatinine is a crucial indicator of kidney function, as creatinine is a waste product filtered by the kidneys. In CKD patients, the kidneys lose their ability to efficiently filter creatinine, leading to higher levels in the blood. The stark contrast between CKD and non-CKD groups underscores serum creatinine's role as a diagnostic tool for identifying kidney dysfunction. Monitoring serum creatinine levels over time can help assess the progression of CKD and the effectiveness of treatments aimed at preserving kidney function.

* *Hemoglobin:*

CKD: Mean = 10.65, Median = 10.9, Range = 3.1 to 16.1
Non-CKD: Mean = 15.19, Median = 15.0, Range = 13.0 to 17.8

Significance: Hemoglobin is a protein in red blood cells that carries oxygen throughout the body. Lower hemoglobin levels in CKD patients are often due to anemia, a common complication of CKD caused by reduced production of erythropoietin (a hormone produced by the kidneys). Anemia can lead to fatigue, weakness, and other health issues in CKD patients. Regular monitoring of hemoglobin levels is essential in managing CKD, as it helps in identifying the need for treatments like erythropoiesis-stimulating agents or iron supplements to combat anemia and improve the patient's quality of life.

* *Blood Urea:*

CKD: Mean = 72.39, Median = 53.0, Range = 1.5 to 391.0
Non-CKD: Mean = 32.80, Median = 33.0, Range = 10.0 to 50.0

Significance: Blood urea levels reflect the amount of urea nitrogen in the blood, a waste product formed from the breakdown of proteins. Elevated levels in CKD patients indicate impaired kidney function, as the kidneys are less able to remove urea from the bloodstream. The broad range of blood urea levels in CKD patients highlights the variability in disease severity and the degree of kidney impairment. Monitoring blood urea can help track disease progression, guide dietary recommendations, and inform the need for interventions like dialysis.

* *Albumin:*

CKD: Mean = 1.72, Median = 2.0, Range = 0.0 to 5.0
Non-CKD: Mean = 0.0, Median = 0.0, Range = 0.0 to 0.0

Significance: Albumin is a protein that is normally retained in the bloodstream by healthy kidneys. The presence of albumin in CKD patients (and its absence in non-CKD patients) indicates kidney damage, as albumin should not normally pass into the urine in significant amounts. Elevated albumin levels in the urine (albuminuria) are often one of the earliest signs of CKD and can be used to detect the disease in its early stages. Regular testing for albumin in the urine is essential for early detection, monitoring disease progression, and preventing complications through timely interventions.

* *Red Blood Cell Count:*

CKD: Mean = 3.95, Median = 3.9, Range = 2.1 to 8.0
Non-CKD: Mean = 5.38, Median = 5.3, Range = 4.4 to 6.5

Significance: Red blood cells are responsible for carrying oxygen from the lungs to the rest of the body. A lower red blood cell count in CKD patients is indicative of anemia, which is commonly caused by reduced production of erythropoietin by the kidneys. Anemia in CKD patients can lead to symptoms such as fatigue, dizziness, and shortness of breath, significantly impacting their quality of life. Monitoring red blood cell count is crucial for diagnosing anemia in CKD patients and guiding treatment options, such as erythropoiesis-stimulating agents or iron supplements, to improve oxygen delivery and overall patient well-being.

* *Packed Cell Volume (PCV):*

CKD: Mean = 32.94, Median = 33.0, Range = 9.0 to 52.0
Non-CKD: Mean = 46.34, Median = 46.0, Range = 40.0 to 54.0

Significance: Packed cell volume, or hematocrit, measures the proportion of blood volume occupied by red blood cells. A lower PCV in CKD patients reflects a reduced number of red blood cells, which is consistent with anemia. This reduction in PCV means that CKD patients have a lower capacity to carry oxygen throughout the body, leading to the various symptoms of anemia. Monitoring PCV is important in assessing the severity of anemia in CKD patients and determining the need for interventions that can improve red blood cell production and oxygen-carrying capacity, ultimately improving patient outcomes.

  <iframe
  src="assets/bivariate_class2.html"
  width="700"
  height="1200"
  frameborder="0"
></iframe>

### Correlation Patterns of Features

Using the finding above help identify the most relevant and informative features for the correlation analysis. Understanding correlations helps in feature selection and engineering for the next step. 

  <iframe
  src="assets/bivariate_class3.html"
  width="700"
  height="1000"
  frameborder="0"
></iframe>
**We can draw the following conclusion from the plots above**

<span style="color: green;">**Positive Correlations:**</span>

* *Haemoglobin vs Packed Cell Volume*

Correlation: 0.95 (Positive)

Variance: Both features show low variance, which suggests they are stable and consistently related in the dataset.

Line of Best Fit: The line of best fit would have a very steep upward slope, indicating a very strong positive relationship.

Significance: This high positive correlation indicates that haemoglobin and packed cell volume are closely related. They are likely capturing similar aspects of blood health. Feature engineering might involve combining these features into a single metric or index to simplify the model and potentially reduce multicollinearity.

* *packed cell volume and red blood cell count*

Correlation: 0.75 (Positive)

Variance: Both features exhibit low variance, which indicates stability in the dataset. Their low variance suggests they are reliable indicators of blood health.

Line of Best Fit: The line of best fit for these two features would likely show a strong upward slope, indicating that as one feature increases, the other tends to increase as well. This strong positive correlation suggests that they are closely related and might be capturing similar aspects of blood health.

Significance: The high positive correlation indicates redundancy between packed_cell_volume and red_blood_cell_count. Feature engineering could involve combining these features into a single metric (e.g., a ratio or index), which can simplify the model and potentially reduce multicollinearity. This composite feature could still provide robust information about blood health while improving model efficiency.

* *serum creatinine and blood urea*

Correlation: 0.55 (Positive)

Variance: Both features have moderate variance, indicating they provide different aspects of kidney function and are not overly redundant.

Line of Best Fit: The line of best fit would show a moderate upward slope. While not as strong as the previous correlation, the positive relationship is still evident.

Significance: The moderate positive correlation suggests that these features are related but not perfectly aligned. Combining serum_creatinine and blood_urea into a single feature, such as a ratio, can provide a comprehensive measure of kidney function. This can help in capturing the broader picture of renal health and improve model accuracy.

<span style="color: purple;">**Negative Correlations:**</span>

* *haemoglobin and red blood cell count*

Correlation: -0.60 (Negative)

Variance: High variance in these features indicates significant variability in blood health among individuals. This high variance is crucial as it shows that the features capture a broad spectrum of conditions.

Line of Best Fit: The line of best fit for these features would show a downward slope, indicating that as haemoglobin levels increase, red_blood_cell_count tends to decrease, and vice versa. This inverse relationship can reflect underlying health issues, such as different forms of anemia.

Significance: The negative correlation and high variance suggest that haemoglobin and red_blood_cell_count provide complementary information. Feature engineering could involve creating an index or score that integrates these two features to better capture anemia's complexity and improve model performance.

* *blood urea and specific gravity*

Correlation: -0.40 (Negative)

Variance: Both features exhibit distinct ranges and distributions, indicating they capture different dimensions of kidney function.

Line of Best Fit: The line of best fit would show a mild downward slope. This moderate negative correlation reflects that changes in blood_urea are somewhat inversely related to specific_gravity.

Significance: Combining these features into a single metric or ratio could enhance the understanding of kidney function by incorporating their inverse relationship. This composite feature may offer more nuanced insights into kidney health and improve predictive accuracy.

* *Haemoglobin vs Blood Urea*

Correlation: -0.57 (Negative)

Variance: High variance in both features indicates significant variability in blood health.

Line of Best Fit: The line of best fit would show a downward slope.

Significance: The negative correlation indicates that lower haemoglobin levels are associated with higher blood urea levels, reflecting potential anemia or worsening renal function. This inverse relationship could be critical for understanding the interplay between anemia and kidney function.

##Assessment of Missingness

### NMAR Analysis
