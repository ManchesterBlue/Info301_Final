# INFOSCI 301 Final Project

**Author**: Shouzhifan Zhu  
**Instructor**: Prof. Luyao Zhang  

## Table of Contents
1. [Introduction](#introduction)
2. [Research Questions](#research-questions)
3. [Dataset](#dataset)
    - [Original Data Sources and Collection](#original-data-sources-and-collection)
    - [Geographical Coverage](#geographical-coverage)
    - [Temporal Coverage](#temporal-coverage)
    - [Languages](#languages)
    - [Data Structure](#data-structure)
    - [Data Features](#data-features)
    - [Data Processing and Preprocessing](#data-processing-and-preprocessing)
4. [Analysis Tools](#analysis-tools)
5. [Results](#results)
6. [References](#references)

---

## Introduction
This project explores the relationship between global COVID-19 infection trends, government policies, and public sentiment on social media. By integrating epidemiological data, policy response measures, and large-scale Twitter data, we aim to understand how public discussions evolved alongside the pandemic's progression. The project employs **SHAP (Shapley Additive Explanations)** to break down the contribution of various temporal, geographical, and policy-driven factors, offering interpretable insights into what drives pandemic-related social media engagement.

<img width="888" alt="image" src="https://github.com/user-attachments/assets/64a584b7-17eb-40c7-ad71-48f2257ffe71" />


---

## Research Questions

1. **COVID-19 Spread and Evolution**  
   - How did global COVID-19 infection trends vary across different regions?
   - What were the temporal patterns of pandemic progression?

2. **Government Policy Impact**  
   - How did policy stringency levels (e.g., lockdowns, travel bans) influence infection trends?
   - Did stricter policies correlate with changes in public sentiment and engagement?

3. **Public Sentiment and Social Media Engagement**  
   - How did COVID-19-related Twitter activity vary across time and geography?
   - What were the predominant emotions and topics discussed on social media during key pandemic phases?

---

## Dataset
This project integrates multiple datasets to analyze the impact of COVID-19 on global public discourse and government responses:

- [**GeoCov19 Twitter Dataset**](https://crisisnlp.qcri.org/covid19): A large collection of geotagged and location-metadata tweets related to COVID-19.
- [**OpenICPSR COVID-19 Sentiment and Topic Dataset**](https://www.openicpsr.org/openicpsr/project/120321/version/V12/view): A dataset containing sentiment classification and topic modeling of COVID-19-related tweets.
- [**Our World in Data COVID-19 Statistics**](https://ourworldindata.org/covid-cases): Aggregated COVID-19 case numbers, hospitalizations, recoveries, and government policy responses.
- [**COVID-19 Global Case and Policy Dataset**](https://covid19datahub.io/): This dataset compiles country-level data on confirmed COVID-19 cases, deaths, recoveries, hospitalizations, and vaccinations.

### Original Data Sources and Collection
- **Social Media (Twitter)**: Public discussions on COVID-19 were collected using over **800 predefined keywords** and hashtags.
- **Epidemiological Data**: Official records on confirmed cases, deaths, recoveries, and hospitalizations.
- **Policy Data**: Government responses, including lockdown measures, economic support, and vaccination policies.

### Geographical Coverage
- **Global Scope**: The dataset includes data from over **218 countries** and **47,000+ cities**.
- **Location-based Features**: Country and city-level analysis using **ISO 3166-1** country codes.

### Temporal Coverage
- **From the pandemic onset to various key phases**: The study spans multiple timeframes, focusing on key pandemic milestones.
- **Timestamped Data**: Social media activity is mapped against real-world events to detect correlation patterns.

### Languages
- **Multilingual Analysis**: Tweets in **62+ languages** enable cross-cultural sentiment analysis.

### Data Structure
- **Social Media Data**: Includes tweet ID, timestamps, user information, location, text content, and hashtags.
- **Epidemiological Data**: Daily and cumulative case numbers, deaths, and recovery trends.
- **Policy Data**: Stringency measures, economic relief, and vaccination rollout tracking.

### Data Features
- **Temporal**: `Weekday`, `Month`, `Weekend Effect`, `Policy Implementation Date`.
- **Geographical**: Country, state, city-based variations in COVID-19 discourse.
- **Sentiment and Topic Analysis**: Classifications of public sentiment (positive, neutral, negative) and discussion topics.

### Data Processing and Preprocessing
- **Standardization**: Cleaning and structuring timestamps, geolocation data, and policy response tracking.
- **Feature Engineering**: Extracting key variables for machine learning models.
- **Aggregation**: Analysis of tweet counts, case numbers, and policy measures across time intervals.

---

## Visualization
### Global Spread of COVID-19 Over Time
<img width="888" alt="image" src="https://github.com/user-attachments/assets/153a19fa-06c0-4913-a68c-5b1676e78ec4" />

### Government Policy Responses and Their Evolution
<img width="888" alt="image" src="https://github.com/user-attachments/assets/8b049ab5-4970-444d-95ae-678f239a3ee5" />

### Tweet Volume and Global Social Media Engagement
<img width="888" alt="image" src="https://github.com/user-attachments/assets/a95898ba-f407-41d4-9247-a2ffce4b2033" />

### Relationship Between Confirmed Cases and Government Stringency
<img width="888" alt="image" src="https://github.com/user-attachments/assets/aaf0e53b-9fa9-4d03-85ff-a6d53c358f0a" />

### COVID-19 Trends in the Most Affected Countries
<img width="888" alt="image" src="https://github.com/user-attachments/assets/cf7a427f-3d50-4076-9eab-02ede4a01e95" />

### SHAP Summary Plot for Temporal Features (Tweet Volume)
<img width="369" alt="image" src="https://github.com/user-attachments/assets/b4925a41-1690-4c20-9315-c4ca2a8add25" />

### SHAP Summary Plot for Temporal Features (COVID-19 Cases)
<img width="371" alt="image" src="https://github.com/user-attachments/assets/dde2a20d-63c3-496d-a5c1-a5193b6041a7" />

### SHAP Summary Plot for Geographical Features (Tweet Volume)
<img width="234" alt="image" src="https://github.com/user-attachments/assets/addf1f6b-2ac0-4da1-bf23-ef4f9d2281f5" />

### SHAP Summary Plot for Geographical Features (COVID-19 Cases)
<img width="283" alt="image" src="https://github.com/user-attachments/assets/11a99056-a080-4692-8bea-c578ef24d39d" />

### SHAP Summary Plot for Government Policy Measures
<img width="299" alt="image" src="https://github.com/user-attachments/assets/4d8bf4d8-e93e-462f-b04a-2e203c5a797b" />


---

## Analysis Tools

- **Machine Learning Models**: Logistic Regression and **XGBoost** for trend prediction and sentiment analysis.
- **SHAP Analysis**: To quantify the influence of different factors on tweet volumes and infection rates.
- **Geospatial Analysis**: Visualization of global tweet distribution using **GeoPandas** and **Plotly**.
- **Time Series Analysis**: Exploring weekly/monthly variations in tweet activity and case trends.

---

## Results

### 1. Temporal Dynamics and SHAP Analysis
- **Weekend Effect**: Higher social media engagement during weekends.
- **Policy Shifts and Public Sentiment**: Stricter lockdowns correlated with spikes in negative sentiment and higher tweet volumes.

### 2. Geospatial Trends in Social Media Activity
- **Countries with High Tweet Volume**: USA, China, India, UK, Brazil.
- **Regions with Low Engagement**: Parts of Africa and Central Asia showed minimal COVID-19-related social media discussions.

### 3. Relationship Between Public Sentiment and Government Policies
- **Strict Government Policies → Increased Public Frustration**: Higher stringency scores aligned with spikes in tweets expressing negative sentiment.
- **Vaccine Rollouts → Positive Sentiment Spikes**: Public optimism increased in regions with successful vaccine distributions.

---

## Conclusion
This study highlights how public sentiment and online discussions evolved alongside COVID-19 case trends and policy interventions. By leveraging **SHAP analysis**, we identified key temporal and geographical drivers of pandemic-related social media activity. The results suggest that **public engagement with COVID-19 discussions was heavily influenced by weekends, policy shifts, and regional differences in government responses**.

Future work can expand on this by integrating **real-time social media monitoring**, further refining sentiment analysis techniques, and exploring additional contextual factors influencing public discourse.

---

## References
- [GeoCov19 Dataset](https://crisisnlp.qcri.org/covid19)
- [OpenICPSR COVID-19 Dataset](https://www.openicpsr.org/openicpsr/project/120321/version/V12/view)
- [Our World in Data COVID-19 Statistics](https://ourworldindata.org/covid-cases)
- [SHAP Documentation](https://shap.readthedocs.io/en/latest/index.html)

---

