#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install geopandas


# In[5]:


pip install pymongo[srv]


# In[7]:


import json
import copy
from pymongo import MongoClient
client = MongoClient("mongodb+srv://vaccine-devs:vaccine-devs123@clustervaccinedeveloper.imldj.mongodb.net/vaccine-devs?retryWrites=true&w=majority")


# In[8]:


import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
import os
pd.options.display.max_columns=200
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


#os.chdir("/home/adlp/Escritorio/tareas/willie/covid")


# In[10]:


df_vacuna=pd.read_csv("/content/vacunas_covid (5).csv")


# In[11]:


vaccineDatosAbiertos = client["vaccine-devs"].vaccineDatosAbiertos
vaccineDatosAbiertos.delete_many({})
#proceso


# In[122]:


df_vacuna_ubigeo=pd.merge(df_vacuna,df_ubigeo, how="left", on=["DEPARTAMENTO","PROVINCIA","DISTRITO"])


# In[126]:


df_vacuna_ubigeo["UBIGEO_DEPART"]=df_vacuna_ubigeo["UBIGEO"].str[0:2] +'0000'
df_vacuna_ubigeo["UBIGEO_PROVINCIA"]=df_vacuna_ubigeo["UBIGEO"].str[0:4] +'00'


# In[170]:


def cat_edad(x):
    if 0<=x<=19:
        return "[0-19]"
    elif 20<=x<=24:
        return "[20-24]"
    elif 25<=x<=29:
        return "[25-29]"
    elif 30<=x<=34:
        return "[30-34]"
    elif 35<=x<=39:
        return "[35-39]"
    elif 40<=x<=44:
        return "[40-44]"
    elif 45<=x<=49:
        return "[45-49]"
    elif 50<=x<=54:
        return "[50-54]"
    elif 55<=x<=59:
        return "[55-59]"
    elif 60<=x<=64:
        return "[60-64]"
    elif 65<=x<=69:
        return "[65-69]"
    elif 70<=x<=74:
        return "[70-74]"
    elif 75<=x<=79:
        return "[75-79]"
    elif 80<=x<=120:
        return "[80-120]"
    elif 121<=x:
       return "[120+]"


# In[2]:


int("7")


# In[171]:


df_vacuna_ubigeo["EDAD_CAT"]=df_vacuna_ubigeo["EDAD"].apply(lambda x:cat_edad(x))


# In[188]:


temp_ubigeo=df_vacuna_ubigeo[~df_vacuna_ubigeo["UBIGEO"].isnull()]


# In[191]:


list_ubigeo=list(temp_ubigeo["UBIGEO"]) + list(temp_ubigeo["UBIGEO_PROVINCIA"]) + list( temp_ubigeo["UBIGEO_DEPART"])


# In[176]:


def cant_vac_ubi(UBIGEO,df_vacuna_ubigeo):
  df=df_vacuna_ubigeo[(df_vacuna_ubigeo["UBIGEO"]==UBIGEO)|(df_vacuna_ubigeo["UBIGEO_PROVINCIA"]==UBIGEO)|(df_vacuna_ubigeo["UBIGEO_DEPART"]==UBIGEO)]
  totalVacunados   = int(df["DOSIS"].count()) 
  mujeresVacunados =  int(df[df["SEXO"]=='FEMENINO']["DOSIS"].count())
  hombresVacunados =  int(df[df["SEXO"]=='MASCULINO']["DOSIS"].count())
  mujeresEdad=dict()
  hombresEdad=dict()
  for edad_cat in df[df["SEXO"]=='FEMENINO']["EDAD_CAT"].values:
      mujeresEdad[edad_cat]=int(df[(df["SEXO"]=='FEMENINO')&(df["EDAD_CAT"]==edad_cat)]["DOSIS"].count())
  for edad_cat in df[df["SEXO"]=='MASCULINO']["EDAD_CAT"].values:
      hombresEdad[edad_cat]=int(df[(df["SEXO"]=='MASCULINO')&(df["EDAD_CAT"]==edad_cat)]["DOSIS"].count())
  dict_full=dict()
  dict_full["ubigeo"]=UBIGEO
  dict_full["mujeresVacunados"]=mujeresVacunados
  dict_full["hombresVacunados"]=hombresVacunados
  dict_full["mujeresEdad"]=mujeresEdad
  dict_full["hombresEdad"]=hombresEdad
  return dict_full


# In[193]:


dict2=cant_vac_ubi('140101',df_vacuna_ubigeo)


# In[192]:


dict1=cant_vac_ubi('140101',df_vacuna_ubigeo)


# In[201]:


x


# In[209]:


type(dict1)


# In[208]:


x = [dict1, dict1]
vaccineDatosAbiertos.insert_many(x)


# In[207]:


type(x)


# In[203]:


x


# In[ ]:





# In[ ]:





# In[ ]:



   "ubigeo": "01000",
   totalVacunados:""
     mujeresVacunados: ""
     hombresVacunados:""
     mujeresEdad:{}
     hombresEdad: {}
}


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


010000: {
     totalVacunados:""
     totalPoblacion: ""
     mujeresTotal:""
     varonesTotal: ""
     mujeresVac: ""
     hombresVac:""
     mujeresEdad:{}
     hombresEdad: {}
}


# In[ ]:


mujeresEdad:{
   "40-44": { vacunados: "100", totalPoblacion: "123"
}


# In[ ]:





# In[77]:


df_demogragia=pd.read_csv("/content/demografia.csv")


# In[79]:


df_demogragia["ubigeo"].value_counts()


# In[91]:


df_demogragia[df_demogragia["ubigeo"]==20000]


# In[89]:


df_demogragia["ubigeo"]


# In[ ]:





# In[78]:


data["FABRICANTE"].unique()


# In[79]:


data["GRUPO_RIESGO"].nunique()


# In[80]:


data.isnull().sum()


# In[81]:


data[data["SEXO"].isnull()]


# In[82]:


data.head(2)


# In[83]:


data.columns


# In[84]:


def Sexo_Plot(data,dict_filt):
  for filt in dict_filt.keys():
    print(filt)
  el
  return
  #data_plot=data[(data["depart"].isin(depart))&()]


# In[85]:


dict_filt={"depart":"DEPARTAMENTO","distr":"San Juan de Lurigancho"}


# In[86]:


dict_filt.values()


# In[87]:


Sexo_Plot(data,{"depart":"Lima","distr":"San Juan de Lurigancho"})


# In[ ]:


$'print("")'


# In[ ]:


exec("print('Holar mundo')")


# In[87]:





# In[88]:


data.head(2)


# In[89]:


data[data["DEPARTAMENTO"]=="LAMBAYEQUE"]['SEXO'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',shadow=True)
plt.title("Distribucion segun Genero")
plt.show()


# In[91]:


data['GRUPO_RIESGO'].value_counts()


# In[18]:


data['GRUPO_RIESGO'].value_counts().plot.bar(color=['#CD7F32','#FFDF00','#D3D3D3'])
plt.title('GRUPO RIESGO')
plt.ylabel('Count')
#sns.countplot('GRUPO_RIESGO',hue='SEXO',data=data,ax=ax[1])
#ax[1].set_title('GRUPO RIESGO   vs SEXO')
plt.show()


# In[19]:


def cat_edad(x):
    if 18<=x<=23:
        return "[18-23>"
    elif 23<=x<28:
        return "[23-28>"
    elif 28<=x<33:
        return "[28-33>"
    elif 33<=x<38:
        return "[33-38>"
    elif 38<=x<43:
        return "[38-43>"
    elif 43<=x<48:
        return "[43-48>"
    elif 48<=x<53:
        return "[48-53>"
    elif 53<=x<58:
        return "[53-58>"
    elif 58<=x<63:
        return "[58-63>"
    elif 63<=x<68:
        return "[63-68>"
    elif 68<=x<75:
        return "[68-75>"


# In[20]:


data["EDAD_CAT"]=data["EDAD"].apply(lambda x:cat_edad(x))


# In[21]:


pd.crosstab(data["EDAD_CAT"],data["SEXO"]).style.background_gradient(cmap='summer_r')


# In[26]:


data["DOSIS"].unique()


# In[24]:


temp=pd.crosstab(data["EDAD_CAT"],data["SEXO"]).reset_index().fillna(0)
temp["FEMENINO"]=temp["FEMENINO"]*(-1)
bar_plot = sns.barplot(x='MASCULINO', y=temp["EDAD_CAT"].sort_values(ascending=True), data=temp, order=temp["EDAD_CAT"],label=["M"])

bar_plot = sns.barplot(x='FEMENINO', y=temp['EDAD_CAT'].sort_values(ascending=True), data=temp, order=temp["EDAD_CAT"],label=["F"])

bar_plot.set(xlabel="Population (hundreds of millions)", ylabel="Age-Group", title = "Poblacion Vacunada")
plt.show()


# In[ ]:


depa=gpd.read_file("DEPARTAMENTOS.shp")


# In[ ]:


depa.head()


# In[ ]:


depa["center"] = depa["geometry"].centroid
depa_points = depa.copy()
depa_points.set_geometry("center", inplace = True)


# In[ ]:


data.head()


# In[ ]:


columna=["DOSIS"]
agg={}
for col in columna:
    agg[col]=["sum"]


# In[ ]:


agg_data1=data.groupby(["DEPARTAMENTO"]).agg(agg).reset_index()
agg_data1.columns=[x[0]+'-Total-'+x[1] if x[0]!='DEPARTAMENTO' else x[0] for x in agg_data1.columns]


# In[ ]:


agg_data1.head()


# In[ ]:


agg_data1=agg_data1.rename(columns={"DOSIS-Total-sum":"DOSIS"})


# In[ ]:


agg_data1.sort_values(by="DEPARTAMENTO",inplace=True)


# In[ ]:


agg_data1["IDDPTO"]=np.arange(1,26)
agg_data1['IDDPTO'] = agg_data1['IDDPTO'].astype(str).str.zfill(2)


# In[ ]:


agg_data1=pd.merge(depa,agg_data1,how="left",on="IDDPTO")


# In[ ]:


agg_data1.head()


# In[ ]:


# Añadir la leyenda separada del mapa
from mpl_toolkits.axes_grid1 import make_axes_locatable
import adjustText as aT


# In[ ]:


ax = agg_data1.plot(column="DOSIS",figsize = (10, 10),  cmap='plasma',color = "whitesmoke", legend=True, edgecolor = "lightgrey", linewidth = 0.5)
ax.set_title('Cantidad de Dosis', 
             pad = 20, 
             fontdict={'fontsize':10, 'color': '#4873ab'})
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
texts = []

for x, y, label in zip(depa_points.geometry.x, depa_points.geometry.y, depa_points["DEPARTAMEN"]):
    texts.append(plt.text(x, y, label, fontsize = 8))

aT.adjust_text(texts, force_points=0.3, force_text=0.8, expand_points=(1,1), expand_text=(1,1), 
               arrowprops=dict(arrowstyle="-", color='grey', lw=0.5))
for x, y, label in zip(depa_points.geometry.x, depa_points.geometry.y, agg_data1["DOSIS"]):
    texts.append(plt.text(x, y, label, fontsize = 7))

aT.adjust_text(texts, force_points=0.3, force_text=0.6, expand_points=(1,1), expand_text=(1,1), 
               arrowprops=dict(arrowstyle="-", color='grey', lw=0.5))

plt.savefig('DOSIS_DEPA.png')
plt.show()


# In[ ]:


data.sort_values(by="DEPARTAMENTO",inplace=True)


# In[ ]:


data.head()


# In[ ]:


data["FECHA_VACUNACION"]=data["FECHA_VACUNACION"].astype(np.object)


# In[ ]:


vacunado= data.groupby(['FECHA_VACUNACION']).agg({'DOSIS':['sum']})
fig, (ax1) = plt.subplots(1, 1, figsize=(17,7))
vacunado.plot(ax=ax1)
ax1.set_title("Cantidad de dosis", size=13)
ax1.set_ylabel("Numero de Vacunados", size=13)
ax1.set_xlabel("Date", size=13)


# In[ ]:


adjusted_dates = adjusted_dates.reshape(1, -1)[0]
plt.figure(figsize=(16, 10))
plt.plot(adjusted_dates, world_cases)
plt.plot(adjusted_dates, world_confirmed_avg, linestyle='dashed', color='orange')
plt.title('# of Coronavirus Cases Over Time', size=30)
plt.xlabel('Days Since 1/22/2020', size=30)
plt.ylabel('# of Cases', size=30)
plt.legend(['Worldwide Coronavirus Cases', 'Moving Average {} Days'.format(window)], prop={'size': 20})
plt.xticks(size=20)
plt.yticks(size=20)
plt.show()


# In[ ]:





# **INEI**

# In[67]:


data2=pd.read_excel("/content/Poblacion Peru 2020 Dpto Prov Dist Final INEI-actualizado.xlsx")


# In[68]:


data2


# In[ ]:





# In[ ]:





# In[ ]:




