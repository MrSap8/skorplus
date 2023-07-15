import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import xgboost as xgb
import lightgbm as lgb
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

#menu
selected = st.selectbox ('PROSES',
    ('Liga Spanyol',
     'Liga Prancis',
     'Liga Italia',
     'Liga Jerman'))

#Halaman Proses Liga Spanyol
if (selected == 'Liga Spanyol') :
    st.title('Proses Prediksi Dengan Data Liga Spanyol')

    #menampilkan data
    dataset = pd.read_csv('Dataset/spanyol/tes_spanyol.csv')
    
    #mengubah string ke integer
    le=LabelEncoder()
    dataset['HomeTeam']=le.fit_transform(dataset['HomeTeam'])
    dataset['AwayTeam']=le.fit_transform(dataset['AwayTeam'])
    dataset['FTR']=le.fit_transform(dataset['FTR'])

    #membagi data menjadi atribut dan label
    X = dataset[dataset.columns[0:16]]
    Y = dataset['FTR']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

    #model XGBoost
    grSpain = xgb.XGBClassifier(random_state=10)
    grSpain.fit(X_train, y_train)
    grSpain_pred = grSpain.predict(X_test)
    print("pred", grSpain_pred)  #hasil prediksi 
    print("tes", y_test)  #jawaban yang sebenarnya
    print(metrics.accuracy_score(y_test, grSpain_pred))
    print(classification_report(y_test,grSpain_pred))

    #model LightGBM
    lgbSpain = lgb.LGBMClassifier(random_state=10)
    lgbSpain.fit(X_train, y_train)
    lgbSpain_pred = lgbSpain.predict(X_test)
    print(lgbSpain_pred)  #hasil prediksi 
    print(y_test)  #jawaban yang sebenarnya
    print(metrics.accuracy_score(y_test, lgbSpain_pred))
    print(classification_report(y_test,lgbSpain_pred))

    #model AdaBoost
    abSpain = AdaBoostClassifier(random_state=10, learning_rate=0.20)
    abSpain.fit(X_train, y_train)
    abSpain_pred = abSpain.predict(X_test)
    print(abSpain_pred)  #hasil prediksi 
    print(y_test)  #jawaban yang sebenarnya
    print(metrics.accuracy_score(y_test, abSpain_pred))
    print(classification_report(y_test,abSpain_pred))


    st.write('Pertama data yang bertipe string (huruf) diubah ke integer (angka) terlebih dahulu menggunakan label encoder. Setelah diubah menjadi integer hasilnya seperti dibawah ini')
  
    st.dataframe(dataset)

    st.write('Kemudian dataset dibagi menjadi atribut dan target, setelah itu atribut dan target akan dipisah lagi menjadi data train dan data test menggunakan TrainTestSplit dengan perbandingan data train dan data test sebesar 80:20')
    st.write('Data train yang telah dipisah digunakan untuk membangun model. Algoritma yang digunakan yaitu XGBoost, LightGBM, dan AdaBoost')

    st.subheader('Model XGBoost')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write('akurasi = ')
    with col2:
        st.text(metrics.accuracy_score(y_test, grSpain_pred))
    st.text(classification_report(y_test,grSpain_pred))
    
    st.subheader('Model LightGBM')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write('akurasi = ')
    with col2:
        st.text(metrics.accuracy_score(y_test, lgbSpain_pred))
    st.text(classification_report(y_test,lgbSpain_pred))

    st.subheader('Model AdaBoost')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write('akurasi = ')
    with col2:
        st.text(metrics.accuracy_score(y_test, abSpain_pred))
    st.text(classification_report(y_test,abSpain_pred))

    #diagram
    st.subheader("Akurasi Algoritma XGBoost, LightGBM, dan AdaBoost")
    # Data
    labels = ['XGBoost', 'LightGBM', 'AdaBoost']
    values = [metrics.accuracy_score(y_test, grSpain_pred), metrics.accuracy_score(y_test, lgbSpain_pred), metrics.accuracy_score(y_test, abSpain_pred)]
    # Warna untuk setiap batang
    colors = ['red', 'green', 'blue']
    # Membuat diagram batang dengan warna yang berbeda
    fig, ax = plt.subplots(figsize=(8, 5), facecolor='lightgray')
    ax.set_ylabel("Akurasi")
    ax.set_xlabel("Algoritma")
    ax.bar(labels, values, color=colors)
    ax.set_ylim(0, 0.7)
    # Menampilkan diagram batang
    st.pyplot(fig)


