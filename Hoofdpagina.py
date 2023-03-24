import pandas as pd
import streamlit as st
import datetime
import plotly.express as px

st.set_page_config(page_title = "ProcessMinded", layout = "wide", page_icon = "beeldmerk_(003).png")

time = datetime.datetime.now().strftime('%H:%M')
day = datetime.date.today().strftime("%A")
date = datetime.datetime.now().strftime("%d/%m/%Y")

#Clock
st.write(f"""<span style='color: black; font-size: 20px'>{day} 
 </span> <span style='color: black; font-size: 20px'>{date}</span>
 </span> <span style='color: black; font-size: 20px'>{time}</span>""", unsafe_allow_html = True)

#hier ergens ook een Weather API voor Gorinchem met huidige temperatuur en weer-omstadigheden plaatje

st.image("https://raw.githubusercontent.com/christos1991t/webpagina/main/logo.png")
st.title("ProcessMinded Dashboard en App Omgeving")

st.markdown(""" Welkom in de Dashboard van ProcessMinded. Hier kunnen jullie alles en wat van handige info over 
ons vinden. Via de menu kunnen jullie ook handige apps kiezen. In deze pagina vinden jullie de kerngetalen van 
ProcessMinded
""")

col1, col_m, col2 = st.columns([1, 0.5, 1])
with col1:
	df = pd.read_excel("test_data.xlsx")
	jaar_list = df['jaar'].tolist()
	st.header("Aantal medewerkers overzicht")
	fig = px.line(df, x = 'jaar', y = 'Medewerkers')
	st.plotly_chart(fig)

with col2:
	st.header("Project Informatie")
	st.subheader("Geografische verdeling PM projecten")
	df2 = pd.read_excel("coor.xlsx")

	# Create the scatter mapbox chart
	map_fig = px.scatter_mapbox(df2, lat = "lat", lon = "lon", hover_name = "Project",
	                            hover_data = ["Status"],
	                            color = "Status", zoom = 10, height = 600, size = "size")

	# Customize the hover information
	map_fig.update_traces(hovertemplate = "<b>%{hovertext}</b><br>Status: %{customdata[0]}")

	# Set the mapbox style and display the chart in Streamlit
	map_fig.update_layout(mapbox_style = "open-street-map")
	st.plotly_chart(map_fig)

