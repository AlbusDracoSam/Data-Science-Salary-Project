# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:28:04 2021

@author: Ajith
"""
import time
import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/Ajith/OneDrive/Desktop/Data Science/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 4)
