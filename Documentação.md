
📚 Documentação Técnica - Comandos dos Scripts Python
Aqui está uma lista completa de comandos para todos os seus arquivos Python, perfeita para documentação técnica:

📋 ÍNDICE DE COMANDOS
1. 🎯 DASHBOARD PRINCIPAL
2. 📊 ANÁLISE DE DADOS NYPD
3. 🔧 SCRIPTS DE PROCESSAMENTO
4. 📈 ANÁLISES ESPECÍFICAS
5. 🛠️ UTILITÁRIOS
1. 🎯 DASHBOARD PRINCIPAL
app.py - Dashboard Interativo Streamlit
bash
# Iniciar o dashboard web (interface gráfica)
streamlit run app.py

# Executar com porta específica
streamlit run app.py --server.port 8501

# Executar em modo headless (sem navegador)
streamlit run app.py --server.headless true

# Executar com tema escuro
streamlit run app.py --theme.base dark
nypd_dashboard.py - Visualizações Avançadas
bash
# Executar visualizações específicas
python nypd_dashboard.py --tipo grafico --dataset nypd.csv

# Gerar relatório completo
python nypd_dashboard.py --relatorio completo --output relatorio.pdf

# Visualizar apenas uma análise
python nypd_dashboard.py --analise crimes_por_distrito
2. 📊 ANÁLISE DE DADOS NYPD
analise_completa.py - Análise Completa
bash
# Análise completa do dataset
python analise_completa.py --input nypd.csv --output analise_completa.md

# Análise com filtros específicos
python analise_completa.py --filtro-ano 2023 --filtro-distrito "MANHATTAN"

# Gerar múltiplos formatos
python analise_completa.py --formatos csv json html --verbose
analise_crimes.py - Análise Criminal
bash
# Top 10 crimes mais comuns
python analise_crimes.py --top 10 --dataset nypd.csv

# Análise por período
python analise_crimes.py --periodo mensal --ano 2023

# Exportar resultados
python analise_crimes.py --export top_crimes.csv --format csv
analise_demografica.py - Análise Demográfica
bash
# Distribuição por raça/etnia
python analise_demografica.py --variavel RACE --dataset nypd.csv

# Análise por gênero e idade
python analise_demografica.py --variaveis GENDER AGE_GROUP

# Gerar gráficos demográficos
python analise_demografica.py --graficos histograma pizza --output demografia/
analise_temporal.py - Análise Temporal
bash
# Tendências ao longo do tempo
python analise_temporal.py --periodo diario --meses 12

# Sazonalidade (padrões semanais/mensais)
python analise_temporal.py --sazonalidade semanal --dataset nypd.csv

# Previsão de tendências
python analise_temporal.py --previsao 30 --modelo arima
analise_rapida.py - Análise Rápida
bash
# Quick analysis (estatísticas básicas)
python analise_rapida.py --quick --dataset nypd.csv

# Resumo estatístico
python analise_rapida.py --resumo --colunas todas

# Detecção de outliers
python analise_rapida.py --outliers --metodo iqr
analise_simples.py - Análise Simples
bash
# Estatísticas descritivas básicas
python analise_simples.py --describe --dataset nypd.csv

# Contagem de valores únicos
python analise_simples.py --unique --coluna BOROUGH

# Verificar dados faltantes
python analise_simples.py --missing --output missing_report.txt
3. 🔧 SCRIPTS DE PROCESSAMENTO
analisar_nypd.py - Processamento Principal
bash
# Processar dataset completo
python analisar_nypd.py --processar --input NYPD_Arrests_Data__Historic_.csv

# Limpar e transformar dados
python analisar_nypd.py --limpar --remover-duplicados --preencher-nulos

# Dividir dataset por ano
python analisar_nypd.py --dividir-por ano --output-pasta datasets_por_ano/
analisar_grande.py - Processamento de Grandes Volumes
bash
# Processar em chunks (para datasets grandes)
python analisar_grande.py --chunk-size 10000 --dataset grande.csv