#Halaman Proses Liga Prancis
if (selected == 'Liga Prancis') :
    st.title('Proses Prediksi Dengan Data Liga Prancis')

    dataset = pd.read_csv('Dataset/france/tes_france.csv')

    le=LabelEncoder()
    dataset['HomeTeam']=le.fit_transform(dataset['HomeTeam'])
    dataset['AwayTeam']=le.fit_transform(dataset['AwayTeam'])
    dataset['FTR']=le.fit_transform(dataset['FTR'])

    X = dataset[dataset.columns[0:16]]
    Y = dataset['FTR']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

    #Model XGBoost 
    grFrance = xgb.XGBClassifier(random_state=10)
    grFrance.fit(X_train, y_train)
    grFrance_pred = grFrance.predict(X_test)
    print(grFrance_pred)  #hasil prediksi 
    print(y_test)  #jawaban yang sebenarnya
    print(metrics.accuracy_score(y_test, grFrance_pred))
    print(classification_report(y_test,grFrance_pred))

    #Model LightGBM
    lgbFrance = lgb.LGBMClassifier(random_state=10)
    lgbFrance.fit(X_train, y_train)
    lgbFrance_pred = lgbFrance.predict(X_test)
    print(lgbFrance_pred)  #hasil prediksi 
    print(y_test)  #jawaban yang sebenarnya
    print(metrics.accuracy_score(y_test, lgbFrance_pred))
    print(classification_report(y_test,lgbFrance_pred))

    #Model AdaBoost
    abFrance = AdaBoostClassifier(random_state=10, learning_rate=0.20)
    abFrance.fit(X_train, y_train)
    abFrance_pred = abFrance.predict(X_test)
    print(abFrance_pred)  #hasil prediksi 
    print(y_test)  #jawaban yang sebenarnya
    print(metrics.accuracy_score(y_test, abFrance_pred))
    print(classification_report(y_test,abFrance_pred))

    st.write('Pertama data yang bertipe string (huruf) diubah ke integer (angka) terlebih dahulu menggunakan label encoder. Setelah diubah menjadi integer hasilnya seperti dibawah ini')

    st.dataframe(dataset)

    st.write('Kemudian dataset dibagi menjadi atribut dan target, setelah itu atribut dan target akan dipisah lagi menjadi data train dan data test menggunakan TrainTestSplit dengan perbandingan data train dan data test sebesar 80:20')
    st.write('Data train yang telah dipisah digunakan untuk membangun model. Algoritma yang digunakan yaitu XGBoost, LightGBM, dan AdaBoost')

    st.subheader('Model XGBoost')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text('akurasi = ')
    with col2:
        st.text(metrics.accuracy_score(y_test, grFrance_pred))
    st.text(classification_report(y_test,grFrance_pred))

    st.subheader('Model LightGBM')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text('akurasi = ')
    with col2:
        st.text(metrics.accuracy_score(y_test, lgbFrance_pred))
    st.text(classification_report(y_test,lgbFrance_pred))

    st.subheader('Model AdaBoost')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text('akurasi = ')
    with col2:
        st.text(metrics.accuracy_score(y_test, abFrance_pred))
    st.text(classification_report(y_test,abFrance_pred))

    #diagram
    st.subheader("Akurasi Algoritma XGBoost, LightGBM, dan AdaBoost")
    # Data
    labels = ['XGBoost', 'LightGBM', 'AdaBoost']
    values = [metrics.accuracy_score(y_test, grFrance_pred), metrics.accuracy_score(y_test, lgbFrance_pred), metrics.accuracy_score(y_test, abFrance_pred)]
    # Warna untuk setiap batang
    colors = ['red', 'green', 'blue']
    # Membuat diagram batang dengan warna yang berbeda
    fig, ax = plt.subplots(figsize=(8, 5), facecolor='lightgray')
    ax.set_ylabel("Akurasi")
    ax.set_xlabel("Algoritma")
    ax.bar(labels, values, color=colors)
    ax.set_ylim(0, 0.7)
    # Menampilkan diagram batang
    st.pyplot(fig)

