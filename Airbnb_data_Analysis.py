import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go


## SETTING UP PAGE CONFIGURATION
st.set_page_config(page_title= "Airbnb Data Analysis",
                   page_icon= Image.open("icon.png"),
                   layout= "wide",
                   initial_sidebar_state= "collapsed"
                   )

## TITLE IMAGE
st.image("title.png")

## CREATING SIDEBAR
with st.sidebar:
    Sidebar_Option = st.radio(
                        "Menu", 
                        ["***Home***","***Overview***","***Insights***"])

## HOME PAGE

if Sidebar_Option == "***Home***":
    
    col1,col2 = st.columns([4,2])
    
    with col1: 
        st.title("Exploring Airbnb Data Analysis")
        st.write("Welcome to our interactive web application dedicated to exploring and analyzing Airbnb data! Whether you're a traveler seeking insights into accommodation options or a data enthusiast fascinated by trends, this platform is designed for you. Discover the world of Airbnb and learn about its transformative impact on the travel industry. Get insights into how the platform connects hosts and guests, providing unique and personalized lodging experiences.")
        st.write("Explore raw data and customize your view with filters. Gain a deeper understanding of Airbnb listings based on criteria such as country, property type, room type, and price.")
        st.write("Dive into detailed insights derived from the Airbnb dataset:")
        st.write(" - Discover the top 10 property types and hosts based on the number of listings.")
        st.write(" - Visualize the distribution of listings across different room types and countries.")
        st.write(" - Explore average prices in countries through scattergeo and pie chart visualizations.")
        st.write(" - Compare average prices based on room types.")
        st.write(" - Identify the highest-priced listings and analyze their review scores.")
        st.write(" - Examine average availability in countries using a scattergeo plot.")
        st.write(" - Investigate availability across room types through box plots and violin plots.")
        st.write(" - Whether you're curious about Airbnb trends, planning your next trip, or just intrigued by data, this web application provides a rich and interactive experience for your exploration. Enjoy your journey into the world of Airbnb data analysis! 🌍🏡📊")
                 
                 
    with col2:
        st.subheader("What is Airbnb?")
        st.write("Airbnb is a popular online marketplace and hospitality service that enables people to list, discover, and book accommodations around the world. The platform connects hosts (individuals or property owners) who have available space, whether it's a room, apartment, or entire house, with travelers seeking temporary lodging. Airbnb provides a platform for these connections, facilitating the booking process and ensuring a secure and trusted environment for both hosts and guests.")
        st.write("Overall, Airbnb has transformed the way people travel by offering alternatives to traditional hotels and providing unique and personalized lodging experiences. The platform has gained widespread popularity since its founding in 2008 and has become a significant player in the sharing economy.")


## ANALYSIS OF DATA

# READING THE CLEANED DATAFRAME
df = pd.read_csv('Airbnb_data.csv')

# GETTING USER INPUTS
price = st.sidebar.slider('Select Price',df.Price.min(),df.Price.max(),(df.Price.min(),df.Price.max()))
country = st.sidebar.multiselect('Select a Country',sorted(df.Country.unique()),sorted(df.Country.unique()))
property = st.sidebar.multiselect('Select Property_type',sorted(df.Property_type.unique()),sorted(df.Property_type.unique()))
room = st.sidebar.multiselect('Select Room_type',sorted(df.Room_type.unique()),sorted(df.Room_type.unique()))

# CONVERTING THE USER INPUT INTO QUERY
query = f'Country in {country} & Room_type in {room} & Property_type in {property} & Price >= {price[0]} & Price <= {price[1]}'
        

## OVERVIEW PAGE

if Sidebar_Option == "***Overview***":

    st.subheader("Raw Data")
    st.write(df.query(query))
 

## EXPLORE PAGE

if Sidebar_Option == "***Insights***":

    st.header("Explore more about the Airbnb data")

    tab1, tab2, tab3 = st.tabs(["Top Insights", "Price Analysis", "Availability Analysis"])
    
    with tab1:


        ## 1) TOP 10 PROPERTY TYPES BAR CHART
        col1,col2 = st.columns([4,1])

        with col1:
            
            st.subheader("Top 10 Property Types")
            st.text("based on no.of listings")

            df1 = df.query(query).groupby(["Property_type"]).size().reset_index(name="Listings").sort_values(by='Listings',ascending=False)[:10]
            fig = px.bar(df1,
                            x='Listings',
                            y='Property_type',
                            orientation='h',
                            color='Property_type',
                            color_continuous_scale=px.colors.sequential.Agsunset)
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig,use_container_width=True) 
        
        with col2:
            # BLANK SPACE
            st.markdown("#   ")
            st.markdown("#   ")
            st.markdown("#   ")
            # DISPLAYING DATAFRAME BASED ON USER INPUT
            st.dataframe(df1, hide_index=True)


        ## 2) TOP 10 HOSTS BAR CHART
        col1,col2 = st.columns([4,1])

        with col1:

            st.subheader("Top 10 Hosts")
            st.text("based on no.of listings")
            
            df2 = df.query(query).groupby(["Host_name"]).size().reset_index(name="Listings").sort_values(by='Listings',ascending=False)[:10]
            fig = px.bar(df2,
                            y='Listings',
                            x='Host_name',
                            orientation='v',
                            color='Host_name',
                            color_continuous_scale=px.colors.sequential.Agsunset)
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig,use_container_width=True)

        with col2:
            # BLANK SPACE
            st.markdown("#   ")
            st.markdown("#   ")
            st.markdown("#   ")
            # DISPLAYING DATAFRAME BASED ON USER INPUT
            st.dataframe(df2, hide_index=True)

        
        ## 3) TOTAL LISTINGS IN EACH ROOM TYPES PIE CHART
        col1,col2 = st.columns([4,1])

        with col1:

            st.subheader("Total number of Listings based on Room Types")

            df3 = df.query(query).groupby(["Room_type"]).size().reset_index(name="counts")
            fig = px.pie(df3,
                            names='Room_type',
                            values='counts',
                            color_discrete_sequence=px.colors.sequential.Agsunset
                        )
            fig.update_layout(showlegend=False)
            fig.update_layout(height=500, width=700)
            fig.update_traces(textposition='outside', textinfo='value+label')
            st.plotly_chart(fig,use_container_width=True)
        
        with col2:
            # BLANK SPACE
            st.markdown("#   ")
            st.markdown("#   ")
            st.markdown("#   ")
            # DISPLAYING DATAFRAME BASED ON USER INPUT
            st.dataframe(df3, hide_index=True)


        ## 4) TOTAL LISTINGS BY COUNTRY LINE CHART
        col1,col2 = st.columns([4,1])

        with col1:
            
            st.subheader("Total number of Listings Country wise")

            country_df = df.query(query).groupby(['Country'], as_index=False)['Name'].count().rename(columns={'Name': 'Total_Listings'})
            
            fig_line_chart = px.line(country_df,
                                    x='Country',
                                    y='Total_Listings',
                                    markers=True,
                                    labels={'Total_Listings': 'Number of Listings'})
            fig_line_chart.update_layout(xaxis_title='Country', yaxis_title='Number of Listings')
            st.plotly_chart(fig_line_chart, use_container_width=True)
        
        with col2:
            # BLANK SPACE
            st.markdown("#   ")
            st.markdown("#   ")
            st.markdown("#   ")
            # DISPLAYING DATAFRAME BASED ON USER INPUT
            st.dataframe(country_df, hide_index=True)
        

        ## 5) TOTAL LISTINGS BY COUNTRY CHOROPLETH MAP
        fig = px.choropleth(country_df,
                            locations='Country',
                            locationmode='country names',
                            color='Total_Listings',
                            color_continuous_scale=px.colors.sequential.Agsunset,
                            hover_name='Country')
        # Add bubbles using scatter_geo
        scatter_geo_df = df.query(query).groupby(['Country'], as_index=False)['Name'].count().rename(columns={'Name': 'Total_Listings'})
        scatter_fig = px.scatter_geo(scatter_geo_df,
                                    locations='Country',
                                    locationmode='country names',
                                    size='Total_Listings',
                                    projection='natural earth',
                                    title='Bubble Size Represents Total Listings')
        # Combine choropleth and bubble plots
        fig.add_trace(scatter_fig.data[0])
        st.plotly_chart(fig, use_container_width=True)
    

        ## 6) REVIEW SCORES BASED ON ROOM TYPES
        st.subheader("Analysis of review scores based on Room types")
        # Apply the filter to the DataFrame
        filtered_df = df.query(query)
        # Calculate mean and sum of review scores for each room type
        mean_reviews_df = filtered_df.groupby('Room_type', as_index=False)['Review_scores'].mean().sort_values(by='Review_scores')
        sum_reviews_df = filtered_df.groupby('Room_type', as_index=False)['Review_scores'].sum().sort_values(by='Review_scores')
        # Create subplots with shared y-axis
        fig = sp.make_subplots(rows=1, cols=2, subplot_titles=['Mean Review Scores', 'Sum Review Scores'])
        # Add traces to the subplots
        fig.add_trace(go.Bar(x=mean_reviews_df['Room_type'], y=mean_reviews_df['Review_scores'], marker_color=mean_reviews_df['Review_scores'], showlegend=False), row=1, col=1)
        fig.add_trace(go.Bar(x=sum_reviews_df['Room_type'], y=sum_reviews_df['Review_scores'], marker_color=sum_reviews_df['Review_scores'], showlegend=False), row=1, col=2)
        # Update layout for better visualization
        fig.update_layout(height=600, showlegend=False, width=1200)  # Set the width to make it full-width
        # Show the plot
        st.plotly_chart(fig)


    with tab2:
        # PRICE ANALYSIS
        st.header("Price Analysis")
        col1,col2 = st.columns([3,2])
        country_df1 = df.query(query).groupby('Country',as_index=False)['Price'].mean()

        ## 7) AVG PRICE IN COUNTRIES SCATTERGEO
        with col1:

            st.subheader("Average Price Country wise")

            fig = px.scatter_geo(data_frame=country_df1,
                                            locations='Country',
                                            color= 'Price', 
                                            hover_data=['Price'],
                                            locationmode='country names',
                                            size='Price',
                                            color_continuous_scale='agsunset')
            st.plotly_chart(fig,use_container_width=True)
            
        ## 8) AVG PRICE IN COUNTRIES PIECHART
        with col2:

            # BLANK SPACE
            st.markdown("#   ")
            st.markdown("#   ")

            fig = px.pie(country_df1,
                        values='Price',
                        names='Country',
                        labels={'Price': 'Average Price', 'Country': 'Country'},
                        hover_name='Country')
            
            fig.update_layout(height=400, width=500)
            fig.update_traces(marker=dict(colors=px.colors.sequential.Agsunset))  # Use Agsunset color scale
            st.plotly_chart(fig)

        col1, col2 = st.columns(2)

        ## 9) AVERAGE PRICE BASED ON ROOM TYPE
        with col1:
            
            st.subheader("Average Price based on Room Type")

            pr_df = df.query(query).groupby('Room_type',as_index=False)['Price'].mean().sort_values(by='Price')
            fig = px.bar(data_frame=pr_df,
                            x='Room_type',
                            y='Price',
                            color='Price'
                        )
            st.plotly_chart(fig,use_container_width=True)

        ## 10) HIGH PRICED LISTINGS AND ITS REVIEW SCORES
        with col2:

            # Get the highest-priced listings
            highest_priced_listings = df.query(query).nlargest(10, 'Price')

            # Scatter plot of highest-priced listings and their review scores
            st.subheader("Highest Priced Listings and Their Review Scores")
            fig = px.scatter(highest_priced_listings,
                            x='Review_scores',
                            y='Price',
                            color='Price',
                            size='Review_scores',
                            hover_data=['Property_type', 'Host_name'],
                            labels={'Review_scores': 'Review Scores', 'Price': 'Price'},
                            color_continuous_scale='agsunset')
            st.plotly_chart(fig, use_container_width=True)


    with tab3:
        
        ## 11) AVG AVAILABILITY IN COUNTRIES SCATTERGEO
        country_df2 = df.query(query).groupby('Country',as_index=False)['Availability_365'].mean()
        country_df2.Availability_365 = country_df2.Availability_365.astype(int)
        st.subheader("Availability by Country")

        fig = px.scatter_geo(data_frame=country_df2,
                                        locations='Country',
                                        color= 'Availability_365', 
                                        hover_data=['Availability_365'],
                                        locationmode='country names',
                                        size='Availability_365',
                                        color_continuous_scale='agsunset'
                            )
        st.plotly_chart(fig,use_container_width=True)


        ## 12) AVAILABILITY BY ROOM TYPE BOX PLOT
        st.subheader("Availability by Room Type")
        fig = px.box(data_frame=df.query(query),
                        x='Room_type',
                        y='Availability_365',
                        color='Room_type',
                    )
        st.plotly_chart(fig,use_container_width=True)


        filtered_df = df.query(query)

        ## 13) AVAILABILITY BASED ON PROPERTY TYPE
        st.subheader("Availability by Property Type")
        fig_violin_plot = px.violin(filtered_df,
                                    x='Property_type',
                                    y='Availability_365',
                                    color='Property_type',
                                    box=True,  # Display box plot inside the violin
                                    points="all",  # Show individual data points
                                    )
        fig_violin_plot.update_layout(xaxis_title='Property Type', yaxis_title='Availability (in days)')

        st.plotly_chart(fig_violin_plot, use_container_width=True)
    