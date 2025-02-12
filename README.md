# Navigating COVID-19 Research Data: An Integrated Analysis of Epidemiology, Government Policies, and Public Sentiment

## Project Information
**Author**: Shouzhifan Zhu  
**Instructor**: Prof. Luyao Zhang  

## Table of Contents

- [Overview](#overview)
- [Research Questions](#research-questions)
- [Disclaimer](#disclaimer)
- [Acknowledgments](#acknowledgments)
- [Navigation Instructions](#navigation-instructions)
- [Dataset](#dataset)
- [Applications](#applications)
- [Embedded Media](#embedded-media)
  - [Demo Video](#demo-video)
  - [Poster](#poster)
- [Statement of Intellectual and Professional Growth](#statement-of-intellectual-and-professional-growth)
- [Implementation](#implementation)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    1. [Visualize COVID-19 Trends and Policy Impacts](#1-visualize-covid-19-trends-and-policy-impacts)
    2. [Explore Social Media Reactions and Sentiment](#2-explore-social-media-reactions-and-sentiment)
    3. [SHAP Analysis for Policy and Social Media Influence](#3-shap-analysis-for-policy-and-social-media-influence)
    4. [Geospatial Visualizations and Mapping](#4-geospatial-visualizations-and-mapping)
    5. [Policy Response and Network Analysis](#5-policy-response-and-network-analysis)
- [License](#license)
- [References](#references)

---
## Overview
This project examines the interplay between global COVID-19 infection trends, government policies, and public sentiment on social media. By integrating epidemiological data, policy measures, and large-scale Twitter analysis, we assess how public discourse and engagement evolved throughout different phases of the pandemic. Our study explores key factors influencing tweet volumes and sentiment, highlighting the complex interaction between policy responses, public reactions, and the shifting dynamics of pandemic progression across regions. Through a multi-dimensional approach, this research provides insights into the relationship between crisis communication, government interventions, and public sentiment trends during the COVID-19 pandemic.

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

## Applications

1. **Public Health Policy Development**:
   - Analyze the effectiveness of government interventions, such as lockdowns and travel restrictions, on COVID-19 case trends.
   - Provide data-driven insights to inform adaptive policymaking and crisis response strategies.

2. **Media and Public Communication**:
   - Track public sentiment and emotional responses to major COVID-19 events for more effective crisis communication.
   - Develop targeted messaging strategies to address misinformation and public concerns.

3. **Epidemiological Research**:
   - Investigate correlations between COVID-19 case surges and public sentiment to improve early warning systems.
   - Assess the impact of public behavior on infection rates to guide future pandemic preparedness.

4. **Social Media and Digital Analysis**:
   - Examine how social media engagement fluctuates with policy changes and pandemic phases.
   - Identify key topics and emotional triggers that drive public discussions about COVID-19.

5. **Machine Learning and Predictive Analytics**:
   - Utilize SHAP (Shapley Additive Explanations) to interpret the impact of various factors on COVID-19 case predictions.
   - Develop models to forecast social media reactions to new pandemic developments.

6. **Global and Regional Comparisons**:
   - Compare pandemic responses and public sentiment trends across different countries and regions.
   - Highlight best practices from various governments in managing public health crises.

7. **Healthcare and Resource Allocation**:
   - Use sentiment analysis to detect potential public dissatisfaction and optimize healthcare communication.
   - Guide the allocation of medical resources based on regional variations in case trends and public concern.

8. **Educational and Training Programs**:
   - Provide case studies on the intersection of government policy, public sentiment, and epidemiology for academic research.
   - Develop data-driven tools to enhance public health education and crisis management training.
  
---

## Embedded Media
### Demo Video

🔹 **The video can be viewed in the repository at** [Docs/demo_video.mp4](https://github.com/ManchesterBlue/Info301_Final/tree/main/Docs/demo_video.mp4).  
🔹 **For the subtitled version, please visit** [this link](https://duke.box.com/s/x0pja0lni6inxcb41dkn40tsviadxgts).


### Poster
![Final_Poster](https://github.com/user-attachments/assets/e379b793-f2e3-4f52-8574-d94232fb923e)

---

### Statement of Intellectual and Professional Growth

Through this course, we have gained a deeper appreciation for data visualization techniques and their significance in effectively conveying complex information. This project has sharpened our ability to create engaging, interactive visualizations that not only present data but also enhance comprehension. Additionally, it has strengthened our proficiency in transforming raw data into meaningful narratives that drive insightful discussions. The collaborative nature of this experience has further refined our teamwork and communication abilities, as we worked closely to tackle data-driven challenges, integrate multiple perspectives, and develop visual storytelling approaches suited for professional contexts.

---

## Implementation

### Requirements

To set up and run this project, you will need to install the following dependencies:

  - `pandas`
  - `geopandas`
  - `plotly`
  - `pycountry`
  - `xgboost`
  - `shap`
  - `pmdarima`
  - `numpy`
  - `dash`
  - `json`
  - `dash_cytoscape`
  - `networkx`

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/ManchesterBlue/Info301_Final.git
cd Info301_Final
pip install -r requirements.txt
```
### Usage

 1. Visualize COVID-19 Trends and Policy Impacts

- **[Time-series analysis and policy responses](https://github.com/ManchesterBlue/Info301_Final/tree/main/Code/app)**
  
  ```bash
  python Code/app/trend_chart.py
  ```

- **[Choropleth map showing global COVID-19 case distribution](https://github.com/ManchesterBlue/Info301_Final/tree/main/Code/app)**
  
  ```bash
  python Code/app/choropleth_map.py
  ```

- **[Curve graphs illustrating pandemic progression](https://github.com/ManchesterBlue/Info301_Final/tree/main/Code)**
  
  ```bash
  python Code/Curve_Graphs.ipynb
  ```

 2. Explore Social Media Reactions and Sentiment

- **[Visualizing emotion intensity and sentiment in tweets](https://github.com/ManchesterBlue/Info301_Final/tree/main/Code)**
  
  ```bash
  python Code/Emotion_and_its_Intensity.ipynb
  ```

- **[Keyword network analysis from Twitter data](https://github.com/ManchesterBlue/Info301_Final/tree/main/Code/app)**
  
  ```bash
  python Code/app/keyword_network.py
  ```

 3. SHAP Analysis for Policy and Social Media Influence

- **[SHAP interpretation of confirmed case trends](https://github.com/ManchesterBlue/Info301_Final/tree/main/Code)**
  
  ```bash
  python Code/SHAP_Confirmed_Cases.ipynb
  ```

- **[SHAP interpretation for Twitter engagement](https://github.com/ManchesterBlue/Info301_Final/tree/main/Code)**
  
  ```bash
  python Code/SHAP_TWEET.ipynb
  ```

 4. Geospatial Visualizations and Mapping

- **[Mapping tweet distribution and corresponding SHAP visualizations](https://github.com/ManchesterBlue/Info301_Final/tree/main/Code)**
  
  ```bash
  python Code/INFO.ipynb
  ```

- **[Interactive COVID-19 spread and interventions](https://github.com/ManchesterBlue/Info301_Final/tree/main/Code)**
  
  ```bash
  python Code/map1.ipynb
  python Code/map2.ipynb
  ```

 5. Policy Response and Network Analysis

- **[Analyzing government policy responses](https://github.com/ManchesterBlue/Info301_Final/tree/main/Code/app)**
  
  ```bash
  python Code/app/policy_response.py
  ```

## License

This project is distributed under the MIT License. For more details, please refer to the [LICENSE](https://github.com/ManchesterBlue/Info301_Final/blob/main/LICENSE) file.

---

## References

- **Qatar Computing Research Institute (QCRI)**. (2020). *GeoCov19: A dataset of hundreds of millions of multilingual COVID-19 tweets with location information*. ACM Digital Library. [https://dl.acm.org/doi/10.1145/3404820.3404823](https://dl.acm.org/doi/10.1145/3404820.3404823)

- **Gupta, R., Vishwanath, A., & Yang, Y.** (2022). *COVID-19 Twitter Dataset with Latent Topics, Sentiments and Emotions Attributes*. Ann Arbor, MI: Inter-university Consortium for Political and Social Research (ICPSR). [https://doi.org/10.3886/E120321V12](https://doi.org/10.3886/E120321V12)

- **Mathieu, E., Ritchie, H., Rodés-Guirao, L., Appel, C., Gavrilov, D., Giattino, C., Hasell, J., Macdonald, B., Dattani, S., Beltekian, D., Ortiz-Ospina, E., & Roser, M.** (2020). *Coronavirus (COVID-19) Cases*. Published online at *Our World in Data*. Retrieved from [https://ourworldindata.org/covid-cases](https://ourworldindata.org/covid-cases)

- **COVID-19 Data Hub**. (2020). *COVID-19 Global Case and Policy Dataset*. Retrieved from [https://github.com/covid19datahub/COVID19](https://github.com/covid19datahub/COVID19)

---

