import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime
import openai

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown("# FIFA23 OFFICIAL DATASET! ⚽")
st.sidebar.markdown("Desenvolvido por [Ryan Zimerman Leite] (https://www.linkedin.com/in/ryanzleite/)")



btn = st.button("Acesse os dados no Kaggle")

if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")

st.markdown(
    """
    Este aplicativo foi desenvolvido para explorar o conjunto de dados oficial do FIFA23, disponível no Kaggle. 
    Utilize o menu lateral para navegar entre as diferentes seções do aplicativo
    O conjunto de dados de jogadores **bla bla bla bla bla**.
    """
)