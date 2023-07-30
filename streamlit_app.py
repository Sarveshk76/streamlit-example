from datetime import timedelta
import pandas as pd
import streamlit as st
from sqlalchemy.sql import text

st.title('OrderSense - Order Management System')

# tabs for the app
tab1, tab2, tab3 = st.tabs(["Take the order", "Order List", "Weekly Report"])

# tab1 - take the order
tab1.title('Take the order')
tab1.subheader('Please enter the order details below')

# order details
order_date = tab1.date_input('Order Date', pd.to_datetime('today'))
order_time = tab1.time_input('Order Time', pd.to_datetime('now'))
order_type = tab1.selectbox('Order Type', ['Dine In', 'Take Away', 'Delivery'])
order_table = tab1.number_input(
    'Table Number', min_value=1, max_value=10, value=1)
order_name = tab1.text_input('Customer Name')

col1, col2 = st.columns(3)

# order items
item_list = []
quantity_list = []

with col1:
    add_item = tab1.button('Add Item')
    if add_item:
        item = tab1.selectbox('Item', ['Chicken Burger', 'Beef Burger',
                            'Fish Burger', 'Chicken Nuggets', 'French Fries', 'Coke'])
        quantity = tab1.number_input(
            'Quantity', min_value=1, max_value=10, value=1)
        item_list.append(item)
        quantity_list.append(quantity)

with col2:
    # show order summary
    order_summary = pd.DataFrame(
        {'Item': item_list, 'Quantity': quantity_list})
    tab1.dataframe(order_summary)


# submit order
submit = tab1.button('Submit')
if submit:
    order_summary = pd.DataFrame(
        {'Item': item_list, 'Quantity': quantity_list})
    tab1.dataframe(order_summary)


# tab2 - order list
tab2.title('Order List')
tab2.subheader('Please select the order date below')


# tab3 - weekly report
tab3.title('Weekly Report')
tab3.subheader('Please select the week below')
# conn = st.experimental_connection("sqlite_db", type="sql")

# with conn.session as s:
#     st.markdown(f"Note that `s` is a `{type(s)}`")
#     s.execute(text('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);'))
#     s.execute(text('DELETE FROM pet_owners;'))
#     pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
#     for k in pet_owners:
#         s.execute(
#             text('INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);'),
#             params=dict(owner=k, pet=pet_owners[k])
#         )
#     s.commit()

# pet_owners = conn.query('select * from pet_owners', ttl=timedelta(minutes=10))
# st.dataframe(pet_owners)
