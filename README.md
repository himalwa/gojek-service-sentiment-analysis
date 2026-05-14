# 🚖 Gojek Service Sentiment Analysis

## 📌 Overview

This project analyzes public sentiment toward Gojek services using Twitter (X) data collected between January–April 2025. The objective was to understand customer perception patterns and compare the performance of multiple machine learning classification models.

## 🛠️ Tools & Technologies

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/RapidMiner-FF6600?style=for-the-badge&logoColor=white"/>
  <img src="https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white"/>
  <img src="https://img.shields.io/badge/Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white"/>
  <img src="https://img.shields.io/badge/Twitter_API-1DA1F2?style=for-the-badge&logo=x&logoColor=white"/>
</p>

## ⚙️ Research Workflow

- Tweet crawling and data collection
- Text preprocessing and cleaning
- Sentiment labeling
- Model training and evaluation
- Comparative analysis of:
  - Naïve Bayes
  - Support Vector Machine (SVM)
  - Random Forest

## 📊 Model Performance

| Model | Accuracy | F1-Score |
|---|---|---|
| Naïve Bayes | 75.09% | 74.63% |
| SVM | 70.34% | 72.30% |
| Random Forest | 70.55% | 71.22% |

Naïve Bayes achieved the best overall balance between precision and recall, making it the most stable model for this dataset.

## 💡 Key Insights

The analysis found that negative sentiment was primarily influenced by:
- Technical application issues
- Customer service responsiveness
- Driver cancellation experience

The findings suggest that improving system stability and customer support quality could help increase overall customer satisfaction.

## 🖼️ Project Preview

<p align="center">
  <img src="images/sentiment-analysis-bar.png" width="48%" />
  <img src="images/wordcloud.png" width="48%" />
</p>

## 📚 Research Context

This project was developed as a final thesis project for the Information Systems undergraduate program.
