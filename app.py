import streamlit as st
from matplotlib import pyplot as plt
import pandas as pd
import geopandas as gpd
from shapely import wkt

df = pd.read_csv('./data/populacao_BR_censos_pib_2022_2010.csv', sep = ';')

gdf = gpd.GeoDataFrame(df)
gdf['geometry'] = gdf['geometry'].apply(wkt.loads)
gdf = gdf.set_geometry('geometry')


