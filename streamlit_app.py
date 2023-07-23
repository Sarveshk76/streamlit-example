from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title('Streamlit + Sqlite3')

conn = st.experimental_connection("sqlite_db", type="sql")
conn = conn.cursor()
if conn is not None:
    st.write('Connected!')

    st.write('Creating table...')
    conn.execute('CREATE TABLE IF NOT EXISTS data (x, y);')
    st.write('Done!')
    st.write('Inserting data...')
    conn.execute('INSERT INTO data VALUES (?, ?)', (1, 1))
    conn.execute('INSERT INTO data VALUES (?, ?)', (2, 4))
    conn.execute('INSERT INTO data VALUES (?, ?)', (3, 9))
    st.write('Done!')

    st.write('executeing...')
    data = conn.execute('SELECT * FROM data').fetchall()
    st.write('Done!')

    st.write('Data:')
    st.write(data)

    st.write('Plotting...')
    df = pd.DataFrame(data, columns=['x', 'y'])
    st.write(alt.Chart(df).mark_line().encode(x='x', y='y'))
    st.write('Done!')
    st.write('Closing connection...')
    conn.close()
    st.write('Done!')

