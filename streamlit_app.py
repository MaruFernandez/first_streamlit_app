import streamlit
streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast Favorites')
streamlit.text('ð¥£ Omega 3 & blueberry oatmeal')
streamlit.text('ð¥ Kale, spinach & Rocket Smoothie')
streamlit.text('ð Hared-Boiled Free-Range egg')
streamlit.text('ð¥ðAvocado Toast')
streamlit.header('ðð¥­ Build Your Own Fruit Smoothie ð¥ð')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list=my_fruit_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show =my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)	

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
