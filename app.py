import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
from database import Report
from visualization import plot, plotBar, plotLine
from AnalyseData import Analyse

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

analysis = Analyse("datasets/dataset.csv")

st.title('Mobile Ads CTR EDA')
sidebar = st.sidebar

def viewForm():

    title = st.text_input("Report Title")
    desc = st.text_area('Report Description')
    btn = st.button("Submit")

    if btn:
        report1 = Report(title = title, desc = desc, data = "")
        sess.add(report1)
        sess.commit()
        st.success('Report Saved')

def analyseBannerPos():
    st.header("Analyse Banner Positions\n")

    data = analysis.getPositionData()
    st.plotly_chart(plotBar(data, "title", "xlabel", "ylabel"))

def viewReport():
    reports = sess.query(Report).all()
    titlesList = [ report.title for report in reports ]
    selReport = st.selectbox(options = titlesList, label="Select Report")
    
    reportToView = sess.query(Report).filter_by(title = selReport).first()

    markdown = f"""
        ## {reportToView.title}
        ### {reportToView.desc}
        
    """

    st.markdown(markdown)

sidebar.header('Choose Your Option')
options = [ 'View Database', 'Analyse Mobile Ads Position', 'View Report' ]
choice = sidebar.selectbox( options = options, label="Choose Action" )

if choice == options[1]:
    analyseBannerPos()
elif choice == options[2]:
    analyse()