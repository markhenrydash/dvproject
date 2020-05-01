# -*- coding: utf-8 -*-
"""Exploration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BfKJ_5pUppHcTUC66wja9hpesYngFZv5
"""

import pandas as pd
import io
import os

import numpy as np
import enum

import json

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

os.chdir('/content/drive/My Drive/dv/DES_DwC-A')

name = {"type":"Topology","transform":{"scale":[0.0017670553225065367,0.0012461030136843383],"translate":[-114.81337059380196,31.33168393952881]},"arcs":[[[837,941],[433,0],[207,2]],[[1477,943],[233,0],[249,-5],[110,8],[169,0],[10,2],[220,0]],[[2468,948],[0,-69]],[[2468,879],[0,-558]],[[2468,321],[-343,-4],[-60,0],[1,-164],[-115,-1],[0,-77]],[[1951,75],[-566,254],[-548,240]],[[837,569],[0,372]],[[2468,321],[-5,-94],[0,-226]],[[2463,1],[-347,-1],[-165,75]],[[1844,2520],[30,21],[17,-29],[-26,-26],[54,6],[2,-48],[12,39],[84,22],[58,-63],[29,17],[78,-66],[62,-38],[37,27],[19,-30]],[[2300,2352],[0,-210],[423,0],[0,-340]],[[2723,1802],[0,-89],[-95,-12],[-97,-19],[-57,-37],[-9,-69],[32,-78],[-28,-3]],[[2469,1495],[-80,-49],[-23,7],[-52,-58],[-31,-69],[-99,237],[-11,50],[-37,100]],[[2136,1713],[-64,170],[-39,-61],[-37,45],[-58,95],[10,38],[-45,77],[3,66],[-28,-1]],[[1878,2142],[10,121],[-138,8],[26,116],[9,64],[60,43],[-1,26]],[[53,1113],[8,18],[22,-6],[28,6],[26,5],[22,28],[36,50],[3,46],[-7,17],[-3,39],[-17,42],[-3,0]],[[168,1358],[140,5],[1,348],[175,1],[0,-70],[353,0]],[[837,1642],[0,-490],[0,-211]],[[837,569],[-235,103],[-602,261],[1,23],[9,22],[-10,11],[8,23],[-6,19],[25,26],[26,56]],[[2468,879],[693,-2],[64,1]],[[3225,878],[38,0]],[[3263,878],[0,-274],[-1,-231],[0,-372],[-442,1],[-357,-1]],[[837,3368],[90,-18],[15,-22],[98,-69],[12,-29],[113,-40],[34,4],[86,-60],[58,19],[-1,-89],[60,-1],[1,-141],[185,2],[130,5],[0,-143],[128,-1],[-2,-265]],[[1878,2142],[-130,0],[-249,38],[-18,-59],[-45,-74],[-265,95],[-334,-1]],[[837,2141],[0,255]],[[837,2396],[0,956],[0,16]],[[104,1687],[18,46],[42,49],[-3,44],[2,44],[12,25],[4,21],[-4,33],[-9,54],[8,30],[-1,29],[-15,22],[14,23],[31,44],[11,25],[3,29],[1,11],[13,15],[32,19],[32,25],[36,16],[29,42],[22,16],[-1,35]],[[381,2384],[62,-35],[102,-6],[97,-34],[42,16],[37,62],[95,-12],[21,21]],[[837,2141],[0,-348],[0,-151]],[[168,1358],[-33,10],[-30,-4],[-24,5],[-20,54],[15,44],[1,57],[2,20],[-28,26],[9,28],[0,43],[-10,23],[29,11],[22,3],[3,9]],[[432,4423],[0,126],[48,0],[565,0],[38,0],[39,0],[161,0],[4,0]],[[1287,4549],[6,-39],[-41,-96],[-22,-127],[10,-63],[-22,-42],[21,-55],[-3,-67],[-30,-40],[-24,4],[-39,-49],[-41,-2],[-21,-23],[-60,-12],[-73,-59],[-34,-10],[-16,-50],[-53,5],[-20,-45],[21,-63],[-10,-38],[14,-40],[-13,-49],[0,-221]],[[381,2384],[0,2],[-18,32],[-52,45],[-40,39],[-25,0],[0,54],[-25,51],[-24,89],[-14,27],[-49,72],[-33,47],[3,56],[-2,47],[5,54],[3,42],[11,0],[15,14],[-8,99],[-23,119],[-21,32],[1,60],[6,69],[-21,33],[-4,66],[-4,65],[19,40],[-17,30],[-17,34],[-7,53],[0,44],[0,3],[4,28],[39,10],[22,19],[32,9],[34,-1],[14,-17],[22,-3],[17,16],[26,-2],[20,-28],[12,-37],[25,-21],[33,-16],[35,8],[7,22],[22,54],[30,59],[-1,60],[1,45],[-1,224],[-1,192]],[[1287,4549],[103,1],[535,0],[4,0],[72,-1],[120,2],[179,0],[0,0]],[[2300,4551],[-1,-1582],[1,-617]],[[3009,1863],[9,31],[65,38],[10,31],[170,1]],[[3263,1964],[0,-296],[0,-161],[0,-347],[0,0],[0,-282]],[[3225,878],[-63,83],[11,85],[-22,86],[-50,81],[-92,189],[0,461]],[[2723,1802],[56,-1],[6,-6]],[[2785,1795],[70,-75],[93,111],[61,32]],[[2468,948],[1,19],[0,528]],[[1477,943],[0,142],[1,452],[-1,51],[68,-85],[108,0],[13,-1],[104,1],[58,1],[2,209],[306,0]],[[2300,4551],[157,-4],[266,0]],[[2723,4547],[0,-1071],[99,0],[-10,-116],[0,-559],[-4,-140],[-8,-71],[10,-69],[-7,-278],[0,-280],[-18,0],[0,-168]],[[3264,4548],[0,-100],[0,-608],[0,-91],[0,-99],[0,-213],[-1,-201],[1,-152],[0,-173],[0,-305],[0,-46],[0,-519],[-1,-77]],[[2723,4547],[0,0],[286,1],[255,0]]],"objects":{"cb_2015_arizona_county_20m":{"type":"GeometryCollection","geometries":[
{"arcs":[[0,1,2,3,4,5,6]],"type":"Polygon","properties":{"density":"108.1","density2":"54.8","STATEFP":"04","COUNTYFP":"019","COUNTYNS":"00025446","AFFGEOID":"0500000US04019","GEOID":"04019","NAME":"Pima","LSAD":"06","ALAND":23794325411,"AWATER":5273054}},
{"arcs":[[7,8,-5]],"type":"Polygon","properties":{"density":"38.2","density2":"54.8","STATEFP":"04","COUNTYFP":"023","COUNTYNS":"00040472","AFFGEOID":"0500000US04023","GEOID":"04023","NAME":"Santa Cruz","LSAD":"06","ALAND":3203593349,"AWATER":3088047}},
{"arcs":[[9,10,11,12,13,14]],"type":"Polygon","properties":{"density":"11.1","density2":"54.8","STATEFP":"04","COUNTYFP":"007","COUNTYNS":"00040471","AFFGEOID":"0500000US04007","GEOID":"04007","NAME":"Gila","LSAD":"06","ALAND":12323041468,"AWATER":97111975}},
{"arcs":[[15,16,17,-7,18]],"type":"Polygon","properties":{"density":"36.5","density2":"54.8","STATEFP":"04","COUNTYFP":"027","COUNTYNS":"00023901","AFFGEOID":"0500000US04027","GEOID":"04027","NAME":"Yuma","LSAD":"06","ALAND":14281191792,"AWATER":13171316}},
{"arcs":[[-4,19,20,21,-8]],"type":"Polygon","properties":{"density":"21.0","density2":"54.8","STATEFP":"04","COUNTYFP":"003","COUNTYNS":"00025442","AFFGEOID":"0500000US04003","GEOID":"04003","NAME":"Cochise","LSAD":"06","ALAND":15968982233,"AWATER":137024922}},
{"arcs":[[22,-15,23,24,25]],"type":"Polygon","properties":{"density":"26.3","density2":"54.8","STATEFP":"04","COUNTYFP":"025","COUNTYNS":"00042809","AFFGEOID":"0500000US04025","GEOID":"04025","NAME":"Yavapai","LSAD":"06","ALAND":21039920080,"AWATER":11501575}},
{"arcs":[[26,27,-25,28,-17,29]],"type":"Polygon","properties":{"density":"4.5","density2":"54.8","STATEFP":"04","COUNTYFP":"012","COUNTYNS":"00043540","AFFGEOID":"0500000US04012","GEOID":"04012","NAME":"La Paz","LSAD":"06","ALAND":11654000682,"AWATER":36568021}},
{"arcs":[[30,31,-26,-28,32]],"type":"Polygon","properties":{"density":"15.0","density2":"54.8","STATEFP":"04","COUNTYFP":"015","COUNTYNS":"00025445","AFFGEOID":"0500000US04015","GEOID":"04015","NAME":"Mohave","LSAD":"06","ALAND":34475714657,"AWATER":387347771}},
{"arcs":[[33,34,-10,-23,-32]],"type":"Polygon","properties":{"density":"7.3","density2":"54.8","STATEFP":"04","COUNTYFP":"005","COUNTYNS":"00025443","AFFGEOID":"0500000US04005","GEOID":"04005","NAME":"Coconino","LSAD":"06","ALAND":48222080889,"AWATER":110096951}},
{"arcs":[[35,36,-21,37]],"type":"Polygon","properties":{"density":"4.8", "density2":"54.8","STATEFP":"04","COUNTYFP":"011","COUNTYNS":"00042807","AFFGEOID":"0500000US04011","GEOID":"04011","NAME":"Greenlee","LSAD":"06","ALAND":4773671883,"AWATER":13745242}},
{"arcs":[[38,39,-38,-20,-3,40,-12]],"type":"Polygon","properties":{"density":"8.0","density2":"54.8","STATEFP":"04","COUNTYFP":"009","COUNTYNS":"00025444","AFFGEOID":"0500000US04009","GEOID":"04009","NAME":"Graham","LSAD":"06","ALAND":11972305015,"AWATER":47705575}},
{"arcs":[[-13,-41,-2,41]],"type":"Polygon","properties":{"density":"72.6","density2":"54.8","STATEFP":"04","COUNTYFP":"021","COUNTYNS":"00025447","AFFGEOID":"0500000US04021","GEOID":"04021","NAME":"Pinal","LSAD":"06","ALAND":13897001099,"AWATER":22331619}},
{"arcs":[[-29,-24,-14,-42,-1,-18]],"type":"Polygon","properties":{"density":"427.9","density2":"54.8","STATEFP":"04","COUNTYFP":"013","COUNTYNS":"00037026","AFFGEOID":"0500000US04013","GEOID":"04013","NAME":"Maricopa","LSAD":"06","ALAND":23826751660,"AWATER":64344166}},
{"arcs":[[42,43,-39,-11,-35]],"type":"Polygon","properties":{"density":"10.8","density2":"54.8","STATEFP":"04","COUNTYFP":"017","COUNTYNS":"00042808","AFFGEOID":"0500000US04017","GEOID":"04017","NAME":"Navajo","LSAD":"06","ALAND":25770082478,"AWATER":24078111}},
{"arcs":[[44,-36,-40,-44,45]],"type":"Polygon","properties":{"density":"6.4","density2":"54.8","STATEFP":"04","COUNTYFP":"001","COUNTYNS":"00025441","AFFGEOID":"0500000US04001","GEOID":"04001","NAME":"Apache","LSAD":"06","ALAND":29001812294,"AWATER":54170779}}]}}}

