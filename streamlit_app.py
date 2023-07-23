from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title('Streamlit + Sqlite3')

conn = st.experimental_connection("sqlite_db", type="sql")
conn