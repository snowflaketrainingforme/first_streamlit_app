import streamlit
import pandas

streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥟 Aloo paratha          RS 80')
streamlit.text('Aloo pyaaj paratha        RS 80')
streamlit.text('Paneer paratha            RS 80')
streamlit.text('Gobi paratha              RS 80')

streamlit.header('🍊🍋🍌🥛🧃Make your special smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#setting the index as the fruit name instead of the number
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Apple'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)


