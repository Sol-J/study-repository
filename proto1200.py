#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import proto
from proto import *
info_list = get_book_list("solbook.xlsx")
publishers, book_names, inf_ids, inf_urls, inf_dates = get_infringe_naver_blog(info_list[900:1200])

