import streamlit as st

st.title ('Simulador do custo de moradia com aluguel - Brasília/DF')
st.subheader("Preencha os dados com a simulação desejada e o modelo dirá um valor para os custos mensais de moradia (Aluguel + Condomínio + IPTU (diluído mensalmente)")
quartos = st.selectbox("Quartos: ",
                     [1, 2, 3, 4])
area = st.slider("Area (m²)", 20, 250)


setores = ['SQNW', 'SQN', 'QMSW', 'CCSW', 'SQS', 'QRSW', 'Condomínio', 'CLSW',
       'SHS', 'CLN', 'SMAS', 'CA', 'SQSW', 'SEPS', 'SCES', 'SCRN', 'SGCV',
       'SHTN', 'SCEN', 'CLNW', 'SHN', 'SHIN', 'SGAN', 'AOS', 'CRS', 'STN',
       'QC', 'SCLRN', 'SHCGN', 'SGAS', 'EQRSW', 'SHIGS', 'CRNW', 'SMLN',
       'SEPN', 'Vila Planalto', 'SCN', 'SMDB', 'SIG', 'EQSW', 'EQS',
       'SHIS', 'SHDB']
setores.sort()

nomes_setores = ['SQNW - Superquadra Noroeste - Noroeste', 'SQN - Superquadra Norte - Asa Norte', 'QMSW - Quadras Mistas Sudoeste - Octogonal', 'CCSW - Centro Comercial Sudoeste - Sudoeste',
         'SQS - Superquadra Sul - Asa Sul', 'QRSW - Quadras Regionais Sudoeste ', 'Condomínio - Beira Lago', 'CLSW - Comércio Local Sudoeste = Sudoeste',
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
       'SHIS - Setor de Habitações Individuais Sul - Lago Sul', 'SHDB']

nomes_setores.sort()


setor = st.selectbox("Setor: ",nomes_setores)


# print the selected hobby
st.write("Quartos: ", quartos)
st.write("Area: ", area, "m²")
st.write("Setor: ", setor)