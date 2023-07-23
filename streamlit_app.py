from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title('Streamlit + Sqlite3')

conn = st.experimental_connection("sqlite_db", type="sql")

if conn is not None:
    st.write('Connected!')

    st.write('Creating table...')
    conn.query('CREATE TABLE IF NOT EXISTS data (x, y) RETURNING id;')
    st.write('Done!')

    st.write('Closing connection...')
    conn.close()
    st.write('Done!')

