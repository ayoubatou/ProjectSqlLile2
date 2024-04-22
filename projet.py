import streamlit as st
import pandas as pd 
import sqlite3
import os

#fonction de connection à la base de donnée

def connect(chemin):
    return sqlite3.connect(chemin)

def sql_executor(raw_code ,conn):
    c = conn.cursor()
    c.execute(raw_code)
    data = c.fetchall()
    return data

st.title("SQLITE with streanmlit")

chemin = st.text_input(" Enter le chemin de la BD")

if chemin:
    if not os.path.exists(chemin):
        st.error('Le fichier spécifié est introuvable')
    else : 
        conn = connect(chemin)
        st.success("Database connected")
        with st.expander("Liste des tables"):
            sql_table = "SELECT name FROM sqlite_master WHERE type='table';"
            tables = sql_executor(sql_table ,conn)
            st.write(tables)

