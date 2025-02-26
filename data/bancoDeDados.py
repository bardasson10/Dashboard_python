import pandas as pd
import streamlit as st

dadosVendas = pd.read_excel('data/FCT_Compras.xlsx')
dadosClientes = pd.read_excel('data/DIM_Clientes.xlsx')

dadosFiltrados = pd.DataFrame()

def filtroDinamico():
    global dadosFiltrados
    required_columns_vendas = ['Codigo_Compra', 'Id_Cliente', 'Produto', 'Quantidade', 'Valor Unitário', 'Forma_de_Pagamento', 'Data', 'Parcelamento', 'Transportadora', 'Status', 'Dispositivo', 'Problema', 'Tipo de Problema']
    required_columns_clientes = ['ID_Cliente','Idade', 'UF', 'Estado']
    
    if not all(col in dadosVendas.columns for col in required_columns_vendas):
        st.error(f"Erro: Algumas colunas estão faltando no dataframe de Vendas! Colunas esperadas: {required_columns_vendas}, Colunas encontradas: {dadosVendas.columns.tolist()}")
        dadosFiltrados = pd.DataFrame()
        return
    
    if not all(col in dadosClientes.columns for col in required_columns_clientes):
        st.error("Erro: Algumas colunas estão faltando no dataframe de Clientes!")
        dadosFiltrados = pd.DataFrame()
        return

    dadosVendas['Data'] = pd.to_datetime(dadosVendas['Data'], errors='coerce')
    dadosVendas['Ano'] = dadosVendas['Data'].dt.year

    colu1, colu2, colu3, colu4, colu5, colu6, colu7, colu8 = st.columns(8)
    with colu1:
        dispositivo = st.multiselect('Dispositivo', dadosVendas['Dispositivo'].unique(), key='1')
    with colu2:
        produto = st.multiselect('Produto', dadosVendas['Produto'].unique(), key='2')
    with colu3:
        transportadora = st.multiselect('Transportadora', dadosVendas['Transportadora'].unique(), key='3')
    with colu4:
        status = st.multiselect('Status', dadosVendas['Status'].unique(), key='4')
    with colu5:
        estado = st.multiselect('Estado', dadosClientes['Estado'].unique(), key='5')
    with colu6:
        problema = st.multiselect('Problema', dadosVendas['Problema'].unique(), key='6')
    with colu7:
        forma_pagamento = st.multiselect('Forma de Pagamento', dadosVendas['Forma_de_Pagamento'].unique(), key='7')
    with colu8:
        ano = st.multiselect('Ano', dadosVendas['Ano'].unique(), key='8')

    dadosFiltrados = dadosVendas.copy()

    filtros = {
        'Dispositivo': dispositivo,
        'Produto': produto,
        'Transportadora': transportadora,
        'Status': status,
        'Problema': problema,
        'Forma_de_Pagamento': forma_pagamento,
        'Ano': ano
    }
    
    if estado:
        dadosFiltrados = dadosFiltrados[dadosFiltrados['Id_Cliente'].isin(dadosClientes[dadosClientes['Estado'].isin(estado)]['ID_Cliente'])]

    dadosFiltrados = pd.merge(dadosFiltrados, dadosClientes[['ID_Cliente', 'Estado']], left_on='Id_Cliente', right_on='ID_Cliente', how='left')

    for coluna, filtro in filtros.items():
        if filtro:
            dadosFiltrados = dadosFiltrados[dadosFiltrados[coluna].isin(filtro)]

def getAllVendas():
    st.write(dadosFiltrados.head())
    return dadosFiltrados

def getAllClientes():
    st.write(dadosClientes)
    return dadosClientes

def somaVendas():
    valorEmVendas = (dadosFiltrados['Valor Unitário'] * dadosFiltrados['Quantidade']).sum()
    return valorEmVendas

def qtdTransacoes():
    qtdTransacoes = dadosFiltrados['Codigo_Compra'].count()
    return qtdTransacoes

def vendasValidas():
    vendasValidas = (dadosFiltrados['Valor Unitário'] * dadosFiltrados['Quantidade'])[dadosFiltrados['Problema'] != 'Perda'].sum()
    return vendasValidas

def qtdClientes():
    qtdClientes = dadosClientes['ID_Cliente'].count()
    return qtdClientes

def taxaSucesso():
    transacoesPerdidas = dadosFiltrados[dadosFiltrados['Problema'] == 'Perda'].shape[0]
    taxaSucesso = ((qtdTransacoes() - transacoesPerdidas) / qtdTransacoes()) * 100
    return taxaSucesso

