import streamlit as st 
import pandas as pd
import sqlite3 
import os
# ecrire une fonction qui execute un code sql 
def sql_executor(raw_code, conn):
    pass
# Ecrire une fonction qui donne les noms des tables
def get_table_names(conn):
    pass

def Home():
    st.title("SQLlite with Streamlit and Python")
    # Select Database
    db_file_path = st.text_input("Enter Database File Path:")
    if db_file_path:
        # Check if file exists
        if not os.path.exists(db_file_path):
            st.error("Le fichier spécifié n'existe pas.")
            return

        # Display the selected file path
        st.write("Selected Database Path:", db_file_path)

        # Connect to the database
        conn = sqlite3.connect(db_file_path)
        st.success("Database connected successfully.")
        st.subheader("Database details")
        with st.expander("List of tables"):
            tables = get_table_names(conn)
            st.write("Tables:", tables)  # Debugging message
        st.subheader("Table Details")
        ## Afficher le nom des tables et les détails de chaque colonne pour chaque table 
        def get_details():
            pass





        
        st.subheader("SQL Query")
        # Columns/Layout
        col1,col2 = st.columns(2)

        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area("SQL Code Here")
                submit_code = st.form_submit_button("Execute")

        # Results Layouts
        with col2:
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)

        # Results
        # appliquer la requete avec pandas
        with st.expander("Result of the query"):
            try:

                
            except:
                st.error("Syntax error")
        
        # Table of Info
        
        # Close the database connection
        conn.close()
def About():
    st.subheader("About John Doe")
    st.write("Nom: Doe")
    st.write("Prénom: John")
    st.write("Groupe: Groupe X")
def main():
    # Menu
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice =="Home":
        Home()
    elif choice =="About":
        About()
    
if __name__ == '__main__':
    main()
