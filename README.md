# Environmental Compliance Risk Prediction - Machine Learning Deployment

## Project Description

This project develops an end-to-end Machine Learning solution for predicting environmental compliance risk levels.

The objective is to classify projects according to their probability of environmental non-compliance risk (Low, Medium, High), supporting preventive monitoring, resource prioritization, and data-driven environmental management.

The project includes:

- Exploratory Data Analysis (EDA)
- Data preprocessing pipeline
- Feature engineering
- Machine Learning model comparison
- Hyperparameter optimization
- Model evaluation
- API deployment using FastAPI
- Cloud deployment using Azure Virtual Machine
- CI/CD workflow with GitHub Actions

---

## Analyzed Datasets

Four datasets related to environmental and sustainability topics were analyzed:

### 1. Environmental Compliance Risk

A dataset focused on environmental management and regulatory compliance indicators.

The dataset contains information related to environmental projects, compliance characteristics, historical records, and risk-related variables.

**Proposed Machine Learning problem:**

- Supervised Classification
- Target variable: `non_compliance_risk`

---

### 2. OpenAQ Air Quality

A dataset containing air pollution measurements and environmental quality indicators.

The analysis focuses on pollutant concentration patterns and air quality classification.

**Proposed Machine Learning problem:**

- Supervised Classification
- Target variable: `air_quality`

---

### 3. CO₂ Global Emissions 1950-2024

A dataset containing historical global carbon dioxide emission records by country.

The analysis explores emission trends, emission sources, and differences between countries.

**Proposed Machine Learning problem:**

- Supervised Classification
- Target variable: `emission_level`

---

### 4. Global Climate Energy 2020-2024

A dataset containing climate, energy, sustainability, demographic, and economic indicators.

The analysis evaluates renewable energy participation and sustainability patterns.

**Proposed Machine Learning problem:**

- Supervised Classification
- Target variable: `sustainability_level`

---

# Exploratory Data Analysis Summary

The EDA process included:

- Dataset structure analysis.
- Descriptive statistical analysis.
- Numerical and categorical variable exploration.
- Missing value identification and treatment.
- Data consistency verification.
- Outlier detection.
- Correlation analysis.
- Target variable definition for Machine Learning classification problems.

Each dataset presented different characteristics and challenges:

| Dataset | Main Findings |
|---|---|
| Environmental Compliance Risk | Contains relevant environmental management indicators and provides a complete classification workflow opportunity |
| OpenAQ Air Quality | Shows pollutant concentration patterns related to air quality categories |
| CO₂ Global Emissions | Presents strong relationships between different emission sources and historical emission behavior |
| Global Climate Energy | Shows sustainability trends and renewable energy evolution between 2020 and 2024 |

---

# Selected Problem

After comparing the four datasets, the selected dataset for Machine Learning development is:

## Environmental Compliance Risk Prediction

The selected objective is:

**Predict environmental non-compliance risk using supervised classification algorithms.**

Target variable:

`non_compliance_risk`

---

## Selection Justification

The Environmental Compliance Risk dataset was selected because it provides the most complete Machine Learning challenge:

- Contains both numerical and categorical variables.
- Requires data preprocessing, encoding, scaling, and feature preparation.
- Represents a relevant environmental management problem.
- Allows the development of predictive models that could support preventive decision-making.
- Provides a practical application related to environmental compliance and risk management.

The future objective is to train and evaluate classification models capable of identifying environmental non-compliance risk patterns.

---
# Model Performance

Final selected model:

🌳 Optimized Decision Tree Classifier

Results:

- F1 Score: 99.7%
- High accuracy across Low, Medium and High risk categories

The model was evaluated using:

- Classification Report
- Confusion Matrix
- Performance metrics
---

# Repository Structure

```text
Environmental_Risk_Prediction

├── app
│   ├── main.py
│   └── schemas.py
│
├── datasets
│
├── images
│   ├── Visualizations
│
├── models
│
├── notebooks
│   ├── EDA
│   └── Model Development
│
├── selected_dataset
│
├── .github/workflows
│   └── CI pipeline
│
├── requirements.txt
│
└── README.md
```

---

# How to Run the Project

1. Clone this repository.

2. Install the required Python libraries.

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

3. Open the notebooks folder.

4. Execute the Jupyter notebooks to reproduce the exploratory analysis.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

# AI Usage Disclosure

Artificial Intelligence tools were used solely for English writing support, grammatical editing, and documentation formatting assistance.

All dataset selection decisions, analytical processes, data cleaning strategies, Machine Learning problem definition, interpretations, insights, and final conclusions were independently developed, reviewed, and validated by the author.

---

# Author

**Makarena Ampuero**

Role: Data Science Student

---


# License

This project is developed for educational purposes.
