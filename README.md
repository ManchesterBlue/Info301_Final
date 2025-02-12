# Navigating COVID-19 Research Data: An Integrated Analysis of Epidemiology, Government Policies, and Public Sentiment

## Project Information
**Author**: Shouzhifan Zhu  
**Instructor**: Prof. Luyao Zhang  

##

## Table of Contents
1. [Introduction](#introduction)
2. [Research Questions](#research-questions)
3. [Dataset](#dataset)
4. [Analysis Tools](#analysis-tools)
5. [Results](#results)
6. [References](#references)

---
## Introduction
This project examines the interplay between global COVID-19 infection trends, government policies, and public sentiment on social media. By integrating epidemiological data, policy measures, and large-scale Twitter analysis, we assess how public discourse and engagement evolved throughout different phases of the pandemic. Our study explores key factors influencing tweet volumes and sentiment, highlighting the complex interaction between policy responses, public reactions, and the shifting dynamics of pandemic progression across regions. Through a multi-dimensional approach, this research provides insights into the relationship between crisis communication, government interventions, and public sentiment trends during the COVID-19 pandemic.

![image](https://github.com/user-attachments/assets/6af6a0c0-29e6-4a74-a439-389d08f0ae0e)

## Research Questions

1. **COVID-19 Spread and Evolution**  
   - How did COVID-19 infection trends fluctuate across different regions and time periods?  
   - What patterns emerged in confirmed cases, hospitalizations, and deaths over the course of the pandemic?  

2. **Government Policy Impact**  
   - How did various government interventions (e.g., lockdowns, travel restrictions, vaccination campaigns) influence infection rates?  
   - Did stricter policies lead to noticeable shifts in public sentiment and social media engagement?  

3. **Public Sentiment and Social Media Trends**  
   - How did COVID-19-related Twitter activity change over time and across geographical regions?  
   - What were the dominant emotions and topics discussed, and how did they align with major pandemic events and policy changes?  

---

## Disclaimer

This project was conducted as part of **INFOSCI 301: Data Visualization and Information Aesthetics**, under the guidance of **Prof. Luyao Zhang** at **Duke Kunshan University** in Autumn 2024. We deeply appreciate Professor Zhang’s invaluable insights, encouragement, and expertise, which greatly enhanced our understanding of data-driven storytelling and analytical visualization. The project integrates multiple datasets to explore the intersection of epidemiology, policy measures, and public sentiment during the COVID-19 pandemic.

## Acknowledgments

We would like to extend our gratitude to the following individuals and resources:

- **Prof. Luyao Zhang** for providing insightful guidance, constructive feedback, and continuous support throughout the course.
- **Our classmates** for their valuable discussions, suggestions, and collaboration during the project.
- **AIGC tools** like **ChatGPT** for assistance in refining ideas, debugging code, and enhancing our analysis; **Whimsical** for aiding in the creation of flowcharts and visual frameworks.
- **Datasets** that formed the foundation of our research:
  - [**GeoCov19 Twitter Dataset**](https://crisisnlp.qcri.org/covid19) for geotagged and location-based COVID-19 tweet analysis.
  - [**OpenICPSR COVID-19 Sentiment and Topic Dataset**](https://www.openicpsr.org/openicpsr/project/120321/version/V12/view) for sentiment classification and topic modeling.
  - [**Our World in Data COVID-19 Statistics**](https://ourworldindata.org/covid-cases) for global epidemiological trends and policy records.
  - [**COVID-19 Global Case and Policy Dataset**](https://covid19datahub.io/) for tracking country-level COVID-19 cases, interventions, and public health measures.

Their collective contributions have significantly shaped the depth and scope of our project.

---

## Navigation Instructions

To explore this repository, follow the instructions below:

### [Code](https://github.com/ManchesterBlue/Info301_Final/tree/main/Code)
The `Code` folder contains scripts for data processing, analysis, and visualization used in this project.

### [Sample Datasets & Processed Data](https://github.com/ManchesterBlue/Info301_Final/tree/main/Data)
The `Data` folder includes all datasets utilized in this study, encompassing both raw and processed data.

### [Documentation](https://github.com/ManchesterBlue/Info301_Final/tree/main/Docs)
The `Docs` folder contains supplementary materials, reports, and references for the project.

### [Pilot Visualizations & Figures](https://github.com/ManchesterBlue/Info301_Final/tree/main/Visualization)
The `Visualization` folder provides sample visualizations and figures generated during the analysis.

---

## Dataset
This project integrates multiple datasets to analyze the impact of COVID-19 on global public discourse and government responses:

- [**GeoCov19 Twitter Dataset**](https://crisisnlp.qcri.org/covid19): A large collection of geotagged and location-metadata tweets related to COVID-19.
- [**OpenICPSR COVID-19 Sentiment and Topic Dataset**](https://www.openicpsr.org/openicpsr/project/120321/version/V12/view): A dataset containing sentiment classification and topic modeling of COVID-19-related tweets.
- [**Our World in Data COVID-19 Statistics**](https://ourworldindata.org/covid-cases): Aggregated COVID-19 case numbers, hospitalizations, recoveries, and government policy responses.
- [**COVID-19 Global Case and Policy Dataset**](https://covid19datahub.io/): This dataset compiles country-level data on confirmed COVID-19 cases, deaths, recoveries, hospitalizations, and vaccinations.

By integrating these diverse datasets, our study captures the intersection of epidemiological trends, government interventions, and public sentiment. This approach enables a deeper understanding of how policy measures shaped public discourse and how social media activity reflected pandemic developments. The analysis also helps assess whether social media trends can serve as early indicators of public health concerns, providing valuable insights for crisis management and policy adaptation.

## Embedded Media
### Demo Video

🔹 **The video can be viewed in the repository at** [Docs/demo_video.mp4](https://github.com/ManchesterBlue/Info301_Final/tree/main/Docs/demo_video.mp4).  
🔹 **For the subtitled version, please visit** [this link](https://duke.box.com/s/x0pja0lni6inxcb41dkn40tsviadxgts).


### Poster
![Final_Poster](https://github.com/user-attachments/assets/e379b793-f2e3-4f52-8574-d94232fb923e)

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

