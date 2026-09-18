
# =====================================================================
# APOSTILA EXECUTÁVEL STREAMLIT: O GUIA DEFINITIVO DO SENAI
# Rode este arquivo para ver todos os comandos funcionando na prática!
# =====================================================================

import streamlit as st
import pandas as pd
import time
import numpy as np

# =====================================================================
# 1. CONFIGURAÇÃO INICIAL (Sempre na linha 1)
# =====================================================================
st.set_page_config(page_title="Apostila Streamlit", page_icon="📘", layout="wide")

# O Menu Lateral (Sidebar)
st.sidebar.image("https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=500", caption="Apostila Interativa")
st.sidebar.title("Navegação Lateral")
st.sidebar.info("Tudo que usar 'st.sidebar' vem parar aqui neste menu escuro!")

# =====================================================================
# 2. TEXTOS E TIPOGRAFIA
# =====================================================================
# st.expander cria uma caixa que abre e fecha para organizar a tela
with st.expander("📝 1. TEXTOS E TIPOGRAFIA (Clique para abrir)", expanded=True):
    st.title("Isso é um st.title() - Título Gigante")
    st.header("Isso é um st.header() - Subtítulo Grande")
    st.subheader("Isso é um st.subheader() - Tópico")
    
    st.markdown("**Texto em Negrito** feito com st.markdown()")
    st.markdown("*Texto em Itálico* feito com st.markdown()")
    
    st.write("O st.write() é o coringa! Ele escreve textos normais e substitui o antigo print().")

    # =====================================================================
# 3. ENTRADA DE DADOS (WIDGETS)
# =====================================================================
with st.expander("🎛️ 2. ENTRADA DE DADOS (Widgets do Operador)"):
    st.write("Comandos para o usuário interagir com o sistema:")
    
    texto = st.text_input("st.text_input() -> Nome do Operador:")

    senha = st.text_input("st.text_input(type='password') -> Digite uma senha:", type="password")
    
    numero = st.number_input("st.number_input() -> Quantidade de Peças:", min_value=10, step=10)
    
    selecao = st.selectbox("st.selectbox() -> Escolha a Máquina:", ["Torno CNC", "Fresa", "Prensa"])
    
    radio = st.radio("st.radio() -> Status da Máquina:", ["Operante", "Em Manutenção"])
    
    arquivo = st.file_uploader("st.file_uploader() -> Suba o manual em PDF:")
    
    st.button("st.button() -> Botão de Ação Solto")

# =====================================================================
# 4. EXIBIÇÃO DE DADOS E MÉTRICAS
# =====================================================================
with st.expander("📊 3. EXIBIÇÃO DE DADOS E MÉTRICAS"):
    st.write("Criando visual de Dashboard Corporativo:")
    
    # st.columns divide a tela
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("st.metric()", "98%", delta="2% de aumento")
    with col2:
        st.metric("st.metric() (Queda)", "15 Refugos", delta="-3 refugos")
    
    st.write("---") # Linha de separação
    
    # Tabela Falsa para demonstração
    dados = pd.DataFrame({"Máquina": ["Torno", "Fresa", "Laser"], "Status": ["OK", "Falha", "OK"], "Temp": [45, 80, 30]})
    
    st.write("**st.dataframe()** -> Tabela Interativa (Clique nas colunas para ordenar):")
    st.dataframe(dados, use_container_width=True)
    
    st.write("**st.table()** -> Tabela Estática (Não dá para clicar):")
    st.table(dados)


# =====================================================================
# 5. MÍDIAS
# =====================================================================
with st.expander("🖼️ 4. MÍDIAS (Imagens, Vídeos e Áudio)"):
    st.write("**st.image()** -> Exibindo imagem da internet:")
    st.image("https://www.usinainfo.com.br/1018613-thickbox_default/braco-robotico-completo-para-arduino-manual-de-montagem.jpg", caption="Braço Robótico")
    
    st.write("**st.video()** -> Rodando vídeo do YouTube:")
    st.video("https://www.youtube.com/watch?v=J--7IsdWSwY")

# =====================================================================
# 6. EFEITOS ESPECIAIS E AVISOS
# =====================================================================
with st.expander("🚨 5. FEEDBACK E EFEITOS ESPECIAIS"):
    st.write("Caixas de Aviso Coloridas:")
    st.success("st.success() -> Operação concluída com sucesso!")
    st.error("st.error() -> Falha crítica no motor!")
    st.warning("st.warning() -> Atenção, nível de óleo baixo.")
    st.info("st.info() -> O turno acaba às 18h.")
    
    st.write("Botões de Efeitos Visuais:")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Disparar st.balloons()"):
            st.balloons()
    with c2:
        if st.button("Disparar st.snow()"):
            st.snow()
    with c3:
        if st.button("Disparar st.toast()"):
            st.toast("Notificação flutuante ativada!", icon="🔔")
            
    if st.button("Testar st.spinner()"):
        with st.spinner("Simulando processamento da IA... Aguarde 2 segundos"):
            time.sleep(2) # Pausa o código por 2 segundos
        st.success("Processamento finalizado!")

# =====================================================================
# 7. CHAT E IA VISUAL
# =====================================================================
with st.expander("💬 6. ELEMENTOS DE CHAT (Visual do ChatGPT)"):
    st.write("Como desenhar os balões de conversa:")
    
    # st.chat_message desenha o balão
    with st.chat_message("user"):
        st.write("st.chat_message('user') -> O Torno CNC parou com erro 404. O que eu faço?")
        
    with st.chat_message("assistant"):
        st.write("st.chat_message('assistant') -> Olá! Verifique o nível de óleo refrigerante imediatamente.")
        
    st.info("Obs: O comando 'st.chat_input()' cria a barra de digitação, mas ela sempre fica grudada no fundo da tela da página principal!")

