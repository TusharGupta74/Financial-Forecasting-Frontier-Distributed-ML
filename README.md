# Financial Forecasting Frontier: A Distributed Machine Learning Approach

## Project Overview

This project demonstrates how Distributed Machine Learning can be applied in the banking domain to analyze customer data and predict whether a customer will subscribe to a term deposit. The project combines Big Data technologies including Hadoop, Hive, Apache Spark, Spark ML, and Spark Streaming to build a scalable end-to-end analytics pipeline.

---

## Business Problem

Banks generate massive amounts of customer and transaction data every day. Traditional systems struggle to process such large-scale datasets efficiently. This project leverages distributed computing techniques to improve data processing, analysis, and predictive modeling for better business decision-making.

---

## Objectives

- Store and process banking data using Hadoop.
- Perform SQL-based analysis using Hive.
- Conduct Exploratory Data Analysis (EDA) using Apache Spark.
- Build scalable Machine Learning models using Spark ML.
- Simulate real-time transaction analysis using Spark Streaming.
- Demonstrate data parallelism for efficient processing.

---

## Dataset

**Dataset:** Bank Marketing Dataset

Target Variable:

- **y** → Whether the customer subscribed to a term deposit.

Features include:

- Customer demographics
- Financial information
- Marketing campaign details
- Previous campaign outcomes

---

## Technologies Used

- Python
- Hadoop
- Hadoop MapReduce
- Apache Hive
- Apache Spark
- Spark SQL
- Spark MLlib
- Spark Streaming
- Google Colab
- VS Code

---

## Machine Learning Models

The following models were implemented and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1-Score

---

## Project Structure

```
Financial-Forecasting-Frontier-Distributed-ML
│
├── Dataset/
│   └── bank.csv
│
├── hadoop/
│   ├── mapper_*.py
│   └── reducer_*.py
│
├── Notebooks/
│   └── Financial Forecasting Frontier_Distributed ML.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Results

- Successfully performed distributed data processing using Hadoop and Spark.
- Built multiple classification models for customer subscription prediction.
- Compared model performance using standard evaluation metrics.
- Identified Random Forest as the best-performing model.

---

## Future Improvements

- Deploy the model using Flask or FastAPI.
- Integrate Kafka for real-time streaming.
- Deploy Spark Cluster on AWS.
- Build an interactive dashboard for business users.

---

## Author

**Tushar Gupta**

M.Sc. Computer Science (Machine Learning & AI)
