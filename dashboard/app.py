
import streamlit as st
from vendas.FTC_vendas import vendasProdutos
from clientes.DIM_clientes import clientes
from data.bancoDeDados import getAllVendas, getAllClientes, somaVendas, qtdTransacoes, vendasValidas, qtdClientes, taxaSucesso, filtroDinamico


info4_logo = "https://www.info4.com.br/en-US/_site_imagens/info4-logo-pr-br.png"
info4 = "https://www.info4.com.br/en-US/_site_imagens/info4-logo-pr-br.png"
st.set_page_config(page_title='Dashboard Info4', page_icon=info4_logo, layout='wide')


pageVendas = "Insight vendas"
pageCliente = "Insight cliente"

def build_sidebar():
    st.sidebar.title('Dashboard Info4')
    try:
        st.sidebar.image(info4_logo, width=200)
    except Exception as e:
        st.error(f"Error loading image: {e}")
    page = st.sidebar.selectbox('### Selecione a página:', [pageVendas, pageCliente])
    return page

def build_main(page):
    filtro = filtroDinamico()
    print(filtro)
    if page == pageVendas:
        vendasProdutos();
    elif page == pageCliente:
        clientes();
    else:
        st.error('Page not found')
       
    
    # Calcula os KPIs
    total_vendas = somaVendas();
    total_transacoes = qtdTransacoes();
    total_vendas_validas = vendasValidas();
    total_clientes = qtdClientes();
    taxa_sucesso = taxaSucesso();

    # Configura o layout de colunas com estilo
    col1, col2, col3, col4, col5, col6 = st.columns(6);

    # Adiciona os KPIs às colunas com estilo
    with col1:
        st.subheader('Valor em vendas')
        st.metric(label="", value=f"R$ {total_vendas:,.2f}".replace('.', ',').replace(',', '.', 1).replace(',', '.', 1))
    with col2:
        st.subheader('Qtd de transações')
        st.metric(label="", value=f"{total_transacoes:,.0f}".replace('.', ',').replace(',', '.', 1))
    with col3:
        st.subheader('Vendas válidas')
        st.metric(label="", value=f"R$ {total_vendas_validas:,.2f}".replace('.', ',').replace(',', '.', 1).replace(',', '.', 1))
    with col4:
        st.subheader('Vendas Perdidas')
        st.metric(label="", value=f"R$ {(total_vendas - total_vendas_validas):,.2f}".replace('.', ',').replace(',', '.', 1))
    with col5:
        st.subheader('Qtd de clientes')
        st.metric(label="", value=f"{total_clientes:,.0f}".replace('.', ',').replace(',', '.', 1))
    with col6:
        st.subheader('Percentual de sucesso')
        st.metric(label="", value=f"{taxa_sucesso:,.2f}%".replace('.', ','))
        
st.markdown("""
        <style>
            .streamlit-expanderHeader {
                font-size: 18px !important;
                text-align: center;
            }
            
            .stMetric {
                background-color: #0f0f0f;  /* Cor de fundo */
                border-radius: 10px;         /* Bordas arredondadas */
                padding: 20px;               /* Espaçamento interno */
                box-shadow: 0 4px 8px rgba(0,0,0,0.4); /* Sombra */
                font-size: 20px;             /* Tamanho da fonte */
                font-weight: bold;           /* Peso da fonte */
        }

            .stMetric .stMetricValue {
                color: #79f2dc;  /* Cor do valor */
                font-size: 26px; /* Tamanho do valor */
        }

            .stMetric .stMetricLabel {
                color: #757575;  /* Cor do título */
        }
        </style>
    """, unsafe_allow_html=True)
    
page = build_sidebar()
build_main(page)