# =====================================================================
# 8. ENTRADAS AVANÇADAS (SENSORES)
# =====================================================================
with st.expander("📸 7. ENTRADAS AVANÇADAS (Sensores)"):
    st.write("**st.camera_input()** -> Tira foto usando a Webcam (Ótimo para inspeção):")
    foto = st.camera_input("Tire uma foto do defeito da peça")
    if foto:
        st.success("Foto capturada com sucesso!")
        
    c1, c2, c3 = st.columns(3)
    with c1:
        st.color_picker("st.color_picker() -> Cor:")
    with c2:
        st.date_input("st.date_input() -> Data:")
    with c3:
        st.time_input("st.time_input() -> Hora:")

# =====================================================================
# 9. FORMULÁRIOS E DOWNLOADS
# =====================================================================
with st.expander("📥 8. FORMULÁRIOS E DOWNLOADS"):
    st.write("**st.form()** -> Agrupa vários campos e só processa quando clica em Enviar:")
    
    # Abrindo um formulário
    with st.form("form_os"):
        st.write("Formulário de Ordem de Serviço")
        operador_form = st.text_input("Operador:")
        equipamento_form = st.selectbox("Equipamento:", ["Motor", "Bomba", "Esteira"])
        
        # Todo form OBRIGATORIAMENTE precisa de um submit_button
        enviou = st.form_submit_button("Gerar O.S.")
        
        if enviou:
            st.success(f"O.S. do {equipamento_form} gerada pelo operador {operador_form}!")

    st.write("---")
    st.write("**st.download_button()** -> Baixar arquivos para o PC:")
    
    # Criando um texto fictício para baixar
    texto_relatorio = "Relatório de Parada de Máquina\nData: Hoje\nStatus: Resolvido"
    st.download_button(
        label="Baixar Relatório .TXT",
        data=texto_relatorio,
        file_name="relatorio_manutencao.txt"
    )

import streamlit as st
import pandas as pd
import numpy as np

# =====================================================================
# 10. GRÁFICOS E VISUALIZAÇÕES (Painel Gerencial)
# =====================================================================
with st.expander("📈 10. GRÁFICOS E MAPAS (Visualização de Dados)", expanded=True):
    st.write("Abaixo vemos como transformar tabelas com dados fixos em gráficos interativos:")
    # 1. DADOS DA FÁBRICA (Produção semanal)
    dados_semana = {
        'Produção':   [100, 120, 115, 130, 125, 90, 45],
        'Refugo':     [  5,   8,   4,  10,   6,  3,  1],
        'Retrabalho': [ 12,  15,  10,  18,  14,  7,  2]
    }
    dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
    
    # Criamos a tabela com os dias como linha (índice)
    tabela_fabrica = pd.DataFrame(dados_semana, index=dias)
    # -------------------------------------------------------------
    # ORGANIZAÇÃO EM ABAS PARA EXPLICAR PASSO A PASSO
    # -------------------------------------------------------------
    aba_dados, aba_linhas, aba_barras, aba_area, aba_dispersao, aba_mapa = st.tabs([
        "📋 Tabela Base",
        "📈 Linhas",
        "📊 Barras",
        "📉 Área",
        "🔵 Dispersão",
        "🌍 Mapa"
    ])
    with aba_dados:
        st.subheader("1. A Planilha de Origem")
        st.write("Observe como cada chave do dicionário virou uma coluna da tabela:")
        st.dataframe(tabela_fabrica)
    with aba_linhas:
        st.subheader("2. Gráfico de Linhas")
        st.write("Mostra a evolução da semana (queda natural no fim de semana):")
        st.line_chart(tabela_fabrica)
    with aba_barras:
        st.subheader("3. Gráfico de Barras")
        st.write("Permite comparar o volume de peças lado a lado por dia:")
        st.bar_chart(tabela_fabrica)
    with aba_area:
        st.subheader("4. Gráfico de Área")
        st.write("Similar ao de linhas, preenchendo a área inferior:")
        st.area_chart(tabela_fabrica)
    with aba_dispersao:
        st.subheader("5. Gráfico de Dispersão (Temperatura vs Vibração)")
        st.write("Mostra a relação direta: quanto mais quente a máquina, mais ela vibra!")
        
        # Dados fixos com lógica real de causa e efeito (sem números aleatórios)
        dados_maquina = pd.DataFrame({
            'Temperatura': [50, 55, 60, 68, 75, 82, 90, 98],
            'Vibração':    [ 8, 10, 11, 15, 19, 25, 33, 45]
        })
        st.scatter_chart(dados_maquina, x='Temperatura', y='Vibração')
    with aba_mapa:
        st.subheader("6. Mapa com Pontos Fixos (Caminhões em SP)")
        st.write("Basta uma tabela simples com coordenadas de latitude e longitude:")
        
        # Coordenadas reais de 4 pontos conhecidos de São Paulo (Av. Paulista, Centro, etc.)
        dados_mapa = pd.DataFrame({
            'lat': [-23.5505, -23.5615, -23.5489, -23.5874],
            'lon': [-46.6333, -46.6560, -46.6388, -46.6576]
        })
        st.map(dados_mapa)

st.write("Fim da Apostila Interativa")
#Fim da Apostila