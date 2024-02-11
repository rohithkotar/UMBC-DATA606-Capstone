# Injury Severity Prediction for Unbalanced Data Set

## Project Details

- **Prepared for**: UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang
- **Author Name**: Rohith Kotar
- **Link to the author's GitHub profile**: https://github.com/KotarRohith
- **Link to the author's LinkedIn profile**: https://www.linkedin.com/in/rohith-kotar/
- **Link to your PowerPoint presentation file**: 
- **Link to your YouTube video**: 

## Background

- **Objective**: This project aims to develop a robust predictive modeling approach for estimating injury severity in accidents using an unbalanced dataset.
- **Significance**:
   - Accurate prediction of injury severity can lead to more efficient resource allocation in emergency response systems, potentially saving lives by ensuring            timely and appropriate medical attention.
    - Improved injury severity prediction can aid in the development of proactive measures for accident prevention, contributing to overall public safety and             reducing the occurrence of severe accidents.
    - Reliable injury severity prediction models can facilitate the development of personalized treatment plans for accident victims, optimizing healthcare               resources and improving patient outcomes.
    - The insights gained from this research can have broader implications beyond accident-related injuries, potentially informing predictive modeling efforts in         other domains with imbalanced datasets, such as healthcare and finance.

- **Research Questions**: 
  - How can we effectively address class imbalance in the dataset during the process of injury severity prediction?
  - Which machine learning algorithms demonstrate superior performance in predicting injury severity within unbalanced datasets?
  - Are there any trade-offs between model performance and computational efficiency when using sampling versus non-sampling approaches?
- **Additional Considerations**: 
  - In this study, various sampling methods, including oversampling and undersampling techniques, will be explored to mitigate class imbalance within the dataset.
  - Comparative analysis will be conducted by training predictive models both with and without sampling methods to discern their impact on predictive accuracy.

## Data

- **Data sources**: https://data.montgomerycountymd.gov/Public-Safety/Crash-Reporting-Drivers-Data/mmzv-x632/about_data
- **Data size**: 84MB
- **Data shape**: (172105, 51)
- **Target/label**: injury_severity
      injury_severity
      NO APPARENT INJURY          141185
      POSSIBLE INJURY              17482
      SUSPECTED MINOR INJURY       11870
      SUSPECTED SERIOUS INJURY      1415
      FATAL INJURY                   153
## Tools and Technologies
   Snowflake and AWS Service for complete development and deployment of model.
## Exploratory Data Analysis (EDA)
  - Dataset is imbalanced.
  - Features needs to be transformed.
  - Feature extraction is required.
## Model Training

- **Predictive Analytics Models**: 
  - Logistic Regression
  - XGBoost
  - Random Forest
  - AdaBoost
  - Gradient Boosting
  - Ensemble Models (combination of above algorithms)
  - Each model will be tuned using hyperparameter optimization techniques such as GridSearchCV.
  
- **Sampling Techniques**:
  - Various sampling methods will be employed to address class imbalance, including:
    - Random Oversampling
    - SMOTE (Synthetic Minority Over-sampling Technique)
    - ADASYN (Adaptive Synthetic Sampling)
    - Random Undersampling
- **Train vs Test Split**: 
  - The dataset will be split into training and testing sets using an 80:20 ratio, ensuring a sufficient amount of data for model training and evaluation.

- **Performance Measurement**: 
  - Model performance will be assessed using the following metrics:
    - Precision
    - Recall
    - F1-Score
    - ROC Curves
## Conclusion


## References

https://scikit-learn.org/stable/modules/grid_search.html

https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74

Feature Engineering - https://www.youtube.com/playlist?list=PLKnIA16_RmvYXWH_E6PuVLLHHTWXwwDN7

