# Info301_Final
# Research Question

The research focuses on analyzing how COVID-19 related tweets are distributed both temporally and geographically. Specifically, the study aims to:

## 1. Investigate Temporal Trends:
- Examine how tweet frequency varies depending on the day of the week and the month. The analysis will explore whether there is a noticeable increase in tweets on weekends or during specific months, and how these temporal factors impact the overall volume of tweets related to COVID-19.

## 2. Explore Geographical Patterns:
- Analyze how tweet volume varies across different countries and cities. The goal is to understand the geographical distribution of COVID-19 related tweets, identifying regions with the highest levels of tweet activity and comparing trends across different locations.

## 3. Assess the Impact of Features:
- Use advanced techniques like SHAP (SHapley Additive Explanations) to evaluate the contribution of various features, such as weekday, month, and geographic location, to the predicted tweet counts. This step aims to quantify how much each feature influences the model’s predictions and identify which ones are the most significant.

The overall objective is to understand the dynamics behind the volume and distribution of COVID-19 related tweets, shedding light on both time-based and location-based factors that contribute to the spread of information during the pandemic.

# Data

The dataset consists of COVID-19 related tweets collected over a period of time, providing a comprehensive overview of the global conversation around the pandemic. Below is a structured description of the data:

## 1. Data Sources and Collection:
- The data is sourced from **Twitter**, focusing on tweets related to COVID-19, including those containing keywords, hashtags, and mentions related to the virus.
- Tweets were collected using over **800 predefined keywords** and hashtags associated with COVID-19.
- **Geotagging**: The dataset contains both **geotagged tweets** (378K tweets) and tweets with **location data** but without explicit geotags (5.4 million tweets).

## 2. Geographical Coverage:
- The dataset provides a **global perspective**, covering **218 countries** and **47,328 cities**.
- Data includes **location-based features**, allowing for an analysis of tweet distributions by **country** and **city**.
- The **country codes** in the dataset follow the **ISO 3166-1** standards, with countries identified by their respective codes.

## 3. Temporal Coverage:
- The dataset spans a significant period of time, providing a **timeline** of tweets from the onset of the COVID-19 pandemic to the present.
- Tweets are **timestamped**, allowing for an analysis of trends and patterns over time. Temporal features like **day of the week** and **month** are included, enabling researchers to assess tweet activity on different days and months.

## 4. Languages:
- The dataset is **multilingual**, containing tweets in **62 languages**, allowing researchers to analyze global sentiment and regional differences in response to the pandemic.
- The diversity in language makes the dataset suitable for **multilingual sentiment analysis** and understanding regional variations in COVID-19 discussions.

## 5. Data Structure:
The data is organized into structured **CSV files** with key attributes, including:
- **Tweet ID**: A unique identifier for each tweet.
- **Created_at**: Timestamp of when the tweet was posted.
- **User Information**: Includes user ID, and sometimes, user location.
- **Geo-Location Data**: Geographical information about where the tweet originated, including country, state, and city details.
- **Tweet Content**: The textual content of the tweet, which could contain relevant hashtags or mentions.
- **Country/City Information**: The geographical region (country or city) associated with the tweet.
- **Tweet Count**: The number of tweets related to COVID-19 over a specific time period (e.g., per day, week, or month).

## 6. Data Features:
- **Temporal Features**: Date, time of tweet creation, and derived features such as weekday and month.
- **Geographical Features**: Country, state, and city identifiers.
- **Tweet Metrics**: Tweet counts, including the total number of tweets over a specified time period.
- **Content Features**: The text of the tweets, which can be used for sentiment analysis and topic modeling.

## 7. Data Processing and Preprocessing:
- The dataset has undergone **preprocessing** to standardize the data, including timestamp formatting, geolocation matching, and aggregation based on time (e.g., daily or monthly tweet counts).
- Additional processing, such as **feature scaling**, is used to prepare the data for analysis using machine learning techniques.

## 8. Analysis Tools:
The dataset is compatible with various analytical tools, including:
- **Machine Learning Models**: For trend prediction, sentiment analysis, and feature importance analysis (e.g., SHAP values).
- **Geospatial Analysis**: Tools like **Geopandas** and **Plotly** are used to map tweet distributions and identify geographic trends.
- **Time Series Analysis**: Methods to explore temporal patterns in tweet activity, such as seasonal trends and weekly variations.

## 9. Applications:
The dataset is used for a variety of research purposes, including:
- **Trend Analysis**: Understanding how the conversation about COVID-19 evolved over time.
- **Sentiment Analysis**: Analyzing the tone of tweets to gauge public sentiment regarding the pandemic.
- **Geospatial Research**: Investigating regional differences in COVID-19 related tweets and identifying hotspots of activity.
- **Modeling and Prediction**: Developing predictive models to forecast future tweet volumes or track significant events and outbreaks.

