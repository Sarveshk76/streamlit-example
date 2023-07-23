from datetime import timedelta
import pandas as pd
import streamlit as st
from sqlalchemy.sql import text
import sqlite3

st.title('Streamlit + Sqlite3')

db = st.file_uploader("db.sqlite3", type="db")

conn = st.experimental_connection("sqlite_db", type="sql")

with conn.session as s:
    st.markdown(f"Note that `s` is a `{type(s)}`")
    s.execute(text('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);'))
    s.execute(text('DELETE FROM pet_owners;'))
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for k in pet_owners:
        s.execute(
            text('INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);'),
            params=dict(owner=k, pet=pet_owners[k])
        )
    s.commit()

pet_owners = conn.query('select * from pet_owners', ttl=timedelta(minutes=10))
st.dataframe(pet_owners)
