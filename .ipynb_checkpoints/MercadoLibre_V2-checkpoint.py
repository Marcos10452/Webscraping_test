#!/usr/bin/env python
# coding: utf-8

# In[192]:


#Selenium is a web testing library. It is used to automate browser activities.
from selenium import webdriver
#Beautiful Soup is a Python package for parsing HTML and XML documents. 
#It creates parse trees that is helpful to extract the data easily.
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook


# In[193]:


driver = webdriver.Chrome("C:\ChromeDriver\chromedriver.exe")


# In[194]:


brands={'lg':169,'bgh':169,'samsung':179,'sony':179,'electrolux':169,'motorola':155,'huawei':179}


# In[ ]:





# In[195]:


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('WebCheck.xlsx', engine='xlsxwriter')
writer.save()
for NextBrand in brands:
    UrlAux="https://tienda.mercadolibre.com.ar/"+NextBrand
    print(UrlAux)
    
    products=[] #List to store name of the product
    prices=[] #List to store price of the product
    ratings=[] #List to store rating of th product
    driver.get(UrlAux)
    content = driver.page_source
    soup = BeautifulSoup(content)
    #print(brands[NextBrand]) soup.findAll('li',attrs={'class':'results-item highlighted article grid product item-info-height-'+str(brands[NextBrand])})
    for a in soup.findAll('div',attrs={'class':'item__info'}):
        name=a.find('span', attrs={'class':'main-title'})
        price=a.find('div', attrs={'class':'item__price'})
        #rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
        #print(rating)
        #print(name.text)
        products.append(name.text)
        prices.append(price.text)
    df = pd.DataFrame({'Product Name':products,'Price':prices}) 
    writer = pd.ExcelWriter('WebCheck.xlsx', engine='openpyxl')
    # try to open an existing workbook
    writer.book = load_workbook('WebCheck.xlsx')
    # copy existing sheets
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    # read existing file
    reader = pd.read_excel('WebCheck.xlsx')
    # write out the new sheet
    df.to_excel(writer,sheet_name=NextBrand,index=False)


    #print(df)
     # Close the Pandas Excel writer and output the Excel file.
    writer.save()

    # Convert the dataframe to an XlsxWriter Excel object.
    #df.to_excel(writer, sheet_name=NextBrand)



    #df.to_excel(r'C:\Users\Marcos\Desktop\Python_ITBA\My test\WebCheck.xlsx', sheet_name=NextBrand, index = False)
driver.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




