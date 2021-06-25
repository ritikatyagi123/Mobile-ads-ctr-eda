import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
from database import Report
from visualization import *
from AnalyseData import Analyse

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

analysis = Analyse("datasets/dataset.csv")

st.title('Mobile Ads CTR Exploratory Data Analysis')
st.image('logo.png')
sidebar = st.sidebar


def OverView():
    st.header('Project Overview')

    st.markdown("""
        ### In Internet marketing, click-through rate (CTR) is a metric that measures the number of clicks advertisers receive on their ads per number of impressions.
        ### Mobile has become seamless with all channels, and mobile is the driving force with what’s driving all commerce. 
        ### Mobile ads are expected to generate $1.08 billion this year, which would be a 122% jump from last year.
    """)


def viewDataset():
    st.header('Data Used in Project')
    dataframe = analysis.getDataframe()

    with st.spinner("Loading Data..."):
        st.dataframe(dataframe)

        st.markdown('---')
        cols = st.beta_columns(4)
        cols[0].markdown("### No. of Rows :")
        cols[1].markdown(f"# {dataframe.shape[0]}")
        cols[2].markdown("### No. of Columns :")
        cols[3].markdown(f"# {dataframe.shape[1]}")
        st.markdown('---')

        st.header('Summary')
        st.dataframe(dataframe.describe())
        st.markdown('---')

        types = {'object': 'Categorical',
                 'int64': 'Numerical', 'float64': 'Numerical'}
        types = list(map(lambda t: types[str(t)], dataframe.dtypes))
        st.header('Dataset Columns')
        for col, t in zip(dataframe.columns, types):
            st.markdown(f"### {col}")
            cols = st.beta_columns(4)
            cols[0].markdown('#### Unique Values :')
            cols[1].markdown(f"# {dataframe[col].unique().size}")
            cols[2].markdown('#### Type :')
            cols[3].markdown(f"## {t}")


def analyseClicks():

    st.header("Overall banner positions")
    data = analysis.getPositionData()
    st.plotly_chart(
        plotPie(data, "", "xlabel", "ylabel"))

    st.header('Which Banner Position got highest Clicks')
    st.image('images/banner_pos.png', use_column_width=True)

    st.header('Overall Clicks on Mobile Ads')
    st.image('images/click.png', use_column_width=True)

    st.header('At Which time Mobile Ads got most Clicks')
    st.image('images/clicks_day.png', use_column_width=True)

    st.header('No. of Clicks on Week Days')
    st.image('images/clicks_hour.png', use_column_width=True)

    st.header('Highest CTR Banner Position')
    st.image('images/ctr_banner.png', use_column_width=True)

    st.header('Highest CTR Week Days')
    st.image('images/day_week_ctr.png', use_column_width=True)

    st.header('Clicks for Device Type 1')
    st.image('images/device_type_1.png', use_column_width=True)

    st.header('Impressions vs Click on various Device Types')
    st.image('images/device_types.png', use_column_width=True)

    st.header('CTR in different hours of Day')
    st.image('images/hour_ctr.png', use_column_width=True)

    st.header('Impression vs Clicks by Week Days')
    st.image('images/imp_week.png', use_column_width=True)

    st.header('Hourly Impressions vs Clicks')
    st.image('images/imp.png', use_column_width=True)

    st.header('Click Trends by Day Of Week')
    st.image('images/week_trend.png', use_column_width=True)


sidebar.header('Choose Your Option')
options = ['Overview', 'View Dataset', 'CTR Analysis']
choice = sidebar.selectbox(options=options, label="Choose Action")

if choice == options[0]:
    OverView()
elif choice == options[1]:
    viewDataset()
elif choice == options[2]:
    analyseClicks()
