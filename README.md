# Player_Price_Prediction_and_Web_Scraping

## Documentation
- [Report](Report.pdf)

## Summary
Within the scope of the given project, information about Super League football players will be obtained through web scraping from the Mackolik website. While the old version of the Mackolik website contains market values of players for different years, the new version includes statistical data for each year and each player. The task is to determine consecutive two years containing the players' market values and extract relevant information from the statistical data in between these years, such as position, height, weight, interception rate, playing time, goal count, etc. Approximately 10 to 15 pieces of information will be used for each football player, and these will be transformed into a final table.

#### Main Hypothesis and Research Questions:

The market values of football players change based on their performances each year. Within a season, a player's statistics evolve after every match. The underlying idea is to enable players or managers to make assumptions about potential increases or decreases in market value when a player maintains a consistent performance level throughout a season.

#### Methods:
Once the dataset is constructed as a table, each football player will be assigned a label indicating whether their prices have increased or decreased over the seasons. Various supervised learning methods will be applied, and performance metrics will be analyzed. The decision has been made to use predictive algorithms such as Naïve Bayes, Decision Trees, Random Forest, K-Nearest Neighbors (KNN), and Gradient Boosting. By applying these methods, the aim is to predict the trends of football players' future market values based on performance statistics and assess the effectiveness of each model.

# Project Dataset Preparation

Here is a detailed overview of the steps involved in creating the project dataset.

### Obtaining Raw Data from the Internet

- The market values of both current and former Super League players are extracted using web scraping from the old Mackolik website.
- A function named `player_market_value` is created to fetch players' market values.
- The variable `url` represents the URL of the web page containing players' market value data.
- A loop is used to send requests and perform operations for each page.
- HTML content is parsed using BeautifulSoup.
- Table data is located, and rows are extracted.
- For each row, a detailed player page is accessed, and data is collected in a dictionary.
- The data is stored in the "result" dictionary and written to a CSV file named "player_price_data.csv."

### Collecting URLs for Player Statistics by Year

- HTML content is fetched and parsed using BeautifulSoup to obtain URLs containing player statistics based on years.

### Saving API Information for Retrieved URLs

- Lists of different years' players are combined to create a "temp" list.
- Data is read from a CSV file, and URLs are assigned to the "readed_urls" list.
- A list of URLs not present in the "readed_urls" list is obtained.
- A proxy is configured using Browsermob-proxy and Chrome driver.
- For each URL, player details and API URLs are extracted and added to the "result" dictionary.
- A CSV file named "players_url_api_all.csv" is created.

### Collecting All Available Data Using Combined Player-Full Name, Stat URL, and URL-Specific API Information

- Necessary libraries are imported.
- Functions are defined to extract and organize data from HTTP responses and APIs.
- Player URLs and API URLs are read from a CSV file.
- Data is fetched for each player and written to a CSV file named "player_statistics.csv."

### Manually Filling Missing Data in the Final Raw Data Table

- Missing market values are manually researched and filled.

### Organizing Data into a Single Table

- Initial table with players and features is used. Some players are excluded due to insufficient data.
- Features are analyzed, reduced, and filled as needed.
- Related features are processed to create more meaningful representations.
- String values are converted to numerical values.

### Additional Steps

- Labels, positions, and foot features are transformed into integer values for analysis.

These steps collectively contribute to the creation of a structured dataset, which can be utilized for further analysis and modeling in the project.


## Creation of Predictive Models:

Cross-validation was employed to obtain 10-fold cross-validation results.

The following algorithms were utilized as predictive models in the project:

1. Naive Bayesian Algorithm
2. K-Nearest Neighbors (KNN)
3. Decision Tree
4. Random Forests
5. Gradient Boosting

## Normalization and Feature Transformation:

The min-max scaling technique was used for normalization. While the standard scaling technique was attempted for some features, it was not preferred. For feature transformation, Principal Component Analysis (PCA) was employed. The number of components for PCA was determined through trial and error, selecting the best-performing configuration.


### Collaboration
Collaborated with [Alperen Ölçer](https://github.com/Alperenlcr)
