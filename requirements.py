#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import multiprocessing
from multiprocessing import Pool

from bs4 import BeautifulSoup
import requests

import re
import pandas as pd
import csv
import math
from tqdm.auto import tqdm