#Halaman Proses Liga Italia
if (selected == 'Liga Italia') :
    st.title('Proses Prediksi Dengan Data Liga Italia')

    dataset = pd.read_csv('Dataset/italy/tes_itali.csv')

    rata2=dataset['HF'].mean()
    dataset['HF']=dataset['HF'].fillna(rata2)
    rata2=dataset['AF'].mean()
    dataset['AF']=dataset['AF'].fillna(rata2)

    le=LabelEncoder()
    dataset['HomeTeam']=le.fit_transform(dataset['HomeTeam'])
    dataset['AwayTeam']=le.fit_transform(dataset['AwayTeam'])
    dataset['FTR']=le.fit_transform(dataset['FTR'])

    X = dataset[dataset.columns[0:16]]
    Y = dataset['FTR']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

    grItaly = xgb.XGBClassifier(random_state=10)
    grItaly.fit(X_train, y_train)
    grItaly_pred = grItaly.predict(X_test)
    print("pred", grItaly_pred)  #hasil prediksi 
    print("tes", y_test)  #jawaban yang sebenarnya
    print(metrics.accuracy_score(y_test, grItaly_pred))
    print(classification_report(y_test,grItaly_pred))

    lgbItaly = lgb.LGBMClassifier(random_state=10)
    lgbItaly.fit(X_train, y_train)
    lgbItaly_pred = lgbItaly.predict(X_test)
    print(lgbItaly_pred)  #hasil prediksi 
    print(y_test)  #jawaban yang sebenarnya
    print(metrics.accuracy_score(y_test, lgbItaly_pred))
    print(classification_report(y_test,lgbItaly_pred))

    abItaly = AdaBoostClassifier(random_state=10, learning_rate=0.20)
    abItaly.fit(X_train, y_train)
    abItaly_pred = abItaly.predict(X_test)
    print(abItaly_pred)  #hasil prediksi 
    print(y_test)  #jawaban yang sebenarnya
    print(metrics.accuracy_score(y_test, abItaly_pred))
    print(classification_report(y_test,abItaly_pred))

    st.write('Pertama data yang bertipe string (huruf) diubah ke integer (angka) terlebih dahulu menggunakan label encoder. Setelah diubah menjadi integer hasilnya seperti dibawah ini')

    st.dataframe(dataset)

    st.write('Kemudian dataset dibagi menjadi atribut dan target, setelah itu atribut dan target akan dipisah lagi menjadi data train dan data test menggunakan TrainTestSplit dengan perbandingan data train dan data test sebesar 80:20')
    st.write('Data train yang telah dipisah digunakan untuk membangun model. Algoritma yang digunakan yaitu XGBoost, LightGBM, dan AdaBoost')


    st.subheader('model XGBoost')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text('akurasi = ')
    with col2:
        st.text(metrics.accuracy_score(y_test, grItaly_pred))
    st.text(classification_report(y_test,grItaly_pred))

    st.subheader('model LightGBM')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text('akurasi = ')
    with col2:
        st.text(metrics.accuracy_score(y_test, lgbItaly_pred))
    st.text(classification_report(y_test,lgbItaly_pred))

    st.subheader('model AdaBoost')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text('akurasi = ')
    with col2:
        st.text(metrics.accuracy_score(y_test, abItaly_pred))
    st.text(classification_report(y_test,abItaly_pred))

    #diagram
    st.subheader("Akurasi Algoritma XGBoost, LightGBM, dan AdaBoost")
    # Data
    labels = ['XGBoost', 'LightGBM', 'AdaBoost']
    values = [metrics.accuracy_score(y_test, grItaly_pred), metrics.accuracy_score(y_test, lgbItaly_pred), metrics.accuracy_score(y_test, abItaly_pred)]
    # Warna untuk setiap batang
    colors = ['red', 'green', 'blue']
    # Membuat diagram batang dengan warna yang berbeda
    fig, ax = plt.subplots(figsize=(8, 5), facecolor='lightgray')
    ax.set_ylabel("Akurasi")
    ax.set_xlabel("Algoritma")
    ax.bar(labels, values, color=colors)
    ax.set_ylim(0, 0.7)
    # Menampilkan diagram batang
    st.pyplot(fig)

