
#web scrapping from the flipkart
import pandas as pd
import requests
from bs4 import BeautifulSoup
product_name=[]
prices=[]
description =[]
Reviews=[]

url="https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.price_range.from%3D30000&p%5B%5D=facets.price_range.to%3DMax"
r=requests.get(url)             #for sending the request to flipkart
print(r)
soup=BeautifulSoup(r.text,"lxml") #for pharseing the html code
#print(soup)


#printing the name of products
names=soup.find_all("div",class_="_4rR01T")   #still it has many html syntax
#print(names)

for i in names:
    name=i.text
    product_name.append(name)

#print(product_name)    #for listing only the name by eliminating the html syntax
#print(len(product_name))

price=soup.find_all("div",class_="_30jeq3 _1_WHN1")
for i in price:
    name=i.text
    prices.append(name)
#print("\n prices of product is:",prices,"\n\nlength of price list",len(prices))

#extracting the description
desc=soup.find_all("ul",class_="_1xgFaf")
for i in desc:
    name=i.text
    description.append(name)
#print("description of product is",description)
#print("length of description is:",len(description))

import pandas as pd

# Assuming you have the lists 'product_name', 'prices', and 'description' with the extracted data

# Check the lengths of the lists
if len(product_name) == len(prices) == len(description):
    # Create a DataFrame with three columns
    df = pd.DataFrame({
        "Product Name": product_name,
        "Prices": prices,
        "Description": description
    })
    print(df)
else:
    print("Error: The lengths of the lists are not the same.")

df.to_csv("G:/ALOK/ZINE/web scrapping/web_scrapping.csv")
