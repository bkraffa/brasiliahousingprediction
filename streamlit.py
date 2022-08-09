import streamlit as st
import pandas as pd
import requests
import json

MODEL_URL = f'http://localhost:8000/predict'

st.title ('Calculadora do Custo de Moradia   Brasília/DF')
st.subheader("Preencha os dados com a simulação desejada e o modelo dirá um valor para os custos mensais de moradia (Aluguel + Condomínio")

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
    setores = ['SQNW', 'SQN', 'QMSW', 'CCSW', 'SQS', 'QRSW', 'Condomínio', 'CLSW',
            'SHS', 'CLN', 'SMAS', 'CA', 'SQSW', 'SEPS', 'SCES', 'SCRN', 'SGCV',
            'SHTN', 'SCEN', 'CLNW', 'SHN', 'SHIN', 'SGAN', 'AOS', 'CRS', 'STN',
            'QC', 'SCLRN', 'SHCGN', 'SGAS', 'EQRSW', 'SHIGS', 'CRNW', 'SMLN',
            'SEPN', 'Vila Planalto', 'SCN', 'SMDB', 'SIG', 'EQSW', 'EQS',
            'SHIS', 'SHDB']
    setores.sort()
#    nomes_setores = ['SQNW - Superquadra Noroeste - Noroeste', 'SQN - Superquadra Norte - Asa Norte', 'QMSW - Quadras Mistas Sudoeste - Octogonal', 'CCSW - Centro Comercial Sudoeste - Sudoeste',
#                'SQS - Superquadra Sul - Asa Sul', 'QRSW - Quadras Regionais Sudoeste ', 'Condomínio - Beira Lago', 'CLSW - Comércio Local Sudoeste = Sudoeste',
#            'SHS - Setor Hoteleiro Sul - Asa Sul', 'CLN - Comércio Local Norte - Asa Norte', 'SMAS - Setor de Múltiplas Atividades Sul - Park Sul', 'CA - Centro de Atividades - Lago Norte'
#            ,'SQSW - Superquadra Sudoeste - Sudoeste', 'SEPS - Setor de Edíficios Públicos Sul (700) - Asa Sul', 'SCES - Setor de Clubes Esportivos Sul - Asa Sul',
#                'SCRN - St. de Habitações Coletivas e Geminadas Norte (700) - Asa Norte', 'SGCV - Setor de Garagens e Concessionárias de Veículos - Park Sul',
#            'SHTN - Setor de Hotéis e Turismo Norte - Asa Norte', 'SCEN - Setor de Clubes Esportivos Norte - Asa Norte', 'CLNW - Comércio Local Noroeste - Noroeste', 'SHN - Setor Hoteleiro Norte - Asa Norte'
#            , 'SHIN - Setor de Habitações Individuais Nortes - Lago Norte', 'SGAN - Setor de Grandes Areas Norte (900)- Asa Norte', 'AOS - Area Octogonal Sul - Octogonal',
#                'CRS - Comércio Residencial Sul (500)', 'STN - Setor Terminal Norte - Asa Norte',
#            'QC - Quadra Condominial - Jardins Mangueiral', 'SCLRN - Setor Comercial Local Residencial Norte - Asa Norte',
#                'SHCGN -  Setor Habitacional de Casas Geminadas Norte (700)- Asa Norte', 'SGAS - Setor de Grandes Areas Sul (900)- Asa Sul',
#                'EQRSW - Entrequadra Regional Sudoeste - Sudoeste', 'SHIGS - Setor de Habitações Individuais Germinadas Sul (700) - Asa Sul', 'CRNW - Comércio Regional Noroeste - Noroeste'
#                , 'SMLN - Setor de Mansões do Lago Norte - Lago Norte',
#            'SEPN - Setor de Edíficios Públicos Sul (700) - Asa Norte', 'Vila Planalto', 'SCN - Setor Comercial Norte - Asa Norte', 'SMDB - Setor de Mansões Dom Bosco - Lago Sul', 'SIG - Setor de Indústria Gráfica - Sudoeste', 'EQSW - Entrquadra Sudoeste - Sudoeste', 'EQS - Entrequadra Sul - Asa Sul',
#            'SHIS - Setor de Habitações Individuais Sul - Lago Sul', 'SHDB']

 #   nomes_setores.sort()

    setor = st.selectbox("Setor: ",setores)

    predict = st.form_submit_button(label = 'Prever Valor do Aluguel + Condomínio')


if predict:
    predict_results(MODEL_URL,area,quartos,setor)

# print the selected hobby




#st.subheader("Recomendações de imóveis com base na sua escolha:")
#data = pd.read_excel('data/top10.xlsx', index_col=0)
#data.rename(columns = {'name':'Localização','link':'Link','valor_total':'Valor Total (R$)',
 #                                   'price':'Aluguel (R$)','Condomínio R$':'Condomínio (R$)', 'area':'Area (m²)',
 #                                   }, inplace = True)
#st.dataframe(data=data)