## Conclusion:
This dataset offers a rich resource for understanding global conversations around COVID-19 through the lens of Twitter data. Its combination of temporal, geographical, and linguistic diversity provides insights into public sentiment, regional differences, and pandemic-related discussions worldwide. Researchers can utilize this dataset for a wide range of analyses, including trend forecasting, sentiment evaluation, and spatial analysis.

# Result

## Temporal Distribution in SHAP Plot
The SHAP (SHapley Additive Explanations) plot provides a detailed examination of the impact of temporal features on the model’s output, specifically focusing on tweet volume in relation to time. This analysis evaluates the following features: **Is Weekend**, **Weekday**, **Date (Ordinal)**, and **Month**. Each of these features is assessed in terms of its contribution to the predicted tweet volume, with SHAP values representing the feature’s influence on the model.

### 1. Is Weekend:
- **Feature Overview**: The **Is Weekend** feature indicates whether a tweet was posted on a weekend (Saturday or Sunday).
- **SHAP Value Distribution**: The SHAP values for **Is Weekend** show a notable concentration of positive values, denoted by red dots, with some negative values (blue dots).
- **Interpretation**: A positive SHAP value indicates that tweets posted on weekends contribute significantly to an increase in tweet volume. Specifically, the model predicts higher tweet volumes on weekends, suggesting a higher engagement or activity on these days. The presence of red values confirms that weekend tweets have a substantial positive impact on the predicted outcome, while the blue values imply a relatively minor reduction in impact for non-weekend days.

### 2. Weekday:
- **Feature Overview**: The **Weekday** feature categorizes tweets based on the day of the week, with values indicating each weekday (Monday through Friday).
- **SHAP Value Distribution**: The SHAP values for **Weekday** are distributed with a mix of values close to zero, with a slight positive impact observed in some cases (pink) and minimal negative impacts (blue).
- **Interpretation**: The limited spread of SHAP values near zero suggests that **Weekday** does not have a strong influence on tweet volume. The near-zero distribution implies that tweet activity across weekdays is relatively stable, with no significant day-specific spikes or dips observed in the data. While there are some positive contributions for certain weekdays, the impact is not large enough to make weekday a major factor in predicting tweet volume.

### 3. Date (Ordinal):
- **Feature Overview**: The **Date (Ordinal)** feature represents the sequential day of the year, effectively capturing the passage of time as tweets are posted over the months.
- **SHAP Value Distribution**: The SHAP values for **Date (Ordinal)** are concentrated around zero, showing minimal variability in their impact on the model’s predictions.
- **Interpretation**: The lack of significant SHAP values indicates that the specific date within the year does not greatly affect tweet volume. This suggests that there is no clear trend in tweet activity based purely on the passage of days in the year. It highlights the absence of day-specific effects in tweet counts, where tweet volume appears to be more influenced by other factors, such as weekends or external events, rather than by the specific date.

### 4. Month:
- **Feature Overview**: The **Month** feature captures the month of the year in which a tweet was posted, allowing for the analysis of seasonal trends or monthly fluctuations in tweet volume.
- **SHAP Value Distribution**: The SHAP values for **Month** are relatively dispersed, with a small range of positive and negative values observed. Most values are close to zero, but a few extend to positive values.
- **Interpretation**: The **Month** feature shows a weak influence on tweet volume, with small positive SHAP values indicating that certain months may have slightly higher tweet activity, while negative values suggest that other months contribute slightly less to tweet volume. Despite some variation, the overall influence of **Month** is minimal compared to other time-based features like **Is Weekend**.

### Conclusion:
The SHAP analysis reveals that **Is Weekend** has the most pronounced effect on tweet volume, with tweets posted on weekends contributing significantly to higher predicted tweet counts. In contrast, **Weekday** and **Date (Ordinal)** exhibit minimal impact, with tweet volume appearing unaffected by the specific weekday or date within the year. The **Month** feature shows a slight influence, with some months contributing marginally to the increase or decrease in tweet volume. Overall, the data suggests that time-related factors like weekends play a critical role in driving tweet activity, while other temporal aspects (weekdays, dates, and months) have less substantial effects on the overall volume of COVID-19 related tweets.

---

## Global Distribution of Tweets Across Areas
The map shown represents the global distribution of COVID-19 related tweets across different geographical regions. The map visualizes the tweet volume by country, with a color gradient indicating the number of tweets from each country. The intensity of the color corresponds to tweet counts, allowing for a comparative understanding of how tweet activity varies across the world.

