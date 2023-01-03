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
streamlit.dataframe(my_fruit_list)