name['objects']['cb_2015_arizona_county_20m']['geometries'][0]

data2 = pd.read_csv('occurrences.csv')

data2

data_all

data = pd.read_csv('arizona_csv.csv')

arizonadata = data2[data2['stateProvince'] == 'Arizona']

arizonadata = arizonadata[arizonadata['county'].notna()]

#finding data rows with no county

for index, row in arizonadata.iterrows():
  substring1 = 'no county'
  #substring1 = substring1.lower()
  r = row['county']
  if( r == substring1 ):
    print(index)

arizonadata = arizonadata[arizonadata.index != 14189] #removing data row with 'no county'

counties = ['apache',
 'cochise',
 'coconino',
 'gila',
 'graham',
 'greenlee',
 'la paz',
 'maricopa',
 'mohave',
 'navajo',
 'pima',
 'pinal',
 'santa cruz',
 'yavapai',
 'yuma']

for c in counties:
  print(c)
  for index,row in arizonadata.iterrows():
    name = str(row['county'])
    name = name.lower()
    #name = name.split(',')
    #print(name)
    if( c in name ):
      arizonadata.at[index,'county'] = c





set(arizonadata['county'])

#small changes:

for index,row in arizonadata.iterrows():
  if( row['county'] == 'Maricipa County'):
    print(index)