# Processamento paralelo
python analisar_grande.py --threads 4 --memoria 8GB

# Otimização de performance
python analisar_grande.py --otimizar --dtypes-auto
estrutura.py - Estrutura de Dados
bash
# Analisar estrutura do dataset
python estrutura.py --info --dataset nypd.csv

# Tipos de dados de cada coluna
python estrutura.py --dtypes --output tipos_dados.json

# Schema do dataset
python estrutura.py --schema --format markdown
inspecionar.py - Inspeção de Dados
bash
# Inspecionar primeiras linhas
python inspecionar.py --head 20 --dataset nypd.csv

# Amostra aleatória
python inspecionar.py --sample 100 --random

# Estatísticas por coluna
python inspecionar.py --stats --coluna AGE_GROUP
4. 📈 ANÁLISES ESPECÍFICAS
ver_dados.py - Visualização de Dados
bash
# Visualizar dados em tabela
python ver_dados.py --view table --limit 50

# Exportar para visualização
python ver_dados.py --export html --output visualizacao.html

# Filtrar durante visualização
python ver_dados.py --filter "AGE > 30" --colunas "ARREST_DATE,OFFENSE"
relatorio_final.py - Geração de Relatórios
bash
# Gerar relatório completo
python relatorio_final.py --completo --output relatorio_final.pdf

# Relatório executivo (resumido)
python relatorio_final.py --executivo --pages 10

# Relatório com gráficos
python relatorio_final.py --graficos todos --formato png
show_analysis.py - Demonstração de Análises
bash
# Mostrar análise interativa
python show_analysis.py --interativo --dataset nypd.csv

# Demonstração passo a passo
python show_analysis.py --tutorial --passo-a-passo

# Exportar demonstração
python show_analysis.py --export-demo demo_analysis.ipynb
5. 🛠️ UTILITÁRIOS E EXEMPLOS
analisar.sh - Script Shell de Automação
bash
# Executar pipeline completo
bash analisar.sh --pipeline completo

# Executar etapas específicas
bash analisar.sh --etapas limpeza analise visualizacao

# Executar com logs detalhados
bash analisar.sh --verbose --log analise.log
video_demo.sh - Demonstração em Vídeo
bash
# Criar demonstração em vídeo
bash video_demo.sh --criar --output demonstracao.mp4

# Extrair frames do vídeo
bash video_demo.sh --extrair-frames --fps 30

# Comprimir vídeo
bash video_demo.sh --comprimir --quality medium
Scripts de Exemplo/Estudo:
python_matematica.py - Operações Matemáticas
bash
# Exemplos matemáticos
python python_matematica.py --operacao estatisticas
python python_matematica.py --operacao algebra
python python_matematica.py --operacao calculo
Sequência de Números e Precisão.py - Exemplos Numéricos
bash
# Testar precisão numérica
python "Sequência de Números e Precisão.py" --teste float

# Gerar sequências
python "Sequência de Números e Precisão.py" --sequencia fibonacci --tamanho 20
Tipos Básicos e Typecasting.py - Tipos de Dados
bash
# Demonstração de tipos
python "Tipos Básicos e Typecasting.py" --demo tipos

# Conversões (typecasting)
python "Tipos Básicos e Typecasting.py" --conversoes todas
📖 EXEMPLOS DE USO COMBINADO
Pipeline Completo de Análise:
bash
# 1. Processar dados
python analisar_nypd.py --processar --input dados_brutos.csv

# 2. Análise demográfica
python analise_demografica.py --variavel RACE --output demografia.json

# 3. Análise temporal  
python analise_temporal.py --periodo mensal --output tendencias.png

# 4. Dashboard
streamlit run app.py
Análise Rápida com Exportação:
bash
# Análise rápida + relatório
python analise_rapida.py --quick | tee analise_rapida.txt
python relatorio_final.py --resumido --output relatorio.pdf
Processamento em Lote:
bash
# Processar múltiplos anos
for ano in {2020..2023}; do
    python analise_temporal.py --ano $ano --output analise_$ano.csv
