## SpaceX Falcon 9 Launch Success Analysis 🚀
Welcome to the SpaceX Falcon 9 Launch Success Analysis project! This repository showcases my work on analyzing and predicting the success of SpaceX Falcon 9 first-stage landings, providing insights into launch outcomes and their impact on cost optimization.

## Project Overview
This project aimed to predict the success of Falcon 9 first-stage landings using data from SpaceX APIs and web scraping. By exploring trends, building visualizations, and training predictive models, the project provides valuable insights into factors influencing launch outcomes.

## Key Highlights:
**Data Sources**: SpaceX API and Wikipedia.\n
**Technologies Used**: Python, SQL, Folium, Plotly Dash, and Machine Learning.
**Key Analyses**: Exploratory Data Analysis (EDA), Predictive Modeling, and Interactive Dashboards.

## Key Features 🚀
#### 1. Data Collection and Wrangling
**API**: Extracted data from SpaceX API.
**Web Scraping**: Gathered data from Wikipedia.
Performed data cleaning and categorized missing values for further analysis.

#### 2. Exploratory Data Analysis (EDA)
Visualized launch success rates, trends, and key patterns using Matplotlib and Seaborn.
Analyzed success by payload, orbit, and launch sites.
EDA Notebook.

#### 3. Interactive Mapping
Built interactive maps with Folium to visualize launch sites and success rates.
Mapped proximities to railways, highways, and coastlines for optimal site planning.
Interactive Map Code.

#### 4. Dashboards with Plotly Dash
Created dynamic dashboards to analyze payload success across different launch sites.
Interactive sliders and pie charts for granular insights.
Dashboard Code.

#### 5. Predictive Analysis
**Models used**: Logistic Regression, Support Vector Machines, Decision Trees, K-Nearest Neighbors.
Achieved **94.44%** accuracy using Logistic Regression, SVM, and KNN models.
Machine Learning Notebook.

## Results
#### Key Findings:
Success rates have steadily increased since 2013.
Payload and launch site influence success significantly.
Logistic Regression offers a balance of accuracy and interpretability, achieving 94.44% accuracy.

**Visualizations:**
Trends in success by orbit and payload mass.
Maps of launch site proximities and outcomes.

## Repository Structure 📂
.
├── data/
├── notebooks/
│   ├── spacex-data-wrangling.ipynb
│   ├── eda-visualizations.ipynb
│   ├── interactive-mapping.ipynb
│   ├── dashboards.ipynb
│   └── machine-learning-predictions.ipynb
├── results/
└── README.md