### 1. Color Scale Interpretation:
- The **color scale** on the right side of the map indicates the range of tweet counts, from **0 tweets** (lightest color) to **10 million tweets** (darkest color).
- Countries with a **darker shade** (such as the United States and China) have a significantly higher number of COVID-19 related tweets, with tweet counts exceeding 8 million in these areas.
- **Lighter shades** represent countries with lower tweet volumes, indicating less engagement or fewer COVID-19 related discussions.

### 2. Key Observations:
- **United States**: The map shows the **United States** with the highest concentration of tweets, marked by the darkest shade, indicating that it is one of the most active regions in terms of tweet volume related to COVID-19.
- **China**: Similarly, **China** also shows a high number of tweets, reflected by a dark color, indicating significant engagement from users in this region.
- **Other High-Tweet Countries**: Several other countries, including **India**, **Brazil**, and **Russia**, display medium to high tweet counts, represented by shades of brown. These regions also show notable engagement on the topic of COVID-19.
- **Low-Tweet Countries**: Many countries in regions such as **Africa** and **Central Asia** show very light shades, suggesting that tweet volume in these regions is significantly lower compared to others. This could be due to factors such as lower social media penetration, fewer COVID-19 cases, or other regional factors.

### 3. Geographical Patterns:
- The map visually emphasizes how **geographical location** impacts the volume of tweets. Regions with higher population densities and stronger social media engagement, such as **North America** and **Asia**, tend to have higher tweet volumes.
- Developed regions with robust social media infrastructure, such as the **United States** and **Europe**, are well represented on the map, whereas less developed regions show lower tweet counts.
- **Global Disparity**: The map also highlights the disparity in global engagement, with some countries experiencing massive tweet activity and others showing very minimal online discourse regarding COVID-19.

### Conclusion:
The map of global tweet distribution illustrates the significant **regional variation** in COVID-19 related tweet activity. It highlights regions such as the **United States** and **China** with substantial engagement, while other regions, particularly in **Africa** and parts of **Asia**, show lower engagement. This map provides valuable insights into the **geographical influence** on social media activity and the global spread of COVID-19-related discussions.

---

## SHAP Values for Geographical Distribution
The SHAP (SHapley Additive Explanations) plot shown here illustrates the impact of geographical features on the model’s prediction of tweet counts, specifically based on the **country** feature. The countries are represented by their respective **ISO country codes**, and the SHAP values indicate how strongly each country contributes to the model’s predicted tweet volume.

### 1. Color Scale Interpretation:
- The **color scale** on the right side represents the feature values, with **red** indicating high values and **blue** representing low values.
- This color gradient reflects the tweet volume, where countries with **high tweet counts** are marked by red and **low tweet counts** are marked by blue.

### 2. Key Observations:
- **USA (United States)**: The **USA** has the highest SHAP value, marked with a red color. This indicates that the United States contributes significantly to the overall tweet volume, as the model strongly associates this region with higher tweet activity.
- **China (CHN)**: **China** also shows a high SHAP value, though slightly lower than the USA, indicating that China is another major contributor to tweet counts. The color remains in the red spectrum, signaling substantial engagement.
- **Other High-Tweet Countries**: Countries such as **Spain (ESP)**, **France (FRA)**, and **Italy (ITA)** also show moderate to high SHAP values, marked in varying shades of pink, indicating a noteworthy contribution to the overall tweet volume prediction.
- **Low-Tweet Countries**: On the lower end of the SHAP value scale, countries like **Seychelles (SYC)**, **Lesotho (LSO)**, and **Tokelau (TKL)** exhibit much lower SHAP values. These countries have minimal tweet volumes, as indicated by the **blue** coloring, signifying their relatively insignificant impact on the model’s overall predictions.

### 3. Geographical Influence:
- The SHAP values clearly show that countries with higher population densities and more active social media usage, such as the **United States**, **China**, and **Spain**, significantly influence the total volume of tweets. These countries have stronger positive contributions to the prediction.
- In contrast, smaller nations or those with fewer social media interactions, such as **Seychelles** and **Lesotho**, have minimal impact on the model, contributing relatively fewer tweets.

### 4. Overall Distribution:
- The chart illustrates a clear **geographical disparity** in tweet volume, with **North America**, **Europe**, and **Asia** being the regions most strongly represented. These regions are marked by the highest SHAP values and contribute significantly to the global tweet count.
- Conversely, countries from **Africa** and small island nations show less tweet activity, as reflected in their lower SHAP values.

### Conclusion:
This SHAP plot provides an insightful representation of how **geographical location** influences tweet volume. It highlights the dominance of large, highly connected countries such as the **USA** and **China** in driving the model’s predictions for tweet volume. Smaller or less active countries, represented by lower SHAP values, contribute less to the overall prediction, reflecting global disparities in tweet activity related to COVID-19.
