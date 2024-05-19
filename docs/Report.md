# Injury Severity Prediction for Unbalanced Data Set Using ML Techniques

- **Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang
- **Author Name:** Rohith Kotar
- **GitHub Profile:** [Rohith Kotar](https://github.com/KotarRohith)
- **LinkedIn Profile:** [Rohith Kotar](https://www.linkedin.com/in/rohith-kotar/)
- **Link to PowerPoint Presentation:** [Link]
- **Link to YouTube Video:** [Link]

## Background

### Objective:
This project aims to develop a robust predictive modeling approach for estimating injury severity in accidents using an unbalanced dataset.

### Significance:
- Accurate prediction of injury severity can lead to more efficient resource allocation in emergency response systems, potentially saving lives by ensuring timely and appropriate medical attention.
- Improved injury severity prediction can aid in the development of proactive measures for accident prevention, contributing to overall public safety and reducing the occurrence of severe accidents.
- Reliable injury severity prediction models can facilitate the development of personalized treatment plans for accident victims, optimizing healthcare resources and improving patient outcomes.
- The insights gained from this research can have broader implications beyond accident-related injuries, potentially informing predictive modeling efforts in other domains with imbalanced datasets, such as healthcare and finance.

### Research Questions:
1. How can we effectively address class imbalance in the dataset during the process of injury severity prediction?
2. Which machine learning algorithms demonstrate superior performance in predicting injury severity within unbalanced datasets?
3. Are there any trade-offs between model performance and computational efficiency when using sampling versus non-sampling approaches?

### Additional Considerations:
- Various sampling methods, including oversampling and undersampling techniques, explored to mitigate class imbalance within the dataset.
- Comparative analysis will be conducted by training predictive models both with and without sampling methods to discern their impact on predictive accuracy.

## Data

- **Data sources:** [Montgomery County Crash Reporting Drivers Data](https://data.montgomerycountymd.gov/Public-Safety/Crash-Reporting-Drivers-Data/mmzv-x632/about_data)
- **Data size:** 84MB
- **Data shape:** (172105, 51)
- **Target/label:** injury_severity
    - NO APPARENT INJURY: 141185
    - POSSIBLE INJURY: 17482
    - SUSPECTED MINOR INJURY: 11870
    - SUSPECTED SERIOUS INJURY: 1415
    - FATAL INJURY: 153

## Exploratory Data Analysis (EDA)

- Dataset is imbalanced.
- Features are transformed.
- Feature extraction is done creating new columns for accurate prediction of target.

## Model Training

### Predictive Analytics Models:
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- Ensemble Models (combination of above algorithms)
    - Each model is tuned using hyperparameter optimization techniques such as GridSearchCV.

### Sampling Techniques:
- Below sampling methods employed to address class imbalance, including:
    - Random Oversampling
    - SMOTE (Synthetic Minority Over-sampling Technique)
- Since dataset is large running sampling methods took longer time. Ran different models in different systems. SMOTE performed better when compared to others.


### Train vs Test Split:
- The dataset splitted into training and testing sets using an 80:20 ratio, ensuring a sufficient amount of data for model training and evaluation.

### Performance Measurement:
- Model performance will be assessed using the following metrics:
    - Precision
    - Recall
    - F1-Score



## Conclusion

https://czuoqygrbvyevqjg9xflec.streamlit.app/

If you have any problem loading python files on github paste the link in https://nbviewer.org/ to view the ipynb file.

## References

- [Grid Search in scikit-learn](https://scikit-learn.org/stable/modules/grid_search.html)
- [Hyperparameter Tuning the Random Forest in Python using scikit-learn](https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74)
- [Feature Engineering](https://www.youtube.com/playlist?list=PLKnIA16_RmvYXWH_E6PuVLLHHTWXwwDN7)
- Feature Engineering for Machine Learning: Strategies for Data Preprocessing by Kuhn, M., and Johnson, K. (2019)
- "Injury Severity Prediction: A Review of Literature and Methods" by Abdel-Wahab, O. M., et al. (2009). This paper provides a comprehensive overview of injury severity prediction methods.



