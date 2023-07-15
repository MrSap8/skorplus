import streamlit as st
import pandas as pd

#menu
selected = st.selectbox ('DATASET',
    ('Liga Spanyol',
     'Liga Prancis',
     'Liga Italia',
     'Liga Jerman'))

#halaman Dataset Liga Spanyol
if (selected == 'Liga Spanyol') :
    st.title('Dataset Liga Spanyol')

    #menampilkan data
    dataSP = pd.read_csv('Dataset/spanyol/tes_spanyol.csv')
    dataSP = dataSP[['HomeTeam','AwayTeam','HS','AS','HST','AST','HC','AC','HF','AF',
             'HY','AY','HR','AR','HTHG','HTAG','FTR']]
    st.dataframe(dataSP)

    st.subheader('Keterangan :')

    col1, col2 = st.columns(2)
    with col1 :
        st.caption('HS = Home Team Shots')
        st.caption('AS = Away Team Shots')
        st.caption('HST = Home Team Shots on Target')
        st.caption('AST = Away Team Shots on Target')
        st.caption('HC = Home Team Corners')
        st.caption('AC = Away Team Corners')
        st.caption('HF = Home Team Fouls Committed')
        st.caption('AF = Away Team Fouls Committed')
    with col2 :
        st.caption('HY = Home Team Yellow Cards')
        st.caption('AY = Away Team Yellow Cards')
        st.caption('HR = Home Team Red Cards')
        st.caption('AR = Away Team Red Cards')
        st.caption('HTHG = Half Time Home Team Goals')
        st.caption('HTAG = Half Time Away Team Goals')
        st.caption('FTR= Full Time Result (H=Home Win, D=Draw, A=Away Win)')


#halaman Dataset Liga Prancis
if (selected == 'Liga Prancis') :
    st.title('Dataset Liga Prancis')

    #menampilkan data
    dataF = pd.read_csv('Dataset/france/tes_france.csv')
    dataF = dataF[['HomeTeam','AwayTeam','HS','AS','HST','AST','HC','AC','HF','AF',
             'HY','AY','HR','AR','HTHG','HTAG','FTR']]
    st.dataframe(dataF)

    st.subheader('Keterangan :')
    
    col1, col2 = st.columns(2)
    with col1 :
        st.caption('HS = Home Team Shots')
        st.caption('AS = Away Team Shots')
        st.caption('HST = Home Team Shots on Target')
        st.caption('AST = Away Team Shots on Target')
        st.caption('HC = Home Team Corners')
        st.caption('AC = Away Team Corners')
        st.caption('HF = Home Team Fouls Committed')
        st.caption('AF = Away Team Fouls Committed')
    with col2 :
        st.caption('HY = Home Team Yellow Cards')
        st.caption('AY = Away Team Yellow Cards')
        st.caption('HR = Home Team Red Cards')
        st.caption('AR = Away Team Red Cards')
        st.caption('HTHG = Half Time Home Team Goals')
        st.caption('HTAG = Half Time Away Team Goals')
        st.caption('FTR= Full Time Result (H=Home Win, D=Draw, A=Away Win)')

#halaman Dataset Liga Italia
if (selected == 'Liga Italia') :
    st.title('Dataset Liga Italia')

    #menampilkan data
    dataI = pd.read_csv('Dataset/italy/tes_itali.csv')
    dataI = dataI[['HomeTeam','AwayTeam','HS','AS','HST','AST','HC','AC','HF','AF',
             'HY','AY','HR','AR','HTHG','HTAG','FTR']]
    st.dataframe(dataI)

    st.subheader('Keterangan :')
    
    col1, col2 = st.columns(2)
    with col1 :
        st.caption('HS = Home Team Shots')
        st.caption('AS = Away Team Shots')
        st.caption('HST = Home Team Shots on Target')
        st.caption('AST = Away Team Shots on Target')
        st.caption('HC = Home Team Corners')
        st.caption('AC = Away Team Corners')
        st.caption('HF = Home Team Fouls Committed')
        st.caption('AF = Away Team Fouls Committed')
    with col2 :
        st.caption('HY = Home Team Yellow Cards')
        st.caption('AY = Away Team Yellow Cards')
        st.caption('HR = Home Team Red Cards')
        st.caption('AR = Away Team Red Cards')
        st.caption('HTHG = Half Time Home Team Goals')
        st.caption('HTAG = Half Time Away Team Goals')
        st.caption('FTR= Full Time Result (H=Home Win, D=Draw, A=Away Win)')


#halaman Dataset Liga Jerman
if (selected == 'Liga Jerman') :
    st.title('Dataset Liga Jerman')

    #menampilkan data
    dataD = pd.read_csv('Dataset/germany/tes_jerman.csv')
    dataD = dataD[['HomeTeam','AwayTeam','HS','AS','HST','AST','HC','AC','HF','AF',
             'HY','AY','HR','AR','HTHG','HTAG','FTR']]
    st.dataframe(dataD)

    st.subheader('Keterangan :')
    
    col1, col2 = st.columns(2)
    with col1 :
        st.caption('HS = Home Team Shots')
        st.caption('AS = Away Team Shots')
        st.caption('HST = Home Team Shots on Target')
        st.caption('AST = Away Team Shots on Target')
        st.caption('HC = Home Team Corners')
        st.caption('AC = Away Team Corners')
        st.caption('HF = Home Team Fouls Committed')
        st.caption('AF = Away Team Fouls Committed')
    with col2 :
        st.caption('HY = Home Team Yellow Cards')
        st.caption('AY = Away Team Yellow Cards')
        st.caption('HR = Home Team Red Cards')
        st.caption('AR = Away Team Red Cards')
        st.caption('HTHG = Half Time Home Team Goals')
        st.caption('HTAG = Half Time Away Team Goals')
        st.caption('FTR= Full Time Result (H=Home Win, D=Draw, A=Away Win)')
