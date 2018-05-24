#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import geopandas as gpd
import matplotlib.pylab as mpl
import matplotlib.pyplot as plt
from shapely.geometry import Point

def load_housing_data():
    #读取header信息
    header_description = pd.read_table('D:/DEV_DATA/AI/cal_housing/CaliforniaHousing/cal_housing.domain', header=None, encoding='gb2312', sep=':')
    data = pd.read_csv('D:/DEV_DATA/AI/cal_housing/CaliforniaHousing/cal_housing.data')
    data.columns = header_description[0].tolist()
    #拼接header到columns
    return data

mpl.rcParams['font.sans-serif'] = ['SimHei']   # 雅黑字体
mpl.rcParams['axes.unicode_minus']=False

housing = load_housing_data()
print(housing.info())
print(housing.describe())

df = gpd.read_file('D:/DEV_DATA/shp/states.shp').to_crs({'init':'epsg:4326'})

gpd.sjoin(gpd.GeoDataFrame(crs={'init': 'epsg:4326'},
                           geometry=[Point(-73.966, 40.78)]),
                           df, how='left', op='within')

plt.xlabel(u"经度")
plt.ylabel(u"纬度")
plt.title(u'2015年各省市人均GDP(单位：万元)', fontsize=15)#设置图形标题

xseries = housing['longitude']
yseries = housing['latitude']
print(xseries, yseries)

points = []
for index, row in housing.iterrows():   # 获取每行的index、row
    x = row['longitude']
    y = row['latitude']
    housingMedianAge = row['housingMedianAge']
    totalRooms = row['totalRooms']
    totalBedrooms = row['totalBedrooms']
    population = row['population']
    households = row['households']
    medianIncome = row['medianIncome']
    medianHouseValue = row['medianHouseValue']

    point = Point(x,y)
    points.append(point)

fig, ax = plt.subplots()
ax.set_aspect('equal')

df.plot(column='STATE_NAME', alpha=0.5, ax=ax)
ptLayer = gpd.GeoSeries(points)
ptLayer.plot(ax=ax, marker='o', color='red', markersize=1);

plt.show()