def formaPagamentoAoLongoTempo():
    dadosFiltrados['Data'] = pd.to_datetime(dadosFiltrados['Data'], errors='coerce')
    dadosFiltrados['Ano'] = dadosFiltrados['Data'].dt.year
    formas_pagamento = dadosFiltrados.groupby(['Ano', 'Forma_de_Pagamento']).size().unstack().fillna(0)
    return formas_pagamento

def statusTransacoes():
    dadosFiltrados['Data'] = pd.to_datetime(dadosFiltrados['Data'], errors='coerce')
    dadosFiltrados['Ano'] = dadosFiltrados['Data'].dt.year
    status_transacoes = (dadosFiltrados.groupby(['Status', 'Forma_de_Pagamento']).size().unstack().fillna(0))
    return status_transacoes

def visaoGeograficaValorTotalComprado():
    coordenadas_fixas = {
        "Acre": (-9.97399, -67.80757),
        "Alagoas": (-9.57131, -36.78200),
        "Amapá": (1.41537, -51.33149),
        "Amazonas": (-3.41684, -65.85606),
        "Bahia": (-12.9714, -38.5014),
        "Ceará": (-3.71722, -38.54339),
        "Distrito Federal": (-15.7934, -47.8826),
        "Espírito Santo": (-20.3155, -40.3128),
        "Goiás": (-16.6869, -49.2648),
        "Maranhão": (-2.53874, -44.28290),
        "Mato Grosso": (-12.6469, -55.4246),
        "Mato Grosso do Sul": (-20.4697, -54.6201),
        "Minas Gerais": (-18.5122, -44.5550),
        "Pará": (-1.45502, -48.50237),
        "Paraíba": (-7.11509, -34.86430),
        "Paraná": (-25.4284, -49.2733),
        "Pernambuco": (-8.04756, -34.87700),
        "Piauí": (-5.08921, -42.80160),
        "Rio de Janeiro": (-22.9068, -43.1729),
        "Rio Grande do Norte": (-5.79448, -35.21100),
        "Rio Grande do Sul": (-30.0346, -51.2177),
        "Rondônia": (-11.40987, -63.44254),
        "Roraima": (2.82350, -60.67583),
        "Santa Catarina": (-27.5954, -48.5480),
        "São Paulo": (-23.5505, -46.6333),
        "Sergipe": (-10.9472, -37.0731),
        "Tocantins": (-10.2551, -48.3243),
    }

    dadosFiltrados["Valor Total"] = dadosFiltrados["Valor Unitário"] * dadosFiltrados["Quantidade"]

    valor_total_comprado = dadosFiltrados.groupby('Estado')['Valor Total'].sum().reset_index()

    valor_total_comprado['lat'] = valor_total_comprado['Estado'].map(lambda x: coordenadas_fixas.get(x, (None, None))[0])
    valor_total_comprado['lon'] = valor_total_comprado['Estado'].map(lambda x: coordenadas_fixas.get(x, (None, None))[1])

    return valor_total_comprado

def visaoGeograficaValorTotalComprado2():
    coordenadas_fixas = {
        "Acre": (-9.97399, -67.80757),
        "Alagoas": (-9.57131, -36.78200),
        "Amapá": (1.41537, -51.33149),
        "Amazonas": (-3.41684, -65.85606),
        "Bahia": (-12.9714, -38.5014),
        "Ceará": (-3.71722, -38.54339),
        "Distrito Federal": (-15.7934, -47.8826),
        "Espírito Santo": (-20.3155, -40.3128),
        "Goiás": (-16.6869, -49.2648),
        "Maranhão": (-2.53874, -44.28290),
        "Mato Grosso": (-12.6469, -55.4246),
        "Mato Grosso do Sul": (-20.4697, -54.6201),
        "Minas Gerais": (-18.5122, -44.5550),
        "Pará": (-1.45502, -48.50237),
        "Paraíba": (-7.11509, -34.86430),
        "Paraná": (-25.4284, -49.2733),
        "Pernambuco": (-8.04756, -34.87700),
        "Piauí": (-5.08921, -42.80160),
        "Rio de Janeiro": (-22.9068, -43.1729),
        "Rio Grande do Norte": (-5.79448, -35.21100),
        "Rio Grande do Sul": (-30.0346, -51.2177),
        "Rondônia": (-11.40987, -63.44254),
        "Roraima": (2.82350, -60.67583),
        "Santa Catarina": (-27.5954, -48.5480),
        "São Paulo": (-23.5505, -46.6333),
        "Sergipe": (-10.9472, -37.0731),
        "Tocantins": (-10.2551, -48.3243),
    }

    dadosFiltrados["Valor Total"] = dadosFiltrados["Valor Unitário"] * dadosFiltrados["Quantidade"]

    valor_total_comprado = dadosFiltrados.groupby('Estado').agg(
        Valor_Total=('Valor Total', 'sum'),
        Transacoes=('Valor Total', 'size')
    ).reset_index()

    valor_total_comprado['lat'] = valor_total_comprado['Estado'].map(lambda x: coordenadas_fixas.get(x, (None, None))[0])
    valor_total_comprado['lon'] = valor_total_comprado['Estado'].map(lambda x: coordenadas_fixas.get(x, (None, None))[1])

    return valor_total_comprado

def shareValorProduto():
    dadosFiltrados['Valor Total'] = dadosFiltrados['Valor Unitário'] * dadosFiltrados['Quantidade']

    valor_total_total = dadosFiltrados['Valor Total'].sum()

    dadosFiltrados['Porcentagem'] = (dadosFiltrados['Valor Total'] / valor_total_total) * 100

    valor_total = dadosFiltrados.groupby('Produto').agg({'Valor Total': 'sum', 'Porcentagem': 'max'}).reset_index()

    return valor_total

def faixaEtariaAnalise():
    dadosFiltrados["Valor Total"] = dadosFiltrados["Valor Unitário"] * dadosFiltrados["Quantidade"]
    
    if 'Idade' not in dadosClientes.columns:
        st.error("Erro: A coluna 'Idade' está faltando no dataframe de Clientes!")
        return pd.DataFrame()

    dadosCompletos = pd.merge(dadosFiltrados, dadosClientes, left_on='Id_Cliente', right_on='ID_Cliente', how='inner')

    dadosCompletos['Faixa Etária'] = pd.cut(
        dadosCompletos['Idade'],
        bins=[0, 18, 28, 38, 48, 58, 68, 78, float('inf')],
        labels=['0-17', '18-27', '28-37', '38-47', '48-57', '58-67', '68-77', '78+'],
        right=False
    )
    dadosCompletos['Faixa Etária'] = dadosCompletos['Faixa Etária'].cat.add_categories('.').fillna('.')
    dadosClientes['Faixa Etária'] = pd.cut(
        dadosClientes['Idade'],
        bins=[18, 28, 38, 48, 58, 68, 78, float('inf')],
        labels=['18-27', '28-37', '38-47', '48-57', '58-67', '68-77', '78+'],
        right=False
    )
    dadosClientes['Faixa Etária'] = dadosClientes['Faixa Etária'].cat.add_categories('.').fillna('.')

    faixa_etaria_analise = dadosCompletos.groupby('Faixa Etária').agg(
        Valor_Total_Compra=('Valor Total', 'sum'),
        Contagem_Compras=('Valor Total', 'count')
    ).reset_index()

    contagem_clientes = dadosClientes['Faixa Etária'].value_counts().reset_index()
    contagem_clientes.columns = ['Faixa Etária', 'Contagem_Clientes']

    faixa_etaria_analise = pd.merge(faixa_etaria_analise, contagem_clientes, on='Faixa Etária', how='outer').fillna(0)

    faixa_etaria_analise['Valor_Medio_Compra'] = faixa_etaria_analise['Valor_Total_Compra'] / faixa_etaria_analise['Contagem_Compras']

    return faixa_etaria_analise

def taxaPerdaTransportadora():
    transacoesPerdidas = dadosFiltrados[dadosFiltrados['Problema'] == 'Perda']
    
    transacoesPerdidasPorTransportadora = transacoesPerdidas.groupby('Transportadora').size()
    
    transacoesPorTransportadora = dadosFiltrados.groupby('Transportadora').size()
    
    taxaPerdaTransportadora = (transacoesPerdidasPorTransportadora / transacoesPorTransportadora) * 100
    
    taxaPerdaTransportadora = taxaPerdaTransportadora.reset_index()
    taxaPerdaTransportadora.columns = ['Transportadora', 'Taxa de Perda']
    
    return taxaPerdaTransportadora

def perdaPorTransportadoraFaixaEtaria():
    transacoesPerdidas = dadosFiltrados[dadosFiltrados['Problema'] == 'Perda']
    dadosCompletos = pd.merge(transacoesPerdidas, dadosClientes, left_on='Id_Cliente', right_on='ID_Cliente', how='inner')
    dadosCompletos['Faixa Etária'] = pd.cut(
        dadosCompletos['Idade'],
        bins=[0, 18, 28, 38, 48, 58, 68, 78, float('inf')],
        labels=['0-17', '18-27', '28-37', '38-47', '48-57', '58-67', '68-77', '78+'],
        right=False
    )
    perdaPorTransportadoraFaixaEtaria = dadosCompletos.groupby(['Transportadora', 'Faixa Etária']).size().unstack().fillna(0)

    return perdaPorTransportadoraFaixaEtaria