done
⚙️ PARÂMETROS COMUNS A TODOS OS SCRIPTS
Parâmetros Gerais:
bash
# Ajuda e documentação
python qualquer_script.py --help
python qualquer_script.py -h

# Modo verboso (logs detalhados)
python qualquer_script.py --verbose
python qualquer_script.py -v

# Especificar dataset
python qualquer_script.py --dataset caminho/para/dados.csv
python qualquer_script.py -d dados.csv

# Especificar output
python qualquer_script.py --output resultado.ext
python qualquer_script.py -o saida/

# Modo de execução
python qualquer_script.py --dry-run  # Simulação
python qualquer_script.py --force    # Forçar execução
Parâmetros de Configuração:
bash
# Configuração de memória
python qualquer_script.py --memory-limit 4GB

# Configuração de threads
python qualquer_script.py --threads 2

# Configuração de logging
python qualquer_script.py --log-file analise.log --log-level INFO
🔍 COMANDOS DE DIAGNÓSTICO
Verificar Dependências:
bash
# Verificar se todos os scripts funcionam
for script in *.py; do
    echo "Testando: $script"
    python "$script" --help 2>/dev/null && echo "✓ OK" || echo "✗ Erro"
done
Testar Performance:
bash
# Medir tempo de execução
time python analise_completa.py --quick

# Perfil de memória
python -m memory_profiler analisar_nypd.py
Validar Dados:
bash
# Validar integridade dos dados
python estrutura.py --validate --dataset nypd.csv

# Checar consistência
python inspecionar.py --check-consistency --colunas-chave ID DATE
🎨 EXEMPLOS PRÁTICOS PARA DOCUMENTAÇÃO
Exemplo 1: Pipeline de Análise Diária
bash
#!/bin/bash
# pipeline_analise_diaria.sh

# 1. Processar novos dados
python analisar_nypd.py --input novos_dados.csv --output processado/

# 2. Gerar análises
python analise_demografica.py --output analises/demografia_$(date +%Y%m%d).json
python analise_temporal.py --output analises/temporal_$(date +%Y%m%d).png

# 3. Atualizar dashboard
cp analises/* dashboard/static/

# 4. Gerar relatório
python relatorio_final.py --output relatorios/relatorio_$(date +%Y%m%d).pdf
Exemplo 2: Monitoramento Contínuo
bash
#!/bin/bash
# monitoramento.sh

while true; do
    # Verificar novos dados
    python ver_dados.py --monitor --intervalo 300
    
    # Se houver novos dados, processar
    if [ $? -eq 0 ]; then
        python analisar_nypd.py --processar
        streamlit run app.py --server.port 8501 &
    fi
    
    sleep 60  # Aguardar 1 minuto
done
Exemplo 3: Treinamento/Workshop
bash
#!/bin/bash
# workshop_analise_dados.sh

echo "🎯 Workshop: Análise de Dados com Python"
echo "========================================"

# 1. Introdução
python "Tipos Básicos e Typecasting.py" --demo

# 2. Inspeção de dados
python inspecionar.py --dataset exemplo.csv --interativo

# 3. Análise básica
python analise_simples.py --describe --colunas todas

# 4. Visualização
python ver_dados.py --view grafico --tipo histograma

# 5. Dashboard
echo "Abrindo dashboard..."
streamlit run app.py
📊 MATRIZ DE COMANDOS POR FUNCIONALIDADE
Função	Script Principal	Comando Exemplo
Dashboard	app.py	streamlit run app.py
Processamento	analisar_nypd.py	python analisar_nypd.py --processar
Análise Demográfica	analise_demografica.py	python analise_demografica.py --variavel RACE
Análise Temporal	analise_temporal.py	python analise_temporal.py --periodo mensal
Relatórios	relatorio_final.py	python relatorio_final.py --completo
Inspeção	inspecionar.py	python inspecionar.py --head 50
Validação	estrutura.py	python estrutura.py --validate
Visualização	ver_dados.py	python ver_dados.py --view table