# Airbnb Data Analysis and Visualization

# Airbnb Analysis Project

## Project Overview

This project involves the analysis of Airbnb data using MongoDB Atlas for data retrieval. The analysis includes data cleaning and preparation, development of an interactive streamlit web application for geospatial visualizations, and dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.

## Skills Developed

- **Python Scripting**: Utilized for data retrieval, cleaning, and analysis.
- **Data Preprocessing**: Addressed missing values, duplicates, and data type conversions.
- **Visualization**: Used Streamlit for interactive visualizations, and Plotly and Plotly Express for dynamic plots.
- **MongoDB**: Employed MongoDB Atlas for efficient data storage and retrieval.
- **Tableau**: Created a comprehensive dashboard for data presentation.

## Problem Statement and Objectives

The main objectives of the project are:

1. Establish a MongoDB connection, retrieve the Airbnb dataset, and ensure efficient data retrieval for analysis.
2. Clean and prepare the dataset, addressing missing values, duplicates, and data type conversions for accurate analysis.
3. Develop a streamlit web application with interactive maps showcasing the distribution of Airbnb listings, allowing users to explore prices, ratings, and other relevant factors.
4. Conduct price analysis and visualization, exploring variations based on location, property type, and seasons using dynamic plots and charts.
5. Analyze availability patterns across seasons, visualizing occupancy rates and demand fluctuations using suitable visualizations.
6. Investigate location-based insights by extracting and visualizing data for specific regions or neighborhoods.
7. Create interactive visualizations that enable users to filter and drill down into the data.
8. Build a comprehensive dashboard using Tableau or Power BI, combining various visualizations to present key insights from the analysis.


Certainly! Here are steps you can include in your README file to guide users on how to set up and run your project:

---

# Working of the Project

To run and explore the Airbnb Analysis project follow these steps:

## Prerequisites

1. **MongoDB Atlas Account**: Sign up for a MongoDB Atlas account by visiting the [MongoDB Atlas website](https://www.mongodb.com/cloud/atlas) and follow the registration process to set up your account and create a new project.

2. **Python Installation**: Ensure you have Python installed on your machine. You can download and install Python from the [official Python website](https://www.python.org/downloads/).

3. **Modules Installation**: Install **Streamlit**, **Pandas**, **Plotly** using the following command in your terminal or command prompt:

    ```bash
     pip install streamlit pandas plotly
     ```

4. **Tableau or Power BI**: Install either Tableau or Power BI for dashboard creation. You can download Tableau from the [Tableau website](https://www.tableau.com/) and Power BI from the [Power BI website](https://powerbi.microsoft.com/).

## Setting Up the Project

1. **Create a MongoDB Atlas Cluster**: Within your MongoDB Atlas project, set up a cluster. Choose the cloud provider and region for hosting your data, configure the cluster specifications, and create the cluster. This will serve as the database environment for storing the sample data.

2. **Load the Airbnb Sample Data**: Once your cluster is set up, access the MongoDB Atlas dashboard. In the left-hand navigation menu, click on "Database Access" to create a database user with appropriate permissions for accessing and loading data. Then, select "Network Access" to set up IP whitelisting or configure other security measures.

3. **Import Sample Data**: From the MongoDB Atlas dashboard, navigate to the "Clusters" page and click on your cluster. In the cluster view, select the "Collections" tab and click on the "Sample Data" button. Choose the "Load Sample Dataset" option, and MongoDB Atlas will import the Airbnb sample data into your cluster. The sample data typically includes collection for listings and reviews.

4. **Retrive and Clean Data**: Using python script retrive the data, convert it into pandas dataframe, clean the data, change data types, fill missing values.

5. **Convert to CSV**: Convert the cleaned dataframe to CSV format for further usage.

6. **Streamlit**: Create a web application to visualise the data.

7. **Explore the Insights**: Use the interactive Streamlit interface to explore insights from the Airbnb dataset, including geospatial visualizations, price analysis, and availability patterns.

8. **Tableau**: [Airbnb Data Analysis Dashboard](https://public.tableau.com/views/AirbnbDataAnalysisandVisualizationDashboard/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link) to explore comprehensive visualizations and key insights.