#Halaman Proses Liga Jerman
if (selected == 'Liga Jerman') :
    st.title('Proses Prediksi Dengan Data Liga Jerman')

    dataset = pd.read_csv('Dataset/germany/tes_jerman.csv')

    le=LabelEncoder()
    dataset['HomeTeam']=le.fit_transform(dataset['HomeTeam'])
    dataset['AwayTeam']=le.fit_transform(dataset['AwayTeam'])
    dataset['FTR']=le.fit_transform(dataset['FTR'])

    X = dataset[dataset.columns[0:16]]
    Y = dataset['FTR']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

    grGermany = xgb.XGBClassifier(random_state=10)
    grGermany.fit(X_train, y_train)
    grGermany_pred = grGermany.predict(X_test)
    print("pred", grGermany_pred)  #hasil prediksi 
    print("tes", y_test)  #jawaban yang sebenarnya
    print(metrics.accuracy_score(y_test, grGermany_pred))
    print(classification_report(y_test,grGermany_pred))

    lgbGermany = lgb.LGBMClassifier(random_state=10)
    lgbGermany.fit(X_train, y_train)
    lgbGermany_pred = lgbGermany.predict(X_test)
    print(lgbGermany_pred)  #hasil prediksi 
    print(y_test)  #jawaban yang sebenarnya
    print(metrics.accuracy_score(y_test, lgbGermany_pred))
    print(classification_report(y_test,lgbGermany_pred))

    abGermany = AdaBoostClassifier(random_state=10, learning_rate=0.20)
    abGermany.fit(X_train, y_train)
    abGermany_pred = abGermany.predict(X_test)
    print(abGermany_pred)  #hasil prediksi 
    print(y_test)  #jawaban yang sebenarnya
    print(metrics.accuracy_score(y_test, abGermany_pred))
    print(classification_report(y_test,abGermany_pred))

    st.write('Pertama data yang bertipe string (huruf) diubah ke integer (angka) terlebih dahulu menggunakan label encoder. Setelah diubah menjadi integer hasilnya seperti dibawah ini')

    st.dataframe(dataset)

    st.write('Kemudian dataset dibagi menjadi atribut dan target, setelah itu atribut dan target akan dipisah lagi menjadi data train dan data test menggunakan TrainTestSplit dengan perbandingan data train dan data test sebesar 80:20')
    st.write('Data train yang telah dipisah digunakan untuk membangun model. Algoritma yang digunakan yaitu XGBoost, LightGBM, dan AdaBoost')


    st.subheader('model XGBoost')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text('akurasi = ')
    with col2:
        st.text(metrics.accuracy_score(y_test, grGermany_pred))
    st.text(classification_report(y_test,grGermany_pred))

    st.subheader('model LightGBM')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text('akurasi = ')
    with col2:
        st.text(metrics.accuracy_score(y_test, lgbGermany_pred))
    st.text(classification_report(y_test,lgbGermany_pred))

    st.subheader('model AdaBoost')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text('akurasi = ')
    with col2:
        st.text(metrics.accuracy_score(y_test, abGermany_pred))
    st.text(classification_report(y_test,abGermany_pred))

    #diagram
    st.subheader("Akurasi Algoritma XGBoost, LightGBM, dan AdaBoost")
    # Data
    labels = ['XGBoost', 'LightGBM', 'AdaBoost']
    values = [metrics.accuracy_score(y_test, grGermany_pred), metrics.accuracy_score(y_test, lgbGermany_pred), metrics.accuracy_score(y_test, abGermany_pred)]
    # Warna untuk setiap batang
    colors = ['red', 'green', 'blue']
    # Membuat diagram batang dengan warna yang berbeda
    fig, ax = plt.subplots(figsize=(8, 5), facecolor='lightgray')
    ax.set_ylabel("Akurasi")
    ax.set_xlabel("Algoritma")
    ax.bar(labels, values, color=colors)
    ax.set_ylim(0, 0.7)
    # Menampilkan diagram batang
    st.pyplot(fig)