arizonadata.at[79824,'county'] = 'maricopa'

for index,row in arizonadata.iterrows():
  if( row['county'] == 'Mojave'):
    print(index)

arizonadata.at[13962,'county'] = 'maricopa'

arizonadata2 = arizonadata[arizonadata['county'] != 'San Bernardino County']

arizonadata2

arizonadata2.to_csv("arizona_csv2.csv",index=False)

arizonadataclean1 = pd.read_csv('/content/drive/My Drive/dv/DES_DwC-A/arizona_csv2.csv')

set(arizonadataclean1['county'])





set(arizonadataclean1['county'])

countyScience = arizonadataclean1[['scientificName','county']]

countyScience = countyScience.dropna()

countyScience = countyScience.drop_duplicates(subset=None, keep='first', inplace=False)

countyScience.to_csv("countyOnly.csv",index=False)

countyOnly = pd.read_csv('countyOnly6.csv')

from google.colab import drive
drive.mount('/content/drive')

counties_set = list(set(countyOnly['county']))

countyOnly[countyOnly['scientificName'] == 'Elymus salinus']

county1_list = []
county_len_list = []

counties_dict = {}

for i in counties_set:
  counties_dict[i] = None

for county1 in counties_set:
  print(county1,len(arizonadataclean1[arizonadataclean1['county'] == county1]))
  dfArizona = arizonadataclean1[arizonadataclean1['county'] == county1]
  
  dfArizona = dfArizona[dfArizona['scientificName'].notna()]
  
  scienceNames_set = list(set(dfArizona['scientificName']))

  temp_science_dict = {}

  for j in scienceNames_set:
    temp_science_dict[j] = 0

  for j in scienceNames_set:
    dfArizonaScience = dfArizona[dfArizona['scientificName'] == j]
    length = len(dfArizonaScience)
    temp_science_dict[j] = length
  
  sorted_dict = {k: v for k, v in sorted(temp_science_dict.items(), key=lambda item: item[1], reverse=True)}


  sorted_dict = {k: sorted_dict[k] for k in list(sorted_dict)[:5]}

  print(sorted_dict)

  counties_dict[county1] = sorted_dict


  county1_list.append(county1)
  county_len_list.append(len(arizonadataclean1[arizonadataclean1['county'] == county1]))

for i in counties_dict:
  sorted_dict = {k: v for k, v in sorted(counties_dict[i].items(), key=lambda item: item[1], reverse=True)}
  print(i, sorted_dict)

df_counties_stats = pd.DataFrame(columns=['name','number'])

df_counties_stats['name'] = county1_list
df_counties_stats['number'] = county_len_list



df_counties_stats = df_counties_stats.sort_values(by=['number'],ascending=False)

list(df_counties_stats['number'])

county1_list

county_len_list

scientificNames = list(set(countyOnly['scientificName']))

scientificNames[:4]

associations = pd.DataFrame(columns = scientificNames)

associations

bigrow = []
for county in counties_set:
  print("County name : ", county)
  oneCountyData = countyOnly[countyOnly['county'] == county]
  setScienceNames=set(oneCountyData['scientificName'])
  row = []
  for i in scientificNames:
    if( i in setScienceNames):
      row.append(1)
    else:
      row.append(0)
  
  bigrow.append(row)
print (counties_set[0])

onehotDf=pd.DataFrame(bigrow,columns=scientificNames)

onehotDf.set_index(pd.Index(counties_set))

onehotDf

onehotDf.to_csv("onehotcsv.csv",index=False)

onehotDf = pd.read_csv("onehotcsv2.csv")

