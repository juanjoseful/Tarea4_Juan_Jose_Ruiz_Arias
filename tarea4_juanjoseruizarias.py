#!/usr/bin/env python
# coding: utf-8

# In[47]:


import numpy as np
import pandas as pd


base=pd.read_csv('C:/Users/Vaio/Desktop/juan/tarea4/exoplanets.csv')
base = base.drop(base[base['BINARY']==0].index) #elimino los binario ==0


base_NAME = base['NAME']  #tomo la columna de NAME
base_TEFF = base['TEFF']  #tomo la columna de TEFF
base_MASS = base['MASS']  
base_A = base['A']  
base_DENSITY = base['DENSITY']  
base_R = base['R']  
base_STAR = base['STAR']  
base_MSTAR = base['MSTAR']  
base_RSTAR = base['RSTAR']  
base_BINARY = base['BINARY']  

base_juntas = pd.DataFrame()   #creo un DataFrame vacio para llenarlo
                                #de las columnas que necesito

base_juntas["NAME"]=(base_NAME)  #agrego una columna NAME
base_juntas["TEFF"]=(base_TEFF) 
base_juntas["MASS"]=(base_MASS)  
base_juntas["A"]=(base_A)  
base_juntas["DENSITY"]=(base_DENSITY)  
base_juntas["R"]=(base_R)  
base_juntas["STAR"]=(base_STAR)
base_juntas["MSTAR"]=(base_MSTAR)
base_juntas["RSTAR"]=(base_RSTAR)
base_juntas["BINARY"]=(base_BINARY)  
  
  
df = pd.DataFrame(base_juntas)
df.to_excel('datosfiltro1.xlsx')

#cargo la nueva base de datos con lo que me sirve
filtro1 = pd.read_excel('C:/Users/Vaio/Desktop/juan/tarea4/datosfiltro1.xlsx')


masa_jupiter = 1.898e27 #kg
masa_tierra = 5.972e24 #kg
#creo una nueva columna con masa respecto a la terrestre
filtro1["MASSE"] = (filtro1["MSTAR"]*(masa_tierra/masa_jupiter)*0.1)

respectomasatierra = pd.DataFrame(filtro1)
respectomasatierra.to_excel('respectoMasaTierra.xlsx') 


filtro2 = pd.read_excel('C:/Users/Vaio/Desktop/juan/tarea4/respectoMasaTierra.xlsx')

#radio respecto al radio terrestre

radiojupiter = 69911e6 #metros
radiotierra = 6371e6 #metros

#creo una nueva columna con nuevo radio respecto al terrestre
filtro2["RE"] = (filtro2["R"]*(radiotierra/radiojupiter)) 

respectoradiotierra = pd.DataFrame(filtro2)
respectoradiotierra.to_excel('respectoRadioTierra.xlsx')

#creacion de la columna LUM

    #cargo el archivo con los radios respecto al terrestre
filtro3 = pd.read_excel('C:/Users/Vaio/Desktop/juan/tarea4/respectoRadioTierra.xlsx')
 
sigma = 5.67e-8 #constante Stefan-Boltzmann en [watts/(m2K4)]
 
filtro3["LUM"] = 4*np.pi*pow(filtro3["RE"],2)*sigma*pow(filtro3["TEFF"],4)
 
adiciondeLUM = pd.DataFrame(filtro3)
adiciondeLUM.to_excel('concolumnaLUM.xlsx')


# In[48]:


#los limites de la zona de habitabilidad son:

T_s = 5780 #kelvin
a_i = 2.7619e-5
b_i = 3.8095e-9
a_o = 1.3786e-4
b_o = 1.4286e-9    
r_is = 0.72
r_os = 1.77

filtro4 = pd.read_excel('C:/Users/Vaio/Desktop/juan/tarea4/concolumnaLUM.xlsx')   #cargando el archivo filtrado hasta ahora



# limite interior
filtro4["ri"] = (r_is - a_i*(filtro4["TEFF"]- T_s) - b_i*pow(filtro4["TEFF"] - T_s,2))*pow(filtro4["LUM"], 0.5)
filtro4["ro"] = (r_os - a_o*(filtro4["TEFF"]-T_s)- b_o * pow(filtro4["TEFF"]-T_s,2))*pow(filtro4["LUM"],0.5)

adiciondelimiteinterior = pd.DataFrame(filtro4)
adiciondelimiteinterior.to_excel('conColumna-riyro.xlsx')


# In[67]:


#probabilidad de ser rocosos

filtro5 = pd.read_excel('C:/Users/Vaio/Desktop/juan/tarea4/conColumna-riyro.xlsx')   #cargando el archivo filtrado hasta ahora


# In[68]:


filtro5 = filtro5.drop(filtro5[filtro5['DENSITY']<5].index) #elimino los DENSITY < 5


# In[77]:


#zona de habitabilidad es HZD
filtro5["HZD"] = (2*filtro5["A"] - filtro5["ro"] -filtro5["ri"])/(filtro5["ro"]-filtro5["ri"])


# In[78]:


adiciondeHZD = pd.DataFrame(filtro5)
adiciondeHZD.to_excel('conHZD.xlsx')


# In[79]:


fitro5 = filtro5.dropna()  #elimino las filas que tengan valores NanN


# In[80]:


filtro5 = filtro5.drop(filtro5[filtro5['A']<0.7].index) #elimino distancia a la estrella < 0.7


# In[81]:


filtro5 = filtro5.drop(filtro5[filtro5['A']>1.7].index) #elimino distancia a la estrella < 1.7


# In[82]:


#adiciondeHZD = pd.DataFrame(filtro5)
#adiciondeHZD.to_excel('conHZD.xlsx')


# In[83]:


filtro5.plot(kind='scatter',x='MASSE',y='A',color='blue')


# In[90]:


filtro5["A"].plot.hist(bins=10, color='#F2AB6D', rwidth=0.85) # generamos el histograma a partir de los datos


# In[96]:


filtro5.plot(kind='scatter',x='DENSITY',y='MSTAR',color='blue')


# In[94]:


filtro5.plot(kind='scatter',x='A',y='TEFF',color='RED')


# In[ ]:




