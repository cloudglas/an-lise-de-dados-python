import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ========== CONFIGURAÇÃO DA PÁGINA ==========
st.set_page_config(
    page_title="NYPD Arrest Dashboard",
    page_icon="👮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== CSS PERSONALIZADO ==========
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem;
        border-radius: 10px;
        font-weight: bold;
    }
    .stSelectbox, .stMultiselect, .stSlider {
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ========== FUNÇÕES AUXILIARES ==========
@st.cache_data
def load_data(file_path, sample_size=50000):
    """Carrega os dados com cache para performance"""
    try:
        if file_path.endswith('nypd.csv'):
            # Para o arquivo grande, carrega amostra
            df = pd.read_csv(file_path, nrows=sample_size)
        else:
            df = pd.read_csv(file_path)
        
        # Converter datas
        if 'ARREST_DATE' in df.columns:
            df['ARREST_DATE'] = pd.to_datetime(df['ARREST_DATE'], errors='coerce')
        
        # Mapear bairros
        bairro_map = {
            'K': 'Brooklyn',
            'M': 'Manhattan', 
            'Q': 'Queens',
            'B': 'Bronx',
            'S': 'Staten Island'
        }
        
        if 'ARREST_BORO' in df.columns:
            df['BAIRRO_NOME'] = df['ARREST_BORO'].map(bairro_map)
        
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()

def create_metric_card(title, value, subtitle, icon="📊"):
    """Cria um card de métrica"""
    return f"""
    <div class="metric-card">
        <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
        <div style="font-size: 2.5rem; font-weight: bold;">{value}</div>
        <div style="font-size: 1rem; opacity: 0.9;">{title}</div>
        <div style="font-size: 0.9rem; margin-top: 0.5rem;">{subtitle}</div>
    </div>
    """

# ========== SIDEBAR ==========
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Seal_of_the_New_York_City_Police_Department.svg/200px-Seal_of_the_New_York_City_Police_Department.svg.png", 
             width=150)
    
    st.title("🔧 Configurações")
    
    # Selecionar arquivo
    arquivos_csv = [f for f in st.session_state.get('csv_files', []) if f.endswith('.csv')]
    if not arquivos_csv:
        import os
        arquivos_csv = [f for f in os.listdir('.') if f.endswith('.csv')]
        st.session_state.csv_files = arquivos_csv
    
    selected_file = st.selectbox(
        "📁 Selecionar Dataset",
        arquivos_csv,
        index=0 if arquivos_csv else None
    )
    
    # Tamanho da amostra
    sample_size = st.slider(
        "📊 Tamanho da Amostra",
        min_value=1000,
        max_value=100000,
        value=10000,
        step=1000
    )
    
    # Filtros
    st.subheader("🎯 Filtros")
    
    year_filter = st.slider(
        "Ano",
        min_value=2000,
        max_value=2024,
        value=(2020, 2024)
    )
    
    st.markdown("---")
    st.info("""
    **Sobre os dados:**
    - Dados oficiais da NYPD
    - Atualizados periodicamente
    - Fonte: data.cityofnewyork.us
    """)

# ========== CARREGAR DADOS ==========
if selected_file:
    with st.spinner(f"Carregando {selected_file}..."):
        df = load_data(selected_file, sample_size)
    
    if not df.empty:
        # ========== HEADER ==========
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown('<h1 class="main-header">👮 NYPD Arrest Dashboard</h1>', unsafe_allow_html=True)
            st.markdown('<p class="sub-header">Análise interativa dos dados de prisões de Nova York</p>', unsafe_allow_html=True)
        
        # ========== MÉTRICAS PRINCIPAIS ==========
        st.markdown("## 📈 Métricas Principais")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_arrests = len(df)
            st.markdown(create_metric_card(
                "Total de Prisões", 
                f"{total_arrests:,}", 
                "registros analisados",
                "👮"
            ), unsafe_allow_html=True)
        
        with col2:
            if 'BAIRRO_NOME' in df.columns:
                top_borough = df['BAIRRO_NOME'].value_counts().index[0]
                top_count = df['BAIRRO_NOME'].value_counts().iloc[0]
                st.markdown(create_metric_card(
                    "Bairro Mais Ativo", 
                    top_borough, 
                    f"{top_count:,} prisões",
                    "🏙️"
                ), unsafe_allow_html=True)
        
        with col3:
            if 'AGE_GROUP' in df.columns:
                top_age = df['AGE_GROUP'].value_counts().index[0]
                age_count = df['AGE_GROUP'].value_counts().iloc[0]
                st.markdown(create_metric_card(
                    "Faixa Etária Mais Frequente", 
                    top_age, 
                    f"{age_count:,} casos",
                    "👥"
                ), unsafe_allow_html=True)
        
        with col4:
            if 'ARREST_PRECINCT' in df.columns:
                top_precinct = df['ARREST_PRECINCT'].value_counts().index[0]
                precinct_count = df['ARREST_PRECINCT'].value_counts().iloc[0]
                st.markdown(create_metric_card(
                    "Distrito Mais Ativo", 
                    f"#{top_precinct}", 
                    f"{precinct_count:,} ocorrências",
                    "📍"
                ), unsafe_allow_html=True)
        
        # ========== ANÁLISE GEOGRÁFICA ==========
        st.markdown("---")
        st.markdown("## 🗺️ Análise Geográfica")
        
        tab1, tab2, tab3 = st.tabs(["🏙️ Por Bairro", "📍 Por Distrito", "🗺️ Mapa"])
        
        with tab1:
            col1, col2 = st.columns([2, 1])
            
            with col1:
                if 'BAIRRO_NOME' in df.columns:
                    # Gráfico de barras
                    borough_counts = df['BAIRRO_NOME'].value_counts()
                    
                    fig = px.bar(
                        borough_counts,
                        x=borough_counts.index,
                        y=borough_counts.values,
                        title="Prisões por Bairro",
                        labels={'x': 'Bairro', 'y': 'Número de Prisões'},
                        color=borough_counts.values,
                        color_continuous_scale='Viridis'
                    )
                    st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Tabela de dados
                if 'BAIRRO_NOME' in df.columns:
                    borough_stats = pd.DataFrame({
                        'Bairro': df['BAIRRO_NOME'].value_counts().index,
                        'Prisões': df['BAIRRO_NOME'].value_counts().values,
                        '%': (df['BAIRRO_NOME'].value_counts().values / len(df) * 100).round(1)
                    })
                    st.dataframe(borough_stats, use_container_width=True)
        
        with tab2:
            if 'ARREST_PRECINCT' in df.columns:
                precinct_counts = df['ARREST_PRECINCT'].value_counts().head(20)
                
                fig = px.bar(
                    precinct_counts,
                    x=precinct_counts.index,
                    y=precinct_counts.values,
                    title="Top 20 Distritos com Mais Prisões",
                    labels={'x': 'Distrito', 'y': 'Número de Prisões'},
                    color=precinct_counts.values,
                    color_continuous_scale='Plasma'
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            if all(col in df.columns for col in ['Latitude', 'Longitude']):
                # Mapa de calor
                fig = px.density_mapbox(
                    df.dropna(subset=['Latitude', 'Longitude']).head(1000),
                    lat='Latitude',
                    lon='Longitude',
                    radius=10,
                    center=dict(lat=40.7128, lon=-74.0060),
                    zoom=10,
                    mapbox_style="carto-positron",
                    title="Mapa de Densidade de Prisões"
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Coordenadas geográficas não disponíveis nesta amostra.")
        
        # ========== ANÁLISE DEMOGRÁFICA ==========
        st.markdown("---")
        st.markdown("## 👥 Análise Demográfica")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if 'AGE_GROUP' in df.columns:
                # Gráfico de pizza idade
                age_counts = df['AGE_GROUP'].value_counts()
                
                fig = px.pie(
                    values=age_counts.values,
                    names=age_counts.index,
                    title="Distribuição por Faixa Etária",
                    hole=0.3
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            if 'PERP_SEX' in df.columns:
                # Gráfico de barras sexo
                gender_counts = df['PERP_SEX'].value_counts()
                
                fig = px.bar(
                    gender_counts,
                    x=gender_counts.index,
                    y=gender_counts.values,
                    title="Distribuição por Sexo",
                    labels={'x': 'Sexo', 'y': 'Número de Prisões'},
                    color=gender_counts.values,
                    color_continuous_scale='Blues'
                )
                st.plotly_chart(fig, use_container_width=True)
        
        # Análise por raça
        if 'PERP_RACE' in df.columns:
            st.markdown("### 🌈 Distribuição por Raça/Etnia")
            
            race_counts = df['PERP_RACE'].value_counts().head(10)
            
            fig = px.bar(
                race_counts,
                x=race_counts.values,
                y=race_counts.index,
                orientation='h',
                title="Top 10 Raças/Etnias",
                labels={'x': 'Número de Prisões', 'y': 'Raça/Etnia'},
                color=race_counts.values,
                color_continuous_scale='Rainbow'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # ========== ANÁLISE TEMPORAL ==========
        st.markdown("---")
        st.markdown("## 📅 Análise Temporal")
        
        if 'ARREST_DATE' in df.columns:
            # Extrair componentes de data
            df['ANO'] = df['ARREST_DATE'].dt.year
            df['MES'] = df['ARREST_DATE'].dt.month
            df['DIA_SEMANA'] = df['ARREST_DATE'].dt.day_name()
            df['HORA'] = df['ARREST_DATE'].dt.hour
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Por ano
                yearly = df['ANO'].value_counts().sort_index()
                
                fig = px.line(
                    yearly,
                    x=yearly.index,
                    y=yearly.values,
                    title="Evolução Anual",
                    labels={'x': 'Ano', 'y': 'Prisões'},
                    markers=True
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Por dia da semana
                day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                day_counts = df['DIA_SEMANA'].value_counts()
                day_counts = day_counts.reindex(day_order)
                
                fig = px.bar(
                    day_counts,
                    x=day_counts.index,
                    y=day_counts.values,
                    title="Prisões por Dia da Semana",
                    labels={'x': 'Dia', 'y': 'Prisões'},
                    color=day_counts.values,
                    color_continuous_scale='Greens'
                )
                st.plotly_chart(fig, use_container_width=True)
            
            # Por hora do dia
            hourly = df['HORA'].value_counts().sort_index()
            
            fig = px.area(
                hourly,
                x=hourly.index,
                y=hourly.values,
                title="Distribuição por Hora do Dia",
                labels={'x': 'Hora', 'y': 'Prisões'}
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # ========== ANÁLISE DE CRIMES ==========
        if 'OFNS_DESC' in df.columns:
            st.markdown("---")
            st.markdown("## ⚖️ Análise por Tipo de Crime")
            
            crime_counts = df['OFNS_DESC'].value_counts().head(15)
            
            fig = px.bar(
                crime_counts,
                x=crime_counts.values,
                y=crime_counts.index,
                orientation='h',
                title="Top 15 Tipos de Crime",
                labels={'x': 'Número de Prisões', 'y': 'Tipo de Crime'},
                color=crime_counts.values,
                color_continuous_scale='Reds'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # ========== TABELA INTERATIVA ==========
        st.markdown("---")
        st.markdown("## 📋 Dados Detalhados")
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.subheader("🔍 Filtros Avançados")
            
            # Filtro por bairro
            if 'BAIRRO_NOME' in df.columns:
                bairros = st.multiselect(
                    "Bairros:",
                    options=df['BAIRRO_NOME'].unique(),
                    default=df['BAIRRO_NOME'].unique()[:3]
                )
            
            # Filtro por idade
            if 'AGE_GROUP' in df.columns:
                idades = st.multiselect(
                    "Faixas Etárias:",
                    options=df['AGE_GROUP'].unique(),
                    default=df['AGE_GROUP'].unique()
                )
        
        with col2:
            # Aplicar filtros
            df_filtered = df.copy()
            
            if 'bairros' in locals() and bairros:
                df_filtered = df_filtered[df_filtered['BAIRRO_NOME'].isin(bairros)]
            
            if 'idades' in locals() and idades:
                df_filtered = df_filtered[df_filtered['AGE_GROUP'].isin(idades)]
            
            # Mostrar tabela
            st.dataframe(
                df_filtered.head(100),
                use_container_width=True,
                height=400
            )
            
            # Botão de download
            csv = df_filtered.to_csv(index=False)
            st.download_button(
                label="📥 Baixar Dados Filtrados (CSV)",
                data=csv,
                file_name="nypd_filtrado.csv",
                mime="text/csv"
            )
        
        # ========== ESTATÍSTICAS ==========
        with st.expander("📊 Estatísticas Detalhadas"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Resumo Numérico")
                st.dataframe(df.describe(), use_container_width=True)
            
            with col2:
                st.subheader("Informações do Dataset")
                
                info_text = f"""
                ### 📁 Informações do Dataset
                
                **Arquivo:** {selected_file}
                **Registros:** {len(df):,}
                **Colunas:** {len(df.columns)}
                **Período:** {df['ARREST_DATE'].min().date() if 'ARREST_DATE' in df.columns else 'N/A'} a {df['ARREST_DATE'].max().date() if 'ARREST_DATE' in df.columns else 'N/A'}
                **Valores Nulos:** {df.isnull().sum().sum():,}
                
                ### 🎯 Principais Insights
                1. **Bairro predominante:** {df['BAIRRO_NOME'].value_counts().index[0] if 'BAIRRO_NOME' in df.columns else 'N/A'}
                2. **Faixa etária mais comum:** {df['AGE_GROUP'].value_counts().index[0] if 'AGE_GROUP' in df.columns else 'N/A'}
                3. **Distrito mais ativo:** {df['ARREST_PRECINCT'].value_counts().index[0] if 'ARREST_PRECINCT' in df.columns else 'N/A'}
                """
                st.markdown(info_text)
        
        # ========== RODAPÉ ==========
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 📈 Sobre")
            st.markdown("""
            Dashboard criado com:
            - Python
            - Streamlit
            - Pandas
            - Plotly
            """)
        
        with col2:
            st.markdown("### 🔗 Fontes")
            st.markdown("""
            - Dados: NYPD Open Data
            - GitHub: [link]
            - Documentação: [link]
            """)
        
        with col3:
            st.markdown("### 📅 Atualização")
            st.markdown(f"""
            **Última análise:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
            **Versão:** 1.0.0
            **Status:** ✅ Operacional
            """)
    
    else:
        st.error("Não foi possível carregar os dados. Verifique o arquivo CSV.")
else:
    st.warning("Selecione um arquivo CSV na sidebar para começar.")

# ========== SCRIPT DE INICIALIZAÇÃO ==========
if __name__ == "__main__":
    # Este código só roda quando executado diretamente
    pass
