import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import sweetviz as sv
import streamlit as st
import seaborn as sns


df = pd.read_csv('modified_df.csv')
df['date_mutation'] = pd.to_datetime(df['date_mutation'])

st.sidebar.title("Navigation Bar")

@st.cache(suppress_st_warning=True)
def dataframe():
  chart_data = df.head(1000)
  return chart_data

chart_data = dataframe()

if st.sidebar.checkbox('Afficher le dataframe'):
  chart_data
if st.sidebar.checkbox('Afficher les analyses'):
  st.title("Analyse des achats en fonction des départements")
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
  st.pyplot(fig)

  st.title ("Analyse des achats en fonction des caractéristiques du logement")
  test = df.groupby(df['nombre_pieces_principales'],as_index = False)['valeur_fonciere'].mean()
  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  ax.bar(test['nombre_pieces_principales'],test['valeur_fonciere'],width=0.8)
  ax.set_ylabel('Moyenne des valeurs foncieres')
  ax.set_xlabel('Nombre de pièces')
  ax.set_title('Moyenne des valeurs foncieres par nombre de pièces')
  plt.show()
  st.pyplot(fig)

  test = df.groupby(df['code_departement'],as_index = False)['surface_terrain'].mean()
  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  ax.bar(test['code_departement'].head(91),test['surface_terrain'].head(91),width=0.5)
  ax.set_ylabel('Moyenne de la surface du terrain')
  ax.set_xlabel('Départements')
  ax.set_title('Moyenne de la surface du terrain par Département')
  plt.show()
  st.pyplot(fig)

  test = df.groupby(df['nombre_pieces_principales'],as_index = False)['surface_terrain'].mean()
  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  ax.bar(test['nombre_pieces_principales'],test['surface_terrain'],width=0.8)
  ax.set_ylabel('Moyenne de la surface du terrain')
  ax.set_xlabel('Nombre de pièces')
  ax.set_title('Moyenne de la surface du terrain par nombre de pièces')
  plt.show()
  st.pyplot(fig)

  st.title ("Analyse des achats en fonction du point de vue du type de local")
  test = df.groupby(df['type_local'],as_index = False).size()
  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  ax.bar(test['type_local'],test['size'],width=0.5)
  ax.set_ylabel("Nombre d'achats")
  ax.set_xlabel('Type de local')
  ax.set_title("Nombre d'achats par type de local")
  plt.show()
  st.pyplot(fig)

  test = df.groupby(df['type_local'],as_index = False)['valeur_fonciere'].mean()
  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  ax.bar(test['type_local'],test['valeur_fonciere'],width=0.5)
  ax.set_ylabel('Moyenne des valeurs foncieres')
  ax.set_xlabel('Type de local')
  ax.set_title('Moyenne des valeurs foncieres par type de local')
  plt.show()
  st.pyplot(fig)

  test = df.groupby(df['type_local'],as_index = False)['nombre_pieces_principales'].mean()
  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  ax.bar(test['type_local'],test['nombre_pieces_principales'],width=0.5)
  ax.set_ylabel('Moyenne du nombre de pieces principales')
  ax.set_xlabel('Type de local')
  ax.set_title('Moyenne du nombre de pieces principales par type de local')
  plt.show()
  st.pyplot(fig)

  test = df.groupby(df['type_local'],as_index = False)['surface_terrain'].mean()
  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  ax.bar(test['type_local'],test['surface_terrain'],width=0.5)
  ax.set_ylabel('Moyenne de surface de terrain')
  ax.set_xlabel('Type de local')
  ax.set_title('Moyenne $de surface terrain par type de local')
  plt.show()
  st.pyplot(fig)

if st.sidebar.checkbox('Afficher les analyses temporelles'):
  st.title("Analyse des achats en fonction de la période de l'année")
  hist_values = np.histogram(df['date_mutation'].dt.month, bins=12, range=(0.5,12.5))[0]
  st.bar_chart(hist_values)
  st.line_chart(hist_values)
  df2 = df.groupby(['weekday', 'hour']).apply(count_rows).unstack()
  chart_data = df2.head(30)
