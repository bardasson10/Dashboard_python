import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px
from datetime import datetime
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.grid import grid

from data.bancoDeDados import faixaEtariaAnalise, taxaPerdaTransportadora, perdaPorTransportadoraFaixaEtaria

def clientes():
    faixaEtaria = faixaEtariaAnalise();
    taxa_transportadora_perda = taxaPerdaTransportadora();
    perda_por_transportadora_faixa_etaria = perdaPorTransportadoraFaixaEtaria();
    col1, col2, col3 = st.columns(3);
    with col1:
        st.title('Dados de compra por faixa etária');
        st.write('Informações sobre o valor médio de compra por faixa etária.');
        st.write(faixaEtaria);
    with col2:
        st.title('Perda por Transportadora');
        st.write('Informações sobre a taxa de perda por transportadora.');
        if 'Taxa de Perda' in taxa_transportadora_perda.columns and 'Transportadora' in taxa_transportadora_perda.columns:
            taxa_perda = px.pie(taxa_transportadora_perda, values='Taxa de Perda', names='Transportadora', title='')
            st.plotly_chart(taxa_perda)
        else:
            st.error("DataFrame does not have the required columns.")
    with col3:
        st.title('Perda por Transportadora por Faixa Etária');
        st.write('Informações sobre a perda por transportadora por faixa etária.');
        st.bar_chart(perda_por_transportadora_faixa_etaria, horizontal=False);
    return;