import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder


selected = st.selectbox ('PREDIKSI',
    ('Liga Spanyol',
     'Liga Prancis',
     'Liga Italia',
     'Liga Jerman'))

if (selected == 'Liga Spanyol') :
    st.title('Prediksi Liga Spanyol')
    
    #load save model
    modelSpain = pickle.load(open('spain.sav', 'rb'))

    col1, col2 = st.columns(2)
    option = {
            "": 'Pilih Tim',
            "36": 'Osasuna',
            "44": 'Sevilla',
            "13": 'Celta Vigo',
            "17": 'Espanyol',
            "50": 'Real Valladolid',
            "52": 'Villarreal',
            "7": 'Barcelona',
            "51": 'Rayo Vallecano',
            "10": 'Cadiz',
            "45": 'Real Sociedad',
            "49": 'Valencia',
            "22": 'Girona',
            "3": 'Almeria',
            "40": 'Real Madrid',
            "5": 'Athletic Bilbao',
            "33": 'Mallorca',
            "6": 'Atletico Madrid',
            "20": 'Getafe',
            "8": 'Real Betis',
            "16": 'Elche',
            "29": 'Levante',
            "15": 'Eibar',
            "24": 'Huesca',
            "28": 'Leganes',
            "0": 'Deportivo Alaves',
        }
    with col1:
        #HomeTeam = st.text_input('Home Team')
        HomeTeam = st.selectbox("Tim Kandang (Home Team)", list(option.keys()), format_func=lambda x: option[x])
    with col2:
        AwayTeam = st.selectbox("Tim Tandang (Away Team)", list(option.keys()), format_func=lambda x: option[x])
    with col1:
        HS = st.text_input('Tendangan Tim Kandang (Home Team Shot)')
    with col2:
        AS = st.text_input('Tendangan Tim Tandang (Away Team Shot)')
    with col1:
        HST = st.text_input('Tendangan Tepat Sasaran Tim Kandang (Home Team Shot on Target)')
    with col2:
        AST = st.text_input('Tendangan Tepat Sasaran Tim Tandang (Away Team Shot on Target)')
    with col1:
        HC = st.text_input('Tendangan Sudut Tim Kandang (Home Team Corner)')
    with col2:
        AC = st.text_input('Tendangan Sudut Tim Tandang (Away Team Corner)')
    with col1:    
        HF = st.text_input('Pelanggaran Tim Kandang (Home Team Fouls)')
    with col2:
        AF = st.text_input('Pelanggaran Tim Tandang (Away Team Fouls)')
    with col1:
        HY = st.text_input('Kartu Kuning Tim Kandang (Home Team Yellow Cards)')
    with col2:
        AY = st.text_input('Kartu Kuning Tim Tandang (Away Team Yellow Cards)')    
    with col1:
        HR = st.text_input('Kartu Merah Tim Kandang (Home Team Red Cards)')
    with col2:
        AR = st.text_input('Kartu Merah Tim Tandang (Away Team Red Cards)')
    with col1:
        HTHG = st.text_input('Skor Babak Pertama Tim Kandang (Home Team Half Time Goals)')
    with col2:
        HTAG = st.text_input('Skor Babak Pertama Tim Tandang (Away Team Half Time Goals)')

    #code prediksi
    hasil_prediksi = ''

    #tombol prediksi
    if st.button('Prediksi'):
        
        prediksi = modelSpain.predict([[HomeTeam, AwayTeam, HS, AS, HST, AST, HC, AC, HF, AF, HY, AY, HR, AR, HTHG, HTAG]])

        st.write("nilai yang dipilih :", HomeTeam)
        st.write("nilai yang dipilih :", AwayTeam)

        if (prediksi==0):
            hasil_prediksi = 'Tim Tandang Menang (A)'
        elif (prediksi==1):
            hasil_prediksi = 'Tidak Ada Tim Yang Menang (D)'
        else:
            hasil_prediksi = 'Tim Kandang Menang (H)'
    st.success(hasil_prediksi)

if (selected == 'Liga Prancis') :
    st.title('Prediksi Liga Prancis')

    #load save model
    modelFrance = pickle.load(open('france.sav', 'rb'))

    col1, col2 = st.columns(2)
    option = {
            "": 'Pilih Tim',
            "25": 'AS Monaco',
            "28": 'Nantes',
            "22": 'Olympique Lyon',
            "8": 'Stade Brestois',
            "45": 'Troyes',
            "34": 'Paris Saint-Germain',
            "39": 'Rennes',
            "19": 'Lens',
            "7": 'Bordeaux',
            "12": 'Clermont Foot',
            "29": 'OGC Nice',
            "38": 'Stade de Reims',
            "42": 'Saint Etienne',
            "21": 'FC Lorient',
            "43": 'Strasbourg',
            "3": 'Angers',
            "24": 'FC Metz',
            "20": 'LOSC Lille',
            "26": 'Montpellier',
            "23": 'Olympique de Marseille',
            "0": 'Ajaccio',
            "44": 'Toulouse',
            "4": 'Auxerre',
            "17": 'Le Havre',
        }
    with col1:
        #HomeTeam = st.text_input('Home Team')
        HomeTeam = st.selectbox("Tim Kandang (Home Team)", list(option.keys()), format_func=lambda x: option[x])
    with col2:
        #AwayTeam = st.text_input('Away Team')
        AwayTeam = st.selectbox("Tim Tandang (Away Team)", list(option.keys()), format_func=lambda x: option[x])
    with col1:
        HS = st.text_input('Tendangan Tim Kandang (Home Team Shot)')
    with col2:
        AS = st.text_input('Tendangan Tim Tandang (Away Team Shot)')
    with col1:
        HST = st.text_input('Tendangan Tepat Sasaran Tim Kandang (Home Team Shot on Target)')
    with col2:
        AST = st.text_input('Tendangan Tepat Sasaran Tim Tandang (Away Team Shot on Target)')
    with col1:
        HC = st.text_input('Tendangan Sudut Tim Kandang (Home Team Corner)')
    with col2:
        AC = st.text_input('Tendangan Sudut Tim Tandang (Away Team Corner)')
    with col1:    
        HF = st.text_input('Pelanggaran Tim Kandang (Home Team Fouls)')
    with col2:
        AF = st.text_input('Pelanggaran Tim Tandang (Away Team Fouls)')
    with col1:
        HY = st.text_input('Kartu Kuning Tim Kandang (Home Team Yellow Cards)')
    with col2:
        AY = st.text_input('Kartu Kuning Tim Tandang (Away Team Yellow Cards)')    
    with col1:
        HR = st.text_input('Kartu Merah Tim Kandang (Home Team Red Cards)')
    with col2:
        AR = st.text_input('Kartu Merah Tim Tandang (Away Team Red Cards)')
    with col1:
        HTHG = st.text_input('Skor Babak Pertama Tim Kandang (Home Team Half Time Goals)')
    with col2:
        HTAG = st.text_input('Skor Babak Pertama Tim Tandang (Away Team Half Time Goals)')

    #code prediksi
    hasil_prediksi = ''

    #tombol prediksi
    if st.button('Prediksi'):
        
        prediksi = modelFrance.predict([[HomeTeam, AwayTeam, HS, AS, HST, AST, HC, AC, HF, AF, HY, AY, HR, AR, HTHG, HTAG]])

        if (prediksi==0):
            hasil_prediksi = 'Tim Tandang Menang'
        elif (prediksi==1):
            hasil_prediksi = 'Tidak Ada Tim Yang Menang (Imbang)'
        else:
            hasil_prediksi = 'Tim Kandang Menang'
    st.success(hasil_prediksi)
    
if (selected == 'Liga Italia') :
    st.title('Prediksi Liga Italia')
    
    #load save model
    modelItaly = pickle.load(open('italy.sav', 'rb'))

    col1, col2 = st.columns(2)
    option = {
            "": 'Pilih Tim',
            "19": 'Inter Milan',
            "18": 'Genoa',
            "48": 'Hellas Verona',
            "40": 'Sassuolo',
            "14": 'Empoli',
            "22": 'Lazio',
            "44": 'Torino',
            "2": 'Atalanta',
            "4": 'Bologna',
            "38": 'Salernitana',
            "46": 'Udinese',
            "21": 'Juventus',
            "27": 'Napoli',
            "47": 'Venezia',
            "37": 'Roma',
            "15": 'Fiorentina',
            "6": 'Cagliari',
            "42": 'Spezia',
            "39": 'Sampdoria',
            "25": 'AC Milan',
            "23": 'Lecce',
            "26": 'Monza',
            "12": 'Cremonese',
            "17": 'Frosinone',
        }
    with col1:
        #HomeTeam = st.text_input('Home Team')
        HomeTeam = st.selectbox("Tim Kandang (Home Team)", list(option.keys()), format_func=lambda x: option[x])
    with col2:
        #AwayTeam = st.text_input('Away Team')
        AwayTeam = st.selectbox("Tim Tandang (Away Team)", list(option.keys()), format_func=lambda x: option[x])
    with col1:
        HS = st.text_input('Tendangan Tim Kandang (Home Team Shot)')
    with col2:
        AS = st.text_input('Tendangan Tim Tandang (Away Team Shot)')
    with col1:
        HST = st.text_input('Tendangan Tepat Sasaran Tim Kandang (Home Team Shot on Target)')
    with col2:
        AST = st.text_input('Tendangan Tepat Sasaran Tim Tandang (Away Team Shot on Target)')
    with col1:
        HC = st.text_input('Tendangan Sudut Tim Kandang (Home Team Corner)')
    with col2:
        AC = st.text_input('Tendangan Sudut Tim Tandang (Away Team Corner)')
    with col1:    
        HF = st.text_input('Pelanggaran Tim Kandang (Home Team Fouls)')
    with col2:
        AF = st.text_input('Pelanggaran Tim Tandang (Away Team Fouls)')
    with col1:
        HY = st.text_input('Kartu Kuning Tim Kandang (Home Team Yellow Cards)')
    with col2:
        AY = st.text_input('Kartu Kuning Tim Tandang (Away Team Yellow Cards)')    
    with col1:
        HR = st.text_input('Kartu Merah Tim Kandang (Home Team Red Cards)')
    with col2:
        AR = st.text_input('Kartu Merah Tim Tandang (Away Team Red Cards)')
    with col1:
        HTHG = st.text_input('Skor Babak Pertama Tim Kandang (Home Team Half Time Goals)')
    with col2:
        HTAG = st.text_input('Skor Babak Pertama Tim Tandang (Away Team Half Time Goals)')

    #code prediksi
    hasil_prediksi = ''

    #tombol prediksi
    if st.button('Prediksi'):
        
        prediksi = modelItaly.predict([[HomeTeam, AwayTeam, HS, AS, HST, AST, HC, AC, HF, AF, HY, AY, HR, AR, HTHG, HTAG]])

        if (prediksi==0):
            hasil_prediksi = 'Tim Tandang Menang'
        elif (prediksi==1):
            hasil_prediksi = 'Tidak Ada Tim Yang Menang (Imbang)'
        else:
            hasil_prediksi = 'Tim Kandang Menang'
    st.success(hasil_prediksi)

