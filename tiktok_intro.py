#!/usr/bin/env python
# coding: utf-8

# # Setting Everything Up

# In[2]:


import pandas as pd
from datetime import datetime


# In[3]:


#import the file from the web
import requests
from bs4 import BeautifulSoup
import pandas as pd
from unicodedata import normalize
import re
from datetime import datetime
from pandas import read_csv 
from sklearn.feature_extraction.text import CountVectorizer

# I can give a number or use None to remove maximum ceiling & display all columns
pd.options.display.max_columns = None

# # I want to be able to see the entire narrative, so remove the maximum width for each column
# pd.options.display.max_colwidth = None

# pd.options.display.float_format = '{:,.2f}'.format

# import string

# get_ipython().run_line_magic('matplotlib', 'inline')


# # In[4]:


# get_ipython().run_line_magic('load_ext', 'rpy2.ipython')
# get_ipython().run_line_magic('load_ext', 'autoreload')
# get_ipython().run_line_magic('autoreload', '2')

# get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import rcParams
rcParams['figure.figsize'] = (8, 8)

import warnings
from rpy2.rinterface import RRuntimeWarning
warnings.filterwarnings("ignore") # Ignore all warnings
# warnings.filterwarnings("ignore", category=RRuntimeWarning) # Show some warnings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, HTML
from IPython.display import Javascript


# In[5]:


# get_ipython().run_cell_magic('javascript', '', '// Disable auto-scrolling\nIPython.OutputArea.prototype._should_scroll = function(lines) {\n    return false;\n}\n')


# In[6]:


# get_ipython().run_cell_magic('R', '', "\n# My commonly used R imports\n\nrequire('tidyverse')\n")


# In[7]:


#To Download PDFs
from urllib.parse import urljoin


# In[8]:


#To import camelot and PDF-related items
import camelot
import ghostscript
import sys


# In[9]:


# get_ipython().run_cell_magic('R', '', '\nlibrary(jpeg)\nlibrary(wordcloud)\nlibrary(RColorBrewer)\nlibrary(wordcloud2)\nlibrary(tm)\n')


# In[10]:


from sklearn.feature_extraction.text import CountVectorizer


# In[11]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[12]:


from TikTokApi import TikTokApi



# # Scraping

# In[13]:


# tiktok_url_example = "https://www.tiktok.com/discover/why-you-lying-challenge-high-school-edition?lang=en"
# tiktok_raw_html_example = requests.get(tiktok_url_example).content
# tiktok_soup_doc_example = BeautifulSoup(tiktok_raw_html_example, "html.parser")
# # print(soup_doc.prettify())


# In[14]:


# tiktok_soup_doc_example.find_all(id='main-content-discover_kw')


# In[15]:


# # //*[@id="main-content-discover_kw"]/div[1]/div[2]/div[1]/a/div[2]/div/span[1]

# temp_title = tiktok_soup_doc_example.find_all('span', attrs={'class': 'tiktok-j2a19r-SpanText efbd9f0'})


# temp_title

# for entry in temp_title:
#     print(entry)
#     print("#######")


# In[16]:


# tiktok_soup_doc_example.prettify()


# ### Not sure if this will work given it is a one page result that changes regularly. 
# 1) The fact that the caption is spread out makes it difficult to figure out where a caption begins or ends
# 2) video URL is also complicated to find. 
# 3) could pursue this with some support

# ### Trying to scrape Tiktok itself

# In[17]:


# curl -X POST \
#   'https://open.tiktokapis.com/v2/research/video/query/?fields=id,like_count' \
#   -H 'authorization: bearer clt.1234567XlLdeTzD79wm76' \
#   -d '{ 
#           "query": {
#               "and": [
#                    { "operation": "IN", "field_name": "region_code", "field_values": ["US", "IN"] },
#                    { "operation": "GT", "field_name": "hashtag_name", "field_values": ["hello"] }
#                ]
#           }, 
#           "start_date": "20220615",
#           "end_date": "20220628",
#           "max_count": 10
# }


# In[18]:


# %%js
# alert("hello, world!");


# # Start here

# In[19]:


CLIENT_KEY="awu65z8y5py5mpyl"
CLIENT_SECRET="3b52b47d389463a34cde40e2a75544ac"


# In[20]:


# get_ipython().run_cell_magic('js', '', '\nCLIENT_KEY=>"awu65z8y5py5mpyl"\nCLIENT_SECRET=>"3b52b47d389463a34cde40e2a75544ac"\n')


# In[21]:


# %%js

# app.get('/redirect', (req, res) => {
#     const { code, state } = req.query;
#     const { csrfState } = req.cookies;

#     if (state !== csrfState) {
#         res.status(422).send('Invalid state');
#         return;
#     }

#     let url_access_token = 'https://open-api.tiktok.com/oauth/access_token/';
#     url_access_token += '?client_key=' + CLIENT_KEY;
#     url_access_token += '&client_secret=' + CLIENT_SECRET;
#     url_access_token += '&code=' + code;
#     url_access_token += '&grant_type=authorization_code';

#     fetch(url_access_token, {method: 'post'})
#         .then(res => res.json())
#         .then(json => {
#             res.send(json);
#         });
# })


# In[22]:


# curl -X POST \
#   'https://open.tiktokapis.com/v2/research/video/query/?fields=id,like_count' \
#   -H 'authorization: bearer clt.1234567XlLdeTzD79wm76' \
#   -d '{ 
#           "query": {
#               "and": [
#                    { "operation": "IN", "field_name": "region_code", "field_values": ["US", "CA"] },
#                    { "operation": "EQ", "field_name": "keyword", "field_values": ["whyareyoulying","whyareyoulyingchallenge","whyyoulyingchallenge"] }
#                ]
#           }, 
#           "start_date": "20220615",
#           "end_date": "20220628",
#           "max_count": 10
# }'


# # End Here

# # Try Tiktok API library

# # Getting started
# https://pypi.org/project/TikTokApi/3.8.0/#the-gethashtagobject-method

# In[23]:


# ! pip install TikTokApi


# In[24]:


# ! python -m playwright install


# In[25]:


# !docker pull mcr.microsoft.com/playwright:focal
# !docker build . -t tiktokapi:latest
# !docker run -v TikTokApi --rm tiktokapi:latest python3 tiktok_intro.ipynb


# In[26]:


# Watch https://www.youtube.com/watch?v=-uCt1x8kINQ for a brief setup tutorial
with TikTokApi() as api:
    for trending_video in api.trending.videos(count=50):
        # Prints the author's username of the trending video.
        print(trending_video.author.username)


# In[ ]:





# In[ ]:





# In[ ]:




