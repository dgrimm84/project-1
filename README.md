# project-1
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
> 
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