if (selected == 'Liga Jerman') :
    st.title('Prediksi Liga Jerman')

    #load save model
    modelGermany = pickle.load(open('germany.sav', 'rb'))

    col1, col2 = st.columns(2)
    option = {
            "": 'Pilih Tim',
            "25": 'Borussia Monchengladbach',
            "1": 'Bayern Munich',
            "0": 'FC Augsburg',
            "20": 'TSG Hoffenheim',
            "2": 'Arminia Bielefeld',
            "13": 'SC Freiburg',
            "36": 'VfB Stuttgart',
            "14": 'Greuther Furth',
            "37": 'Union Berlin',
            "24": 'Bayer Leverkusen',
            "40": 'VfL Wolfsburg',
            "3": 'VfL Bochum',
            "6": 'Borussia Dortmund',
            "9": 'Eintracht Frankfurt',
            "27": 'FSV Mainz 05',
            "31": 'RB Leipzig',
            "11": 'FC Koln',
            "19": 'Hertha Berlin',
            "39": 'Werder Bremen',
            "34": 'Schalke 04',
            "5": 'Darmstadt 98',
            "18": 'FC Heidenheim',
        }
    with col1:
        #HomeTeam = st.text_input('Home Team')
        HomeTeam = st.selectbox("Tim Kandang (Home Team)", list(option.keys()), format_func=lambda x: option[x])
    with col2:
        #AwayTeam = st.text_input('Away Team')
        AwayTeam = st.selectbox("Tim Tandang (Away Team)", list(option.keys()), format_func=lambda x: option[x])
    with col1:
        HS = st.text_input('Tendangan Tim Kandang (Home Team Shot)')
    with col2:
        AS = st.text_input('Tendangan Tim Tandang (Away Team Shot)')
    with col1:
        HST = st.text_input('Tendangan Tepat Sasaran Tim Kandang (Home Team Shot on Target)')
    with col2:
        AST = st.text_input('Tendangan Tepat Sasaran Tim Tandang (Away Team Shot on Target)')
    with col1:
        HC = st.text_input('Tendangan Sudut Tim Kandang (Home Team Corner)')
    with col2:
        AC = st.text_input('Tendangan Sudut Tim Tandang (Away Team Corner)')
    with col1:    
        HF = st.text_input('Pelanggaran Tim Kandang (Home Team Fouls)')
    with col2:
        AF = st.text_input('Pelanggaran Tim Tandang (Away Team Fouls)')
    with col1:
        HY = st.text_input('Kartu Kuning Tim Kandang (Home Team Yellow Cards)')
    with col2:
        AY = st.text_input('Kartu Kuning Tim Tandang (Away Team Yellow Cards)')    
    with col1:
        HR = st.text_input('Kartu Merah Tim Kandang (Home Team Red Cards)')
    with col2:
        AR = st.text_input('Kartu Merah Tim Tandang (Away Team Red Cards)')
    with col1:
        HTHG = st.text_input('Skor Babak Pertama Tim Kandang (Home Team Half Time Goals)')
    with col2:
        HTAG = st.text_input('Skor Babak Pertama Tim Tandang (Away Team Half Time Goals)')

    #code prediksi
    hasil_prediksi = ''

    #tombol prediksi
    if st.button('Prediksi'):
        
        prediksi = modelGermany.predict([[HomeTeam, AwayTeam, HS, AS, HST, AST, HC, AC, HF, AF, HY, AY, HR, AR, HTHG, HTAG]])

        if (prediksi==0):
            hasil_prediksi = 'Tim Tandang Menang'
        elif (prediksi==1):
            hasil_prediksi = 'Tidak Ada Tim Yang Menang (Imbang)'
        else:
            hasil_prediksi = 'Tim Kandang Menang'
    st.success(hasil_prediksi)