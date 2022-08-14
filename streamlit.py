import streamlit as st
import pandas as pd
import requests
import json
from src.reccomendationsystem import RecomendaImoveis

MODEL_URL = f'http://localhost:8000/predict'

st.title ('Calculadora e Recomendações de Aluguel   Brasília/DF')
st.subheader("Preencha os dados e o modelo dirá um valor para os custos mensais de moradia (Aluguel + Condomínio) e também recomendações de imóveis similares anunciados")

def predict_results(url,area,Quartos,setor):
    result = requests.post(f'{url}', json = {'area':area,'Quartos':quartos,'setor':setor})
    prediction = json.loads(result.text)[0]
    prediction = prediction.split('[')[1].split(']')[0]
    st.subheader("Previsão do Valor Total (Aluguel + Condomínio)")
    st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(f'<p class="big-font">R$ {float(prediction):.0f}</p>', unsafe_allow_html=True)
    #st.write(f'**{float(prediction):.0f}**')


with st.form('my_ml'):

    st.subheader('Quartos')
    quartos = st.selectbox("Quartos",
                        [1, 2, 3, 4])

    st.subheader('Área (m²)')
    area = st.slider("Area (m²)", 20, 250)

    st.subheader("Setor")
    nomes_setores = ['SQNW - Superquadra Noroeste - Noroeste', 'SQN - Superquadra Norte - Asa Norte', 'QMSW - Quadras Mistas Sudoeste - Octogonal', 'CCSW - Centro Comercial Sudoeste - Sudoeste',
                'SQS - Superquadra Sul - Asa Sul', 'QRSW - Quadras Regionais Sudoeste ', 'Condomínio - Beira Lago', 'CLSW - Comércio Local Sudoeste - Sudoeste',
            'SHS - Setor Hoteleiro Sul - Asa Sul', 'CLN - Comércio Local Norte - Asa Norte', 'SMAS - Setor de Múltiplas Atividades Sul - Park Sul', 'CA - Centro de Atividades - Lago Norte'
            ,'SQSW - Superquadra Sudoeste - Sudoeste', 'SEPS - Setor de Edíficios Públicos Sul (700) - Asa Sul', 'SCES - Setor de Clubes Esportivos Sul - Asa Sul',
                'SCRN - St. de Habitações Coletivas e Geminadas Norte (700) - Asa Norte', 'SGCV - Setor de Garagens e Concessionárias de Veículos - Park Sul',
            'SHTN - Setor de Hotéis e Turismo Norte - Asa Norte', 'SCEN - Setor de Clubes Esportivos Norte - Asa Norte', 'CLNW - Comércio Local Noroeste - Noroeste', 'SHN - Setor Hoteleiro Norte - Asa Norte'
            , 'SHIN - Setor de Habitações Individuais Nortes - Lago Norte', 'SGAN - Setor de Grandes Areas Norte (900)- Asa Norte', 'AOS - Area Octogonal Sul - Octogonal',
                'CRS - Comércio Residencial Sul (500)', 'STN - Setor Terminal Norte - Asa Norte',
            'QC - Quadra Condominial - Jardins Mangueiral', 'SCLRN - Setor Comercial Local Residencial Norte - Asa Norte',
                'SHCGN -  Setor Habitacional de Casas Geminadas Norte (700)- Asa Norte', 'SGAS - Setor de Grandes Areas Sul (900)- Asa Sul',
                'EQRSW - Entrequadra Regional Sudoeste - Sudoeste', 'SHIGS - Setor de Habitações Individuais Germinadas Sul (700) - Asa Sul', 'CRNW - Comércio Regional Noroeste - Noroeste'
                , 'SMLN - Setor de Mansões do Lago Norte - Lago Norte',
            'SEPN - Setor de Edíficios Públicos Sul (700) - Asa Norte', 'Vila Planalto', 'SCN - Setor Comercial Norte - Asa Norte', 'SMDB - Setor de Mansões Dom Bosco - Lago Sul', 'SIG - Setor de Indústria Gráfica - Sudoeste', 'EQSW - Entrquadra Sudoeste - Sudoeste', 'EQS - Entrequadra Sul - Asa Sul',
            'SHIS - Setor de Habitações Individuais Sul - Lago Sul', 'SHDB - Setor Habitacional Dom Bosco (QL32) - Lago Sul']
    nomes_setores.sort()

    setor = st.selectbox("Setor: ",nomes_setores)


    predict = st.form_submit_button(label = 'Prever Valor do Aluguel + Condomínio')

    dict_renomear = {'SQNW - Superquadra Noroeste - Noroeste':'SQNW',
    'SQN - Superquadra Norte - Asa Norte':'SQN',
    'QMSW - Quadras Mistas Sudoeste - Octogonal':'QMSW',
    'CCSW - Centro Comercial Sudoeste - Sudoeste':'CCSW',
    'SQS - Superquadra Sul - Asa Sul':'SQS',
    'QRSW - Quadras Regionais Sudoeste ':'QRSW',
    'Condomínio - Beira Lago':'Condomínio',
    'CLSW - Comércio Local Sudoeste - Sudoeste':'CLSW',
    'SHS - Setor Hoteleiro Sul - Asa Sul':'SHS',
    'CLN - Comércio Local Norte - Asa Norte':'CLN',
    'SMAS - Setor de Múltiplas Atividades Sul - Park Sul':'SMAS',
    'CA - Centro de Atividades - Lago Norte':'CA',
    'SQSW - Superquadra Sudoeste - Sudoeste':'SQSW',
    'SEPS - Setor de Edíficios Públicos Sul (700) - Asa Sul':'SEPS',
    'SCES - Setor de Clubes Esportivos Sul - Asa Sul':'SCES',
    'SCRN - St. de Habitações Coletivas e Geminadas Norte (700) - Asa Norte':'SCRN',
    'SGCV - Setor de Garagens e Concessionárias de Veículos - Park Sul':'SGVC',
    'SHTN - Setor de Hotéis e Turismo Norte - Asa Norte':'SHTN',
    'SCEN - Setor de Clubes Esportivos Norte - Asa Norte':'SCEN',
    'CLNW - Comércio Local Noroeste - Noroeste':'CLNW',
    'SHN - Setor Hoteleiro Norte - Asa Norte':'SHN',
    'SHIN - Setor de Habitações Individuais Nortes - Lago Norte':'SHIN',
    'SGAN - Setor de Grandes Areas Norte (900)- Asa Norte':'SGAN',
    'AOS - Area Octogonal Sul - Octogonal':'AOS',
    'CRS - Comércio Residencial Sul (500)':'CRS',
    'STN - Setor Terminal Norte - Asa Norte':'STN',
    'QC - Quadra Condominial - Jardins Mangueiral':'QC',
    'SCLRN - Setor Comercial Local Residencial Norte - Asa Norte':'SCLRN',
    'SHCGN -  Setor Habitacional de Casas Geminadas Norte (700)- Asa Norte':'SHCGN',
    'SGAS - Setor de Grandes Areas Sul (900)- Asa Sul':'SGAS',
    'EQRSW - Entrequadra Regional Sudoeste - Sudoeste':'EQRSW',
    'SHIGS - Setor de Habitações Individuais Germinadas Sul (700) - Asa Sul':'SHIGS',
    'CRNW - Comércio Regional Noroeste - Noroeste':'CRNW',
    'SMLN - Setor de Mansões do Lago Norte - Lago Norte':'SMLN',
    'SEPN - Setor de Edíficios Públicos Sul (700) - Asa Norte':'SEPN',
    'Vila Planalto':'Vila Planalto',
    'SCN - Setor Comercial Norte - Asa Norte':'SCN',
    'SMDB - Setor de Mansões Dom Bosco - Lago Sul':'SMDB',
    'SIG - Setor de Indústria Gráfica - Sudoeste':'SIG',
    'EQSW - Entrquadra Sudoeste - Sudoeste':'EQSW',
    'EQS - Entrequadra Sul - Asa Sul':'EQS',
    'SHIS - Setor de Habitações Individuais Sul - Lago Sul':'SHIS',
    'SHDB - Setor Habitacional Dom Bosco (QL32) - Lago Sul':'SHDB'
    }

    setor = dict_renomear[setor]

if predict:
    predict_results(MODEL_URL,area,quartos,setor)
    st.subheader("Recomendações de Imóveis")
    top10 = RecomendaImoveis(area,quartos,setor)
    top10.rename(columns = {'name':'Localização','link':'Link','valor_total':'Valor Total (R$)',
                                    'price':'Aluguel (R$)','Condomínio R$':'Condomínio (R$)', 'area':'Area (m²)','Cidade':'Bairro'
                                    }, inplace = True)
    top10.index += 1
    top10.replace({0:'Não Disponível'}, inplace=True)

    def make_clickable(link):
        text = str(link)
        return f'<a target="_blank" href="{link}">{text}</a>'

    top10['Link'] = top10['Link'].apply(make_clickable)
    top10 = top10.to_html(escape=False)
    st.write(top10, unsafe_allow_html=True)

st.write(f'Modelo treinado em 14/8/2022 com 1875 imóveis extraídos do site www.dfimoveis.com.br ')