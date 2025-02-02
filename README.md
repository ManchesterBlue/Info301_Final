# INFOSCI 301 Final Project

**Author**: Shouzhifan Zhu

**Instructor**: Prof. Luyao Zhang  

## Table of Contents
1. [Introduction](#introduction)
2. [Research Question](#research-question)
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
    - [1. Temporal Distribution (SHAP Plot)](#1-temporal-distribution-shap-plot)
    - [2. Global Distribution of Tweets](#2-global-distribution-of-tweets)
    - [3. SHAP Values for Geographical Distribution](#3-shap-values-for-geographical-distribution)
6. [References](#references)

---

## Introduction
This project explores the distribution of COVID-19-related tweets from **February 1 to February 10, 2020**. We aim to uncover **temporal trends** (daily, monthly) and **geographical patterns** (by country, city), while also assessing the **impact of different features** on tweet volume predictions using **SHAP** (SHapley Additive exPlanations). By highlighting these trends, we hope to offer insights into global engagement and discussion patterns around the COVID-19 pandemic during its early stages.

---

## Research Question

1. **Investigate Temporal Trends**  
   - Examine how tweet frequency varies by day of the week and month.  
   - Explore whether there is a noticeable increase on weekends or specific months.

2. **Explore Geographical Patterns**  
   - Analyze tweet volume across different countries and cities.  
   - Identify regions with the highest activity and compare trends across locations.

3. **Assess the Impact of Features (via SHAP)**  
   - Evaluate how features like `weekday`, `month`, and `geographical location` contribute to **predicted tweet counts**.  
   - Determine which features have the most significant influence on the model’s predictions.

---

## Dataset

The dataset comprises COVID-19-related tweets from **February 1 to February 10, 2020**. Due to [GitHub’s file size limitations](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github), the explicit dataset is provided through a [BOX folder link](https://duke.box.com/s/mlamr9af858ayo6vbca215mg95477we2). The original dataset is published on the [GeoCoV19 page](https://crisisnlp.qcri.org/covid19).

> **Note**: We employed a **few-shot** approach by selecting a **ten-day** subset (February 1–10, 2020) for this project.

### Original Data Sources and Collection
- **Twitter**: Tweets are related to COVID-19 (keywords, hashtags, mentions).
- **Collection Method**: Over **800 predefined keywords** associated with COVID-19.
- **Geotagging**:  
  - **378K** geotagged tweets.  
  - **5.4 million** tweets with location data but without explicit geotags.

### Geographical Coverage
- **Global** scope: **218 countries** and **47,328 cities**.
- **Location-based features** allow analysis by **country** and **city**.
- **ISO 3166-1** standard for country codes.

### Temporal Coverage
- From early pandemic onset to a selected timeframe (Feb 1–10, 2020).
- **Timestamped** tweets for time-based analysis (e.g., day of the week, month).

### Languages
- **Multilingual** dataset with tweets in **62 languages**.
- Enables analysis of **regional differences** and **multilingual sentiment**.

### Data Structure
- **Format**: Structured **CSV files** with:
  - `Tweet ID`
  - `Created_at` (timestamp)
  - `User Information` (user ID, user location)
  - `Geo-Location Data` (country, state, city)
  - `Tweet Content` (text, hashtags, mentions)
  - `Country/City Information`
  - `Tweet Count` (aggregations per day/week/month)

### Data Features
- **Temporal**: Date, time, `weekday`, `month`.
- **Geographical**: Country, state, city identifiers.
- **Tweet Metrics**: Count of tweets for given time intervals.
- **Content**: Text for sentiment analysis or topic modeling.

### Data Processing and Preprocessing
- **Standardization**: Timestamp formatting, geolocation matching, aggregated counts.
- **Feature Scaling**: Prepares data for ML analyses (e.g., model training).
- **Aggregation**: Daily or monthly tweet counts.

---

## Analysis Tools
- **Machine Learning Models**: For trend prediction, sentiment analysis, feature importance (SHAP).
- **Geospatial Analysis**: Using **GeoPandas**, **Plotly**, or similar libraries.
- **Time Series Analysis**: Identifying seasonal trends and weekly variations in tweet activity.

---

## Results with Visualization

### 1. Temporal Distribution (SHAP Plot)

![Temporal SHAP Plot](https://github.com/user-attachments/assets/d15ca7c3-4df6-4cb8-aa56-211cbf73fc1f)

This **SHAP** plot (learn more at [SHAP’s documentation](https://shap.readthedocs.io/en/latest/index.html)) demonstrates how **temporal features** (`Is Weekend`, `Weekday`, `Date (Ordinal)`, and `Month`) affect the model’s predicted tweet volume.

1. **Is Weekend**  
   - Higher **positive SHAP values** on weekends, indicating an **increase** in tweet volume.  
   - Suggests weekends are a **significant** driver of higher COVID-19 tweet activity.

2. **Weekday**  
   - Values hover around zero, implying **weekdays** do not strongly influence tweet counts.  
   - Minor positive effects for certain days, but overall **weak** predictive power.

3. **Date (Ordinal)**  
   - SHAP values concentrated near zero, showing **no strong day-specific** trend in tweet volume.  
   - Indicates **no clear** daily progression effect.

4. **Month**  
   - Slight variations around zero; some months show mildly **positive** or **negative** contributions.  
   - Less influential than **Is Weekend** in shaping tweet volume.

**Conclusion**: **Weekends** are most impactful on tweet counts, while weekdays, ordinal dates, and months have notably less effect on COVID-19 tweet volume in this subset.

---

### 2. Global Distribution of Tweets

![Global Tweet Distribution](https://github.com/user-attachments/assets/c7737615-e0fe-4829-a350-25a3f60fc0d6)

A world map visualizing **COVID-19-related tweet volumes**. A color gradient represents tweet counts per country:

- **Darkest shades**: Indicates **highest** tweet counts (e.g., **USA**, **China**).  
- **Medium shades**: Moderately high tweet activity (e.g., **India**, **Brazil**, **Russia**).  
- **Lightest shades**: Very low tweet activity (e.g., certain areas in **Africa**, **Central Asia**).

**Key Observations**:
- **USA & China**: Highest engagement, surpassing **8 million** tweets.
- **Developed regions**: North America, Europe, parts of Asia show robust activity.
- **Global Disparities**: Lower engagement in regions with limited internet access or smaller populations on Twitter.

**Conclusion**: There is a **significant regional variation**, influenced by population, internet penetration, and social media usage, reflecting **global disparities** in pandemic-related discussions.

---

### 3. SHAP Values for Geographical Distribution

![Geographical SHAP Plot](https://github.com/user-attachments/assets/f0fcca17-9345-40c9-8d14-4fefdcebe135)

This SHAP plot reveals how **country codes** (following **ISO 3166-1**) contribute to predicted tweet volume:

- **Color Scale**: Red = **High tweet volume**, Blue = **Low tweet volume**.  
- **USA**: Dominant influence (strongest red), indicating highest impact on predictions.  
- **China (CHN)**: Also significant (red), reflecting large tweet counts.  
- **Spain (ESP), France (FRA), Italy (ITA)**: Moderate-high influence.  
- **Less Active Countries** (e.g., Seychelles (SYC), Lesotho (LSO)): Minimal effect (blue).

**Conclusion**: Large, populous, and social-media-active nations (USA, China) drive the overall global tweet volume prediction. Smaller or less connected countries exhibit lower SHAP values, underscoring **geographical disparities** in COVID-19-related tweeting behavior.

---

## Conclusion
This project provides valuable insights into the temporal and geographical dynamics of COVID-19-related discussions on Twitter during the early stages of the pandemic. By focusing on a concise, ten-day window (February 1–10, 2020), we identified that weekends exhibit a clear spike in tweet volume, whereas weekdays and specific dates show minimal influence. At the same time, geographical disparities emerge as major drivers of tweet activity, with countries like the United States and China dominating overall volume. Through SHAP analyses, we confirmed that both the “weekend” factor and specific high-engagement countries have the strongest impact on predicting tweet counts.

These findings underscore the importance of temporal and spatial features when examining social media data related to global crises. Despite this, there are inherent limitations—including a relatively short time frame and the complexities of early COVID-19 discussions—that must be considered when generalizing results. Future work could leverage longer periods, more granular location data, or advanced machine learning and natural language processing techniques (e.g., sentiment analysis, topic modeling) to provide a deeper understanding of how public discourse evolves during major health emergencies. Ultimately, our results highlight the need for timely, data-driven analyses to inform public health communication strategies and policy decisions on a global scale.

---

## References
- [GeoCoV19 Dataset](https://crisisnlp.qcri.org/covid19)  
- [SHAP Documentation](https://shap.readthedocs.io/en/latest/index.html)  
- [GitHub Large File Limitations](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)  

---

**Thank you** for reading through this project overview. If you have any questions or would like to contribute, please feel free to open an **Issue** or submit a **Pull Request**.
