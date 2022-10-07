# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

beer=pd.read_csv('https://raw.githubusercontent.com/ian1152/Snallygaster_2022/main/Snallygaster%202022%20Beer%20List%20-%20Public%20-%20Beers.csv')
beer.columns=beer.columns.str.lower()
beer.abv=beer.abv.str.replace('%','').replace('TBD',np.nan).astype('float')
styles= {'IPA': [len(beer[beer.description.str.contains(r'IPA', na=False)])],
         'Pale ale': [len(beer[beer.description.str.contains(r'[Pp]ale', na=False)])],
         'Stout/Porter': [len(beer[beer.description.str.contains(r'[Ss]tout|[Pp]orter', na=False)])],
         'Sour': len(beer[beer.description.str.contains(r'[Ss]our|[Gg]ose|[Ff]ermentation|[Ff]ruited|[Bb]erliner', na=False)]),
         'Lager': len(beer[beer.description.str.contains(r'[Ll]ager|[Pp]ilsner|[Mm]ärzen|[Ff]estbier|[Hh]elles|[Dd]unkel', na=False)]),
         'Lambic': len(beer[beer.description.str.contains(r'[Ll]ambic', na=False)]),
         'Saison': len(beer[beer.description.str.contains(r'[Ss]aison', na=False)]),
         'Cider': len(beer[beer.description.str.contains(r'[Cc]ider', na=False)]),
         'Brown ale': len(beer[beer.description.str.contains(r'[Bb]rown', na=False)]),
         'Witbier': len(beer[beer.description.str.contains(r'[Ww]itbier | [Ww]heat', na=False)]),
         'Cream ale':len(beer[beer.description.str.contains(r'[Cc]ream', na=False)]),
         'Quads & Tripels': len(beer[beer.description.str.contains(r'[Qq]uadrupel|[Tt]ripel', na=False)])
         
         }
def beer_finder(pattern):
    
    
    new_pattern=''
    

    for i in pattern.split():
        caps=i.capitalize()
        new_pattern=new_pattern+caps
    new_pattern=re.sub(r"(\w)([A-Z])", r"\1 \2", new_pattern)  
        
    return beer[beer.description.str.contains(new_pattern, na=False)]
    

def brewery_location(pattern):
    return[beer.brewery.str.contains(patten, na=False)]
    



st.sidebar.title('Snally 2022')
st.sidebar.write('Developed by Ian Schaaf: ianschaaf1@gmail.com')

option=st.sidebar.selectbox('Select Page', ('Welcome Page', 'Analytics and Visualization', 'Beer Finder'))


if option=='Welcome Page':
    
    st.title('Snallygaster Exploration App')
    
    st.write('This is a one stop app to help you explore and find your favorite beer at Snallygaster. You can access analytics and the beer finder app from the sidebar. Enjoy! ')

    st.image('https://www.snallygasterdc.com/_files/ugd/41fc83_7cb2f62c18744070968db027182f0ea5.pdf')
    
    
if option=='Analytics and Visualization':
   
    st.title('Analytics and Visualization') 
    
    st.subheader('There are {} breweries serving {} unique beers'.format(len(beer.brewery.unique()),len(beer)))
    st.text('')
    st.subheader('The lowest ABV is {}%, the highest is {}%, and the average is {}%'.format(str(beer.describe().loc['min'][0]),str(beer.describe().loc['max'][0]),round(beer.describe().loc['mean'][0],2)))
    
    
    #col1, col2=st.columns(2)
    
    fig=plt.figure(figsize=(10,6))

    beer.abv.plot.hist( title='What ABV are most beers?', xticks=np.arange(3,20,1), edgecolor='black', xlabel='% ABV')
   
    st.pyplot(fig, clear_figure=(True))
    
    
    
    fig=plt.figure(figsize=(10,6))

    pd.DataFrame(styles).plot.bar(title="Beer by style", xlabel='')
    
    st.pyplot(fig)
    
    
if option=='Beer Finder':

    st.title('Beer Finder')
    
    st.write('Below you can enter an ingredient, style, or any other word that might appear in the descripition of the beer. You can also locate your favorite brewery in the dropdown below that. ')

    search=st.text_input("Ingredient/style")
    
    st.write(beer_finder(search))
    
    location=st.selectbox('Select brewery', beer.brewery.unique())
    
    st.write('Here are all {}\'s beers. It is located in the {} section. See the map below'.format(location,beer[beer.brewery==location]['festival location'].iloc[0]))
    
    beer[beer.brewery==location]
    
    st.image('https://www.snallygasterdc.com/_files/ugd/41fc83_7cb2f62c18744070968db027182f0ea5.pdf')
    
    






    
