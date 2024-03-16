import requests
from bs4 import BeautifulSoup
import pandas as pd

# Enter search crieria onto Foxton's page to get 
URL = "https://www.foxtons.co.uk/flats-to-rent/e2/2-bedroom?expand=2.25&travel_%7Bn%7D_mode=public_transport&travel_%7Bn%7D_travel_time=45&order_by=price_asc&price_to=450"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
unwanted = soup.find("div", {'id':"expanded_search"}) # find unwanted searh results
unwanted.extract() # extract unwanted searh results

# A broad category of information about flats
results_list = soup.find_all("div", attrs={'class':"property_summary"})

# Name/ label of the flat
flat_name = soup.find_all(name="span", attrs={'itemprop':"name"})
# Rent
rent = soup.find_all(name="span", attrs={'class':"month"})

# Empty df to save results of loop
flats_df = pd.DataFrame()

for i in range(len(flat_name)):
    link = results_list[i].select('a[href]')
    link_full = f"https://www.foxtons.co.uk{link[0]['href']}"
    # Assign to df
    flats_df.at[i, "name"] = flat_name[i].text
    flats_df.at[i, "rent"] = rent[i].text
    flats_df.at[i, "link"] = link_full

print(flats_df)

flats_df.to_excel("potential_flats.xlsx")