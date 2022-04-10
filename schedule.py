from collections import namedtuple
import streamlit.components.v1 as comp
import altair as alt
import math
from numpy import size
import pandas as pd
import streamlit as st
import requests
from pprint import pprint
from datetime import datetime as dt
import json

def buildingToCoords(code):
    building = "https://api.umd.io/v1/map/buildings/" + code
    cla = requests.get(building).json()
    
    latitude = cla['data'][0]['lat']
    longitude = cla['data'][0]['long']
    coords = str(latitude) + "+" + str(longitude)

    return coords

def coordsToMap(startCoords, endCoords):
    googleInput = 'https://www.google.com/maps/dir/' + startCoords + "/" + endCoords
    
    return googleInput

st.header("UMD MAPS 2.0")
sectionCount = st.number_input("How many sections would you like to input?", 1)

sectionIDs = []
# all_classes = requests.get("https://api.umd.io/v1/map/buildings").json()

for i in range(sectionCount):
    
    sectionIDs.append(st.text_input("Please input your section ID", key = i))

sectionCoords = {}
for i in sectionIDs:
    currentURL = "https://api.umd.io/v1/courses/sections/" + i
    curr = requests.get(currentURL).json()
  
    currentBuildingCode = curr[0]['meetings'][0]['building']

    sectionCoords[i] = (buildingToCoords(currentBuildingCode))




finalMapURL = "https://www.google.com/maps/dir/"

for i in sectionCoords:
    finalMapURL = finalMapURL + str(sectionCoords[i]) + "/"


# st.write("check out this [link]" + "(" + finalMapURL + ")")
# output = comp.iframe(finalMapURL, 10, 10, True)
# st.write(output)

# st.write(finalMapURL)
comp.html(
"""
<iframe src="https://www.google.com/maps/embed?pb=!1m36!1m12!1m3!1d6202.488754463963!2d-76.94867367347527!3d38.98691866822759!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m21!3e6!4m4!2s38.98677255%20-76.9484189!3m2!1d38.986772599999995!2d-76.9484189!4m4!2s38.98872265%20-76.9425929312518!3m2!1d38.988722599999996!2d-76.9425929!4m4!2s38.98506175%20-76.9430892753028!3m2!1d38.9850618!2d-76.9430893!4m4!2s38.98480955%20-76.9418413304917!3m2!1d38.9848096!2d-76.9418413!5e0!3m2!1sen!2sus!4v1649565487992!5m2!1sen!2sus" width="800" height="800" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
""",
height = 800,
scrolling=True
)