# project-1
# Findings and Conclusions
> > - Climate Change Impact: Rising ocean temperatures and sea levels are leading to more hurricanes and coastal flooding, particularly in the Gulf Coast and Southeast U.S., while the western regions are seeing more wildfires.

> > ![pie_chart_damage_by_event_type](https://github.com/user-attachments/assets/d5ccfdb6-c475-4645-9a74-908326acae7d)

> > ![global sea levels](https://github.com/user-attachments/assets/43def44c-37d4-4759-935a-5abba976a91b)

> > ![severe storms](https://github.com/user-attachments/assets/0b40394f-b65a-4e92-bc66-55aa4b621e50)

> > - Death Rate Trends: Although natural hazards are on the rise, improved forecasting and emergency response have helped lower death rates, especially for hurricanes.

> >   ![scatter_plot_linear_reg_deaths](https://github.com/user-attachments/assets/408774f7-5aa2-4d25-aba3-ecbb18160a14)

> > - High-Risk Regions: Areas like the Gulf Coast, Southeast, and parts of California are particularly vulnerable to climate-related hazards.

> > ![high risk areas](https://github.com/user-attachments/assets/a98713de-8109-41c4-a2c7-4e22cb51149a)

> > ![fema map](https://github.com/user-attachments/assets/ccd0fb62-6a5b-49ce-aacc-b815a23baf53)

> > - Policy Needs: There’s a need for climate-resilient policies that integrate risk into planning and emergency management.
> > - FEMA Fund Allocations: FEMA declaration of natural disasters has gone up from 2004 to 2024; which does show that the government is increasing the frequency of disaster declaration that require funding.  But, the funding from 2020 to 2024 has actually gone down.  After some research, it was found that this is likely due to federal government disaster relief funds were depleted during COVID and are still being replenished

> >

> > - Disaster Response: Investment in forecasting, public education, and preparedness is essential for effective disaster response.
> > - Future Research: Further research is critical to understand how climate change influences hazards and to find the best ways to protect communities.
> > - Misleading Data Findings: when a 20 year period is captured (2004 to 2024), air temperatures and ocean temperatures do actually trend downward as expected.  However, when we zoom in onto a 10 year period (2044, 2024), air temperatures and ocean temperatures actually trend downward.  We tried several different datasets like NASA and NOAA to confirm from multiple sources this was the case.  We researched this phenomenon and discovered that the data NOAA captured of these temperatures can be and is skewed by air current shifts, El Nino and La Nina, and during some natural ocean current changes, heat is sometimes distributed to deeper sections of the ocean which decreases the surface temperature of the ocean while not reducing the overall ocean temperature (measurements are taken at the surface)

> >   ![natural hazards](https://github.com/user-attachments/assets/f4de4076-371d-4d12-a4c3-262b54a0bdd6)

# Files in this Repository and Their Functions
> ##  <ins>project_1_main.ipynb</ins> - Written by Daniel Grimm 
> > - this file is the main code for the project.  It combines data from multiple data sources (APIs and CSVs) and creates plots for correlation
> > - It reads the contents of CSV files from the NCDC NOAA website which contain Natural Disaster Data.  This code filters it down to Year, Deaths, Property Damage, the Hurricane, Wildfire, Winter STorm, Tornado, and Flood event types to narrow our band of data capture
> > - The code then cleans the data by totalling deaths and damage per State per Event Type, and formats the Damage column which is in string format in the CSV files, offloads it, and exports it in CSV format
> > - Then, it creates the below plots, displays them, and saves them to image files in the Plot Images folder to compare and correlate data
> > > - bar plot of total property damage per state
> > > - heat map of property damage by event type and year
> > > - Two pie charts showing property damage and deaths per event type
> > > - Stacked Bar Chart showing property damage per event ype
> > > - Line plot showing deaths and property damage amounts over time
> > > - scatter plot of property damage over time with linear regression line
> > > - scatter plot of deaths over time with linear regression line
> > - Then, this code readsd the CSV file created by the ocean_temps.ipynb file, gets the mean per year of these temperatures, and then combines into a dataframe with the previously-collected data
> > - A line plot showing these three datasets (deaths per year, property damage per year, and average ocean temperatures per year) is created
> > - Then, the CSV file created by the air_temps.ipynb file is read, the mean per year of air temperatures is collected, and then it is combined into a dataframe with previous combination data
> > - Then, 4 scatter plots with regression lines for deaths, property damage, ocean temps, and air temps are plotted and saved
> > - The year 2023 was an outlier year, so this code captures the data and plots it on a bar plot
> > - Then, the CSV file created by the oct29,ipynb which contains FEMA disaster data is read, filtered down to date, event type, and obligatedTotalAmounts, the date field is cleaned to match the date format in the previous dataframes, and then this data is combined into one master dataframe
> > - Four scatter plots with regression lines comparing these 4 datasets are plotted and saved
> ## <ins>oct29.ipynb</ins> - Written by Maha Pentakota
> > - this file accesses Version 2 of the API at the FEMA website whicih displays dollar amounts granted by FEMA for disaster relief per state and per year
> > - This information is converted into a dataframe
> > - summary data (mean, median, quartiles, min, max, etc.) are displayed for analysis
> > - This dataframe is written to a CSV file to be called and used in the project_1_main.ipynb file
> > - this dataframe is merged with a Geodata frame so that we can plot disasters on the map later
> > - plots of disaster declarations, proportion of incident types, and a heatmap of incident type are created, displayed, and offloaded
> ## <ins>ocean_temps.ipynb</ins> - Written by Janet Rodriguez
> > - this file accesses the API at NCEI NOAA which captures ocean temperatures on a daily interval
> > - Parameters narrowing this information down to United States data are added
> > - a Line plot of these temperatures per year is generted and saved
> > - A scatter plot with linear regression is plotted
> > - a pie chart of temperature range proportion
> > - a pie chart showing yearly temperature change
> > - a line plot showing yearly temperature percentage change
> > - a scatter plot with linear regression of the yearly temperature percentage change
> ## <ins>air_temps.ipynb</ins> - Written by Sapir Coulson
> > - this calls on the same NCEI NOAA API but references average air temperature readings over a 2014 through 2024 timeframe very similar to the file above
> > - The CSV that this code creates is called in the project_1_main.ipynb file
> ## <ins>GMSL_TPJAOS_5.1</ins> - Created by Sapir Coulson
> > - this is a CSV file that was converted from an HTML file obtained from the NASA website.  This dataset tracks the rising levels of the oceans
> > - NASA only stores this information in HTML format so Sapir converted this to a readable CSV format
> > - Ana Garcia uses this information in her code to combine with the data retrieved from the Version 1 API at the FEMA website
> ## <ins>SeaLevels.ipynb</ins> - Written by Sapir Coulson
> > - This file accesses the CSV file created above from HTML data captured from the NASA website and reads it into the dataframe
> > - This dataframe captures the change delta in ocean levels as GMSL (Global Mean Sea Level) and GIA (Glacial isostatic adjustment) and the date code these temperatures are captured
> > - The code cleans the data in this dataframe by formatting the date, and then visualizes the data on a line chart to look at the trend of temperature change over time
> ## <ins>SevereStorm.ipynb</ins> - Written by Ana Garcia
> > - This file accesses the FEMA version 1 API to capture natural disaster data and the dollar amounts that FEMA allocated funds to and the amounts over time / per year
> > - The data is very messy and very comprehensive in the API, so it is filtered down in this code to pertinent columns, date column converted to date format, etc.
> > - Then, other indeces of the API are accessed to combine and add these data columns to the dataframe to get a complete snapshot of the data
> > - Once all the data we care about is captured in a dataframe, the below visualizations are created:
> > > - Bar chart for number of severe storm declarations
> > > - Heat map of Incidents by Year and Storm Event type
> > > - A choropleth map showing these disasters by State in a United States overlay
> > > - A line plot showing annual obligated amounts that FEMA allocated
# RESOURCES
> Weather.gov Open Source Repository - https://weather-gov.github.io<br>
> World Bank Data Support- https://datahelpdesk.worldbank.org<br>
> National Weather Service (NOAA)- https://www.weather.gov/<br>
> FloodSmart NFIP Services- https://nfipservices.floodsmart.gov/<br>
> FEMA – Emergency Preparedness and Disaster Relief- https://www.fema.gov/<br>
> NSC Injury Facts and Statistics- https://injuryfacts.nsc.org/<br>
> Meteomatics Weather Data Services- https://www.meteomatics.com/<br>
> USGS – Geological and Natural Hazard Data- https://www.usgs.gov/<br>
> NASA Earthdata for Global Observations- https://earthdata.nasa.gov/<br>
> NASA APIs for Space and Earth Data- https://api.nasa.gov/<br>
> NASA Climate Change and Global Warming Insights- https://climate.nasa.gov/<br>
> NOAA NCDC – Environmental Data Archive- https://www.ncdc.noaa.gov/<br>
# DATA RESOURCES
> EMA Web Disaster Summaries API - https://www.fema.gov/api/open/v1/FemaWebDisasterSummaries<br>
> FEMA Disaster Declarations Summaries API -  https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries<br>
> NOAA Storm Events FTP Data - https://www.ncdc.noaa.gov/stormevents/ftp.jsp<br>
> NOAA National Centers for Environmental Information API - https://www.ncei.noaa.gov/cdo-web/api/v2/data<br>
> NASA Vital Signs: Sea Level (HTTP)- https://climate.nasa.gov/vital-signs/sea-level/?intent=121<br>
