# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:00:27 2017

@author: Jieqiang.Zhu
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May  2 08:16:30 2017

@author: Jieqiang.Zhu
"""

import requests
import numpy as np
import pandas as pd
import re
import string

from bs4 import BeautifulSoup

main_url = "https://naturalmedicines.therapeuticresearch.com/databases/food,-herbs-supplements.aspx?letter="

herb_name = []
herb_link =[]
alpha = string.ascii_uppercase

for letter in alpha:
    url = main_url + letter
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    k = soup.find_all('a',{'href':re.compile(r'productid')})
    for each in k:
        herb_name.append(each.string)
        herb_link.append("https://naturalmedicines.therapeuticresearch.com" + each.get('href'))

total_herb_list = pd.DataFrame(np.column_stack([herb_name,herb_link]))
total_herb_list.to_csv('total_herb_list_trc.csv')


#for i,element in enumerate(herb_name):
#    for ch in ['/',':']:
#        if ch in element:
#            element = element.replace(ch,"-")
#    modified_herb_name[i] = element
#
#for j in herb_link:
#    r = requests.get(j)
#    soup = BeautifulSoup(r.text,"lxml")
#    k = soup.find_all("a",class_ = "pdf")
#    word_1 = "Final assessment report"
#    word_3 = "Assessment report"
#    word_2 = "Herbal_-_HMPC_assessment_report"
#    for each in k:
#        if re.search(word_1,str(each.string)) and re.search(word_2,each.get('href')):
#            pdf_url = "http://www.ema.europa.eu" + each.get('href')
#            accessement_report_link.append(pdf_url)
#            break
#            #file_name = str(format(i+1,"03d")) +"_" + str(modified_herb_name[i])+".pdf"
#            #urllib.request.urlretrieve(pdf_url,file_name)
#        elif re.search(word_3,str(each.string)) and re.search(word_2,each.get('href')):
#            pdf_url = "http://www.ema.europa.eu" + each.get('href')
#            accessement_report_link.append(pdf_url)
#            break
#            #file_name = str(format(i+1,"03d")) +"_" + str(modified_herb_name[i])+".pdf"
#            #urllib.request.urlretrieve(pdf_url,file_name)
#        else: 
#            accessement_report_link.append("None")
#            
#total_herb_list = pd.DataFrame(np.column_stack([herb_name,herb_link,accessement_report_link]))
#total_herb_list.to_csv('total_herb_list_EMA.csv')
#      
