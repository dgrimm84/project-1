# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from pprint import pprint
import json
from scipy.stats import linregress
import scipy.stats as st

#url = "https://www.fema.gov/api/open/v4/HazardMitigationAssistanceMitigatedProperties"

#url = "https://www.fema.gov/api/open/v1/FemaWebDeclarationAreas"
url ="https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
ds_response = requests.get(url).json()
# Make the GET request and parse the JSON response
try:
    ds_response = requests.get(url)
    ds_response.raise_for_status()  # Raises an error for bad responses (4xx, 5xx)
    data = ds_response.json()  # Parse JSON response

    # Example of how to use the data
    print(data)  # Print the raw data

    # If you know the structure of the data, you can access it directly
    if isinstance(data, dict):
        # For example, if data is a dictionary
        print(data.keys())  # Print keys in the dictionary
    elif isinstance(data, list):
        # If data is a list, you might want to iterate over it
        for item in data:
            print(item)  # Print each item in the list

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")