from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title('Streamlit + Sqlite3')

conn = st.experimental_connection(st.secrets["DB_CONN"])

# print(conn)

if conn is not None:
    st.write('Connected!')

    st.write('Creating table...')
    conn.execute('CREATE TABLE IF NOT EXISTS data (x, y)')
    st.write('Done!')

    st.write('Inserting data...')
    conn.execute('INSERT INTO data VALUES (?, ?)', (1, 1))
    conn.execute('INSERT INTO data VALUES (?, ?)', (2, 4))
    conn.execute('INSERT INTO data VALUES (?, ?)', (3, 9))
    st.write('Done!')

    st.write('Querying...')
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

# with st.echo(code_location='below'):
#     total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#     num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

#     Point = namedtuple('Point', 'x y')
#     data = []

#     points_per_turn = total_points / num_turns

#     for curr_point_num in range(total_points):
#         curr_turn, i = divmod(curr_point_num, points_per_turn)
#         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#         radius = curr_point_num / total_points
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         data.append(Point(x, y))

#     st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#                     .mark_circle(color='#0068c9', opacity=0.5)
#                     .encode(x='x:Q', y='y:Q'))
