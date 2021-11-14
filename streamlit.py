import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import sweetviz as sv
import streamlit as st


df = pd.read_csv('modified_df.csv')

@st.cache(suppress_st_warning=True)
def dataframe():
  chart_data = df.head(100)
  return chart_data

chart_data = dataframe()
chart_data

test = df.groupby(df['code_departement'],as_index = False).size()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(test['code_departement'].head(91),test['size'].head(91))
ax.set_ylabel("Nombre d'achats")
ax.set_xlabel('Départements')
ax.set_title("Nombre d'achats par departement")
plt.show()
st.pyplot(fig)

test = df.groupby(df['code_departement'],as_index = False)['valeur_fonciere'].mean()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(test['code_departement'].head(91),test['valeur_fonciere'].head(91),width=0.8)
ax.set_ylabel('Moyenne des valeurs foncieres')
ax.set_xlabel('Départements')
ax.set_title('Moyenne des valeurs foncieres par Département')
plt.show()

test = df.groupby(df['nombre_pieces_principales'],as_index = False)['valeur_fonciere'].mean()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(test['nombre_pieces_principales'],test['valeur_fonciere'],width=0.8)
ax.set_ylabel('Moyenne des valeurs foncieres')
ax.set_xlabel('Nombre de pièces')
ax.set_title('Moyenne des valeurs foncieres par nombre de pièces')
plt.show()

test = df.groupby(df['code_departement'],as_index = False)['surface_terrain'].mean()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(test['code_departement'].head(91),test['surface_terrain'].head(91),width=0.5)
ax.set_ylabel('Moyenne de la surface du terrain')
ax.set_xlabel('Départements')
ax.set_title('Moyenne de la surface du terrain par Département')
plt.show()

test = df.groupby(df['nombre_pieces_principales'],as_index = False)['surface_terrain'].mean()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(test['nombre_pieces_principales'],test['surface_terrain'],width=0.8)
ax.set_ylabel('Moyenne de la surface du terrain')
ax.set_xlabel('Nombre de pièces')
ax.set_title('Moyenne de la surface du terrain par nombre de pièces')
plt.show()

test = df.groupby(df['type_local'],as_index = False).size()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(test['type_local'],test['size'],width=0.5)
ax.set_ylabel("Nombre d'achats")
ax.set_xlabel('Type de local')
ax.set_title("Nombre d'achats par type de local")
plt.show()

test = df.groupby(df['type_local'],as_index = False)['valeur_fonciere'].mean()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(test['type_local'],test['valeur_fonciere'],width=0.5)
ax.set_ylabel('Moyenne des valeurs foncieres')
ax.set_xlabel('Type de local')
ax.set_title('Moyenne des valeurs foncieres par type de local')
plt.show()

test = df.groupby(df['type_local'],as_index = False)['nombre_pieces_principales'].mean()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(test['type_local'],test['nombre_pieces_principales'],width=0.5)
ax.set_ylabel('Moyenne du nombre de pieces principales')
ax.set_xlabel('Type de local')
ax.set_title('Moyenne du nombre de pieces principales par type de local')
plt.show()

test = df.groupby(df['type_local'],as_index = False)['surface_terrain'].mean()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(test['type_local'],test['surface_terrain'],width=0.5)
ax.set_ylabel('Moyenne de surface de terrain')
ax.set_xlabel('Type de local')
ax.set_title('Moyenne $de surface terrain par type de local')
plt.show()