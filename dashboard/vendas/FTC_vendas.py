import streamlit as st
import plotly.express as px
import pydeck as pdk



from data.bancoDeDados import  formaPagamentoAoLongoTempo, statusTransacoes, visaoGeograficaValorTotalComprado, visaoGeograficaValorTotalComprado2, shareValorProduto

def vendasProdutos():

    vendas_geo_total = visaoGeograficaValorTotalComprado();
    vendas_geo_total2 = visaoGeograficaValorTotalComprado2();
    share_produto = shareValorProduto();
    cl1, cl2 = st.columns(2)

    with cl1:
        st.title("Vendas por Estado")
        st.write("Informações sobre as vendas por estado.")
        fig_bar = px.bar(vendas_geo_total, x="Estado", y="Valor Total", title="Vendas por Estado")
        st.plotly_chart(fig_bar)

    with cl2:
        point_layer = pdk.Layer(
            "ScatterplotLayer",
            data=vendas_geo_total2,
            id="vendas",
            get_position=["lon", "lat"],
            get_color="[255, 0, 0, 200]",
            pickable=True,
            auto_highlight=True,
            get_radius=50000,
            stroked=True,
            filled=True,
            line_width_min_pixels=1,
        )
        view_state = pdk.ViewState(
            latitude=-23.5505,
            longitude=-46.6333,
            controller=True,
            zoom=4,
            pitch=30,
        )
        # Criando o mapa com a camada e as configurações
        chart = pdk.Deck(
            layers=[point_layer],
            initial_view_state=view_state,
            tooltip={"text": "{Estado}\nValor Total: {Valor_Total}\nTransações: {Transacoes}"},
        )
        
        st.title("Mapa de trasanções")
        st.write("Mapa com as transações por cada estado.")
        st.pydeck_chart(chart)


    # Formas de pagamento ao longo do tempo
    pagamentos = formaPagamentoAoLongoTempo();
    status_transacoes = statusTransacoes();

    colu1, colu2, colu3 = st.columns(3);

    with colu1:
        st.title('Forma de pagamento ao longo do tempo')
        st.write('Aqui você encontra informações sobre a forma de pagamento ao longo do tempo')
        st.line_chart(pagamentos);
    with colu2:
        st.title('Share do produto nas vendas')
        st.write('Aqui você encontra informações sobre a participação de cada produto nas vendas')
        share = px.pie(share_produto, values='Valor Total', names='Produto', title='')
        st.plotly_chart(share)

    with colu3:
        st.title('Status das Transações')
        st.write('Aqui você encontra informações sobre o status das transações.')
        # Gráfico ajustado
        try:
            st.bar_chart(status_transacoes)
        except Exception as e:
            st.error(f"Erro ao gerar o gráfico: {e}")

    return;
