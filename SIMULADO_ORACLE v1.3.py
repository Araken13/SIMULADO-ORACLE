import streamlit as st
from datetime import datetime, timedelta

# Tempo limite
TEMPO_LIMITE = timedelta(minutes=90)

# Inicializa sessão
if "inicio_teste" not in st.session_state:
    st.session_state.inicio_teste = datetime.now()
if "indice" not in st.session_state:
    st.session_state.indice = 0
if "respostas" not in st.session_state:
    st.session_state.respostas = []

# Lista de perguntas
questions = [
    {
        "text": "Qual operador do ADS pode ser usado para prever valores futuros com base em séries temporais?",
        "options": ["Detecção de PII", "Agrupamento", "Previsão (Forecasting)", "Detecção de Anomalias"],
        "correct": 2
    },
    {
        "text": "Qual valor de parâmetro de modelo você provavelmente usaria se não tiver certeza da sua escolha ao configurar o operador de previsão?",
        "options": ["autos", "arima", "auto", "prophet"],
        "correct": 2
    },

    # Perguntas_convertidas MD

    {"text": "Qual é a diferença entre um job e uma execução de job (job run) no OCI Data Science Jobs?", "options": ["Um job é usado para treinamento de modelo, enquanto uma execução de job é usada para inferência em lote", "Um job é imutável, enquanto uma execução de job pode ser modificada", "Um job é um template, enquanto uma execução de job é uma execução única desse template", "Um job é uma execução única, enquanto uma execução de job é um template"], "correct": 2},
    {"text": "Onde os resultados do job de treinamento são armazenados após o fine-tuning ser concluído?", "options": ["Em um cache temporário que é excluído após a conclusão do job", "No armazenamento local da instância de treinamento", "Em um bucket do OCI Object Storage", "Diretamente no Catálogo de Modelos da OCI"], "correct": 2},
    {"text": "Qual afirmação está incorreta sobre os benefícios do autoscaling para implantação de modelos na Oracle Data Science?", "options": ["O autoscaling ajusta dinamicamente os recursos computacionais com base na demanda em tempo real", "Os usuários podem definir gatilhos personalizados para autoscaling usando expressões MQL", "O autoscaling, junto com balanceadores de carga, permite redirecionar automaticamente o tráfego para instâncias saudáveis", "Com autoscaling, o custo da implantação permanece constante independentemente da utilização dos recursos"], "correct": 3},
    {"text": "Quais operações do Git são mais afetadas por uma conexão de internet lenta no ambiente de Data Science da OCI?", "options": ["Fazer upload do repositório local para o remoto", "Converter uma pasta local existente em repositório Git", "Fazer um commit local", "Mover alterações para a área de staging"], "correct": 0},
    {"text": "Qual afirmação é verdadeira sobre sobrescrever configurações padrão de um pipeline no OCI Data Science?", "options": ["Os padrões do pipeline não podem ser sobrescritos após sua criação", "Os padrões do pipeline só podem ser sobrescritos durante a criação do pipeline", "Os padrões do pipeline podem ser sobrescritos antes de iniciar a execução do pipeline", "Os padrões do pipeline só podem ser sobrescritos por um administrador"], "correct": 2},
    {"text": "Qual algoritmo de criptografia NÃO é suportado pelo OCI Vault?", "options": ["ECDSA", "AES", "RSA", "SHA-256"], "correct": 3},
    {"text": "O que acontece quando uma implantação de modelo no OCI Data Science é desativada?", "options": ["Os metadados da implantação do modelo são apagados", "O modelo permanece ativo, mas para de aceitar novas requisições", "O modelo implantado é excluído permanentemente", "O endpoint HTTP do modelo fica indisponível, mas os metadados são preservados"], "correct": 3},
    {"text": "Qual operador é mais adequado para ocultar dados pessoais (como nomes, e-mails e telefones) antes de compartilhar registros com uma instituição de pesquisa?", "options": ["Operador de Agrupamento (Clustering)", "Operador de Detecção de PII", "Operador de Previsão", "Operador de Detecção de Anomalias"], "correct": 1},
    {"text": "Qual componente do OCI Data Science permite organizar e versionar modelos treinados?", "options": ["Model Deployment", "Notebook Session", "Model Catalog", "Job Run"], "correct": 2},
    {"text": "Ao usar o operador de Detecção de Anomalias no ADS, qual técnica é comumente aplicada?", "options": ["Regressão Linear", "K-Means", "Isolation Forest", "PCA"], "correct": 2},
    {"text": "Qual é a principal vantagem de usar pipelines no OCI Data Science?", "options": ["Reduzir o custo de armazenamento", "Automatizar fluxos de trabalho de ML", "Melhorar a segurança dos dados", "Evitar o uso de GPUs"], "correct": 1},
    {"text": "Qual operador do ADS é ideal para segmentar clientes com base em comportamento de compra?", "options": ["Previsão", "Detecção de PII", "Agrupamento", "Classificação"], "correct": 2},
    {"text": "Qual biblioteca Python é frequentemente usada para visualização de dados no ambiente OCI Data Science?", "options": ["NumPy", "Matplotlib", "Scikit-learn", "XGBoost"], "correct": 1},
    {"text": "Qual recurso do OCI permite armazenar grandes volumes de dados usados em projetos de Data Science?", "options": ["Vault", "Object Storage", "Functions", "Data Catalog"], "correct": 1},
    {"text": "Qual operador do ADS pode ser usado para prever se um cliente vai cancelar um serviço?", "options": ["Classificação", "Agrupamento", "Detecção de PII", "Previsão"], "correct": 0},
    {"text": "Qual é o papel do operador de Classificação no ADS?", "options": ["Dividir dados em grupos sem rótulos", "Prever valores contínuos", "Identificar outliers", "Atribuir categorias a dados com base em rótulos"], "correct": 3},
    {"text": "Qual ferramenta do OCI Data Science permite executar scripts Python em lote?", "options": ["Notebook Session", "Job", "Model Deployment", "Pipeline Step"], "correct": 1},
    {"text": "Qual operador do ADS é mais adequado para prever vendas futuras com base em dados históricos?", "options": ["Classificação", "Agrupamento", "Previsão", "Detecção de PII"], "correct": 2},
    {"text": "Qual operador do ADS é mais adequado para identificar padrões incomuns em dados financeiros?", "options": ["Previsão", "Detecção de Anomalias", "Classificação", "Agrupamento"], "correct": 1},
    {"text": "Qual recurso do OCI permite versionar notebooks e colaborar com equipes?", "options": ["Object Storage", "Notebook Sessions", "Git Integration", "Vault"], "correct": 2},
    {"text": "Qual tipo de modelo é mais indicado para prever preços de imóveis com base em características?", "options": ["Classificação", "Agrupamento", "Regressão", "Detecção de PII"], "correct": 2},
    {"text": "Qual operador do ADS pode ser usado para dividir dados em grupos sem rótulos?", "options": ["Classificação", "Agrupamento", "Previsão", "Detecção de Anomalias"], "correct": 1},
    {"text": "Qual biblioteca é comumente usada para manipulação de dados tabulares no Python?", "options": ["Matplotlib", "NumPy", "Pandas", "Seaborn"], "correct": 2},
    {"text": "Qual operador do ADS é mais adequado para prever churn de clientes?", "options": ["Classificação", "Agrupamento", "Previsão", "Detecção de PII"], "correct": 0},
    {"text": "Qual ferramenta do OCI permite criar fluxos de trabalho automatizados com múltiplos passos?", "options": ["Notebook Session", "Job", "Pipeline", "Vault"], "correct": 2},
    {"text": "Qual operador do ADS pode ser usado para prever demanda futura de produtos?", "options": ["Classificação", "Agrupamento", "Previsão", "Detecção de PII"], "correct": 2},
    {"text": "Qual tipo de dado é considerado PII?", "options": ["Temperatura", "ID do produto", "Endereço de e-mail", "Categoria de produto"], "correct": 2},
    {"text": "Qual operador do ADS é mais indicado para categorizar e-mails como spam ou não spam?", "options": ["Agrupamento", "Classificação", "Previsão", "Detecção de PII"], "correct": 1},
    {"text": "Qual biblioteca é usada para aprendizado de máquina no Python?", "options": ["Scikit-learn", "Matplotlib", "Pandas", "Seaborn"], "correct": 0},
    {"text": "Qual operador do ADS pode ser usado para detectar fraudes em transações?", "options": ["Previsão", "Detecção de Anomalias", "Classificação", "Agrupamento"], "correct": 1},
    {"text": "Qual recurso do OCI permite armazenar segredos e chaves criptográficas?", "options": ["Vault", "Object Storage", "Notebook Session", "Model Deployment"], "correct": 0},
    {"text": "Qual operador do ADS é mais indicado para prever o tempo de entrega de pedidos?", "options": ["Classificação", "Agrupamento", "Previsão", "Detecção de PII"], "correct": 2},
    {"text": "Qual biblioteca é usada para criar gráficos estatísticos no Python?", "options": ["Seaborn", "NumPy", "Pandas", "Scikit-learn"], "correct": 0},
    {"text": "Qual operador do ADS pode ser usado para segmentar usuários com base em comportamento?", "options": ["Classificação", "Agrupamento", "Previsão", "Detecção de PII"], "correct": 1},
    {"text": "Qual tipo de modelo é mais indicado para prever notas de alunos com base em desempenho?", "options": ["Classificação", "Agrupamento", "Regressão", "Detecção de PII"], "correct": 2},
    {"text": "Qual operador do ADS é mais indicado para prever consumo de energia?", "options": ["Classificação", "Agrupamento", "Previsão", "Detecção de PII"], "correct": 2},
    {"text": "Qual biblioteca é usada para cálculos numéricos no Python?", "options": ["NumPy", "Matplotlib", "Pandas", "Seaborn"], "correct": 0},
    {"text": "Qual operador do ADS pode ser usado para detectar comportamento incomum em sensores?", "options": ["Previsão", "Detecção de Anomalias", "Classificação", "Agrupamento"], "correct": 1},
    {"text": "Qual recurso do OCI permite executar código em notebooks interativos?", "options": ["Notebook Session", "Vault", "Object Storage", "Model Deployment"], "correct": 0},
    {"text": "Qual operador do ADS pode ser usado para prever receita mensal?", "options": ["Classificação", "Agrupamento", "Previsão", "Detecção de PII"], "correct": 2},
    {"text": "Qual biblioteca é usada para visualização de dados em gráficos de linha e barra?", "options": ["Matplotlib", "NumPy", "Pandas", "Scikit-learn"], "correct": 0},
    {"text": "Qual operador do ADS pode ser usado para classificar produtos por categoria?", "options": ["Classificação", "Agrupamento", "Previsão", "Detecção de PII"], "correct": 0},
    {"text": "Qual tipo de modelo é mais indicado para prever número de vendas?", "options": ["Classificação", "Agrupamento", "Regressão", "Detecção de PII"], "correct": 2},
    {"text": "Qual operador do ADS pode ser usado para identificar clientes com comportamento fora do padrão?", "options": ["Previsão", "Detecção de Anomalias", "Classificação", "Agrupamento"], "correct": 1},
    {"text": "Qual biblioteca é usada para manipular arrays multidimensionais?", "options": ["NumPy", "Matplotlib", "Pandas", "Seaborn"], "correct": 0},
    {"text": "Qual operador do ADS pode ser usado para prever tempo de resposta de servidores?", "options": ["Classificação", "Agrupamento", "Previsão", "Detecção de PII"], "correct": 2},
    {"text": "Qual operador do ADS pode ser usado para agrupar produtos similares?", "options": ["Classificação", "Agrupamento", "Previsão", "Detecção de PII"], "correct": 1},
    {"text": "Qual operador do ADS pode ser usado para prever número de visitantes em um site?", "options": ["Classificação", "Agrupamento", "Previsão", "Detecção de PII"], "correct": 2}
    
]

# Tempo restante
tempo_restante = TEMPO_LIMITE - (datetime.now() - st.session_state.inicio_teste)
if tempo_restante.total_seconds() <= 0:
    st.session_state.indice = len(questions)  # força avaliação

# Exibe cronômetro
if st.session_state.indice < len(questions):
    minutos, segundos = divmod(int(tempo_restante.total_seconds()), 60)
    st.info(f"⏳ Tempo restante: {minutos:02d}:{segundos:02d}")

# Exibe pergunta atual
if st.session_state.indice < len(questions):
    q = questions[st.session_state.indice]
    st.write(f"**Questão {st.session_state.indice + 1}:** {q['text']}")
    opcoes = ["Selecione uma resposta"] + q["options"]
    resposta = st.radio("Escolha uma opção:", opcoes, key=st.session_state.indice)

    if st.button("Próxima"):
        if resposta == "Selecione uma resposta":
            st.warning("⚠️ Por favor, selecione uma alternativa antes de continuar.")
        else:
            st.session_state.respostas.append(resposta)
            st.session_state.indice += 1
else:
    # Avaliação final
    score = 0
    for i, q in enumerate(questions):
        if i < len(st.session_state.respostas):
            if st.session_state.respostas[i] == q["options"][q["correct"]]:
                score += 1

    total = len(questions)
    porcentagem = (score / total) * 100
    nota = round((porcentagem / 100) * 10, 2)

    st.markdown(f"### ✅ Você acertou **{score}** de **{total}** questões.")
    st.markdown(f"### 📊 Porcentagem de acertos: **{porcentagem:.2f}%**")
    st.markdown(f"### 📝 Sua nota final é: **{nota} / 10**")

    if porcentagem >= 80:
        st.success("🎉 Parabéns! Você foi aprovado.")
    else:
        st.error("❌ Você não atingiu os 80%. Tente novamente.")