len(bigrow[0])

for scientificName in scientificNames:
  #print(onehotDf[scientificName])
  x = list(onehotDf[scientificName])
  ones = 0
  for i in x:
    if( i == 1 ):
      ones+=1
  if( ones <= 3 ):
    onehotDf = onehotDf.drop(columns=[scientificName])

onehotDf

freq_items = apriori(onehotDf, min_support=0.8, use_colnames=True)
#apriori(onehotDf, min_support=0.7, use_colnames=True, max_len=None)

freq_items.tail(n=10)

rules = association_rules(freq_items, metric="confidence", min_threshold=0.6)

rules

antecedents = list(rules['antecedents'])

rules.to_csv('rules.csv', index=False)

consequents = list(rules['consequents'])



#draw_graph(rules,6)

result_counties = list()

i = 0

counties_discovery = []

dict1 = dict()

counties_list = list(counties_set)

for i in counties_list:
  dict1[i] = set()


for i in range(len(antecedents)):
  print("Iteration ",i)
  ls = list(antecedents[i])
  ls_consequents = list(consequents[i])
  print(ls)

  county_match = []
  counties_list = list(counties_set)

  names = []




  if( len(ls) > 1 ):
    for j in ls:
      temp_list = list(onehotDf[j])
      county_match.append(temp_list)
    
    for k in range(len(county_match[0])):
      if county_match[0][k] == 1:
        names.append(counties_list[k])
    #print(names)
    for k in county_match[1:]:
      names_temp = []
      for x in range(len(k)):
        if k[x] == 1:
          names_temp.append(counties_list[x])
      
      for name in names:
        if name not in names_temp:
          names.remove(name)
    
    #print(names)

  elif len(ls) == 1:
    temp_list = list(onehotDf[ls[0]])
    for x in range(len(temp_list)):
      if temp_list[x] == 1:
        names.append(counties_list[x])

  places_containing_antecedents = names
  #print(places_containing_antecedents)

  for place in places_containing_antecedents:
    ind = counties_list.index(place)
    for plant in ls_consequents:
      if(onehotDf[plant][ind] == 0):
        print("County: ", place, "Plant: ", plant)
        
        rule_support = rules.at[i,'support']
        rule_support = round(rule_support,3)
        rule_confidence = rules.at[i,'confidence']
        rule_confidence = round(rule_confidence,3)

        rule = ''
        for ant in ls:
          rule+=ant + ","
        rule = rule[:len(rule)-1]

        rule = rule + " ==> "
        for ls_consequent in ls_consequents:
          rule+= ls_consequent + ","
        
        rule = rule[:len(rule)-1]
        
        print("Rule", rule)
        print("Support", round(rule_support,3), "Confidence", round(rule_confidence,3))

        dict1[place].add(plant + '$$'+str(rule_support)+ "$$" +str(rule_confidence))
        #
        result_counties.append(plant)
        counties_discovery.append(place)
  
print(dict1) #store results of possible discovery

print(set(counties_discovery))

result_counties = list(set(result_counties))

dict1

result_counties
