# 🔬 Controle de Qualidade Farmacêutico — Análise e Detecção de Lotes Fora do Padrão

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)
![Área](https://img.shields.io/badge/Área-Data%20Science%20Industrial-green)

## Sobre o Projeto

Este projeto aplica técnicas de Ciência de Dados a dados simulados de controle de qualidade de uma linha de produção farmacêutica, com o objetivo de:

- Realizar análise exploratória (EDA) de parâmetros críticos de qualidade (CPPs e CQAs)
- Identificar padrões e desvios em dados de processo e produto
- Construir um modelo preditivo simples para detectar lotes com risco de não conformidade

O contexto é inspirado em ambientes regulados sob **GAMP 5** e **21 CFR Part 11**, onde a integridade e rastreabilidade dos dados de qualidade são requisitos críticos.

---

## Motivação

Em indústrias farmacêuticas, a detecção tardia de lotes fora do padrão gera retrabalho, descarte de produto e risco regulatório. A aplicação de análise de dados e modelos preditivos sobre parâmetros de processo e resultado de testes pode antecipar desvios, reduzindo perdas e aumentando a confiabilidade do processo produtivo.

---

## Dataset

Os dados foram **simulados com base em parâmetros realistas** de processos farmacêuticos (compressão de comprimidos), incluindo:

| Variável | Descrição |
|---|---|
| `lote` | Identificador do lote |
| `data_producao` | Data de produção |
| `turno` | Turno de produção (A, B, C) |
| `temp_processo` | Temperatura média do processo (°C) |
| `umidade_relativa` | Umidade relativa do ambiente (%) |
| `pressao_compressao` | Pressão de compressão (kN) |
| `dureza_media` | Dureza média dos comprimidos (N) |
| `friabilidade` | Friabilidade (%) |
| `peso_medio` | Peso médio (mg) |
| `dissolucao` | Dissolução em 45min (%) |
| `status_lote` | `APROVADO` / `REPROVADO` (variável alvo) |

> **Nota:** Os dados são fictícios e gerados para fins educacionais. Não representam dados reais de nenhuma empresa.

---

## Estrutura do Projeto

```
projeto_qc_farma/
│
├── data/
│   ├── raw/                  # Dados brutos gerados
│   └── processed/            # Dados tratados e prontos para modelagem
│
├── notebooks/
│   ├── 01_geracao_dados.ipynb        # Geração do dataset simulado
│   ├── 02_eda.ipynb                  # Análise exploratória de dados
│   └── 03_modelo_preditivo.ipynb     # Modelo de detecção de lotes fora do padrão
│
├── src/
│   └── utils.py              # Funções auxiliares reutilizáveis
│
├── reports/
│   └── figures/              # Gráficos exportados
│
├── requirements.txt
└── README.md
```

---

## Metodologia

```
1. Geração dos dados simulados
        ↓
2. Análise Exploratória (EDA)
   - Distribuição dos parâmetros por status do lote
   - Correlações entre variáveis de processo e resultado
   - Análise de tendências por turno e período
   - Gráficos de controle (SPC) para parâmetros críticos
        ↓
3. Pré-processamento
   - Tratamento de valores ausentes
   - Normalização de variáveis numéricas
   - Encoding de variáveis categóricas
        ↓
4. Modelagem Preditiva
   - Baseline: Regressão Logística
   - Modelo principal: Random Forest
   - Avaliação: Matriz de confusão, ROC-AUC, Precision-Recall
   - Interpretabilidade: Feature Importance
```

---

## Tecnologias Utilizadas

- **Python 3.10+**
- **Pandas** — manipulação e análise de dados
- **NumPy** — operações numéricas
- **Matplotlib / Seaborn** — visualização de dados
- **Scikit-learn** — modelagem preditiva
- **Jupyter Notebook** — desenvolvimento e documentação

---

## Como Executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/projeto-qc-farma.git
cd projeto-qc-farma

# Instale as dependências
pip install -r requirements.txt

# Execute os notebooks na ordem:
# 01 → 02 → 03
```

---

## Resultados Esperados

- Identificação das variáveis de processo com maior influência no status do lote
- Modelo capaz de sinalizar lotes com risco de reprovação antes do resultado final dos testes
- Visualizações claras e interpretáveis para suporte à tomada de decisão em ambiente produtivo

---

## Contexto Profissional

Este projeto é parte do portfólio de transição de carreira para Ciência de Dados de um profissional com 14 anos de experiência em Automação Industrial, sendo 6 deles em indústrias farmacêuticas e biofarmacêuticas reguladas.

A escolha do tema reflete aplicação direta de conhecimento de domínio — parâmetros críticos de processo, ambiente regulado, rastreabilidade de lotes — combinado com técnicas de análise de dados e aprendizado de máquina.

---

## Autor

**Guilherme**
Especialista em Automação Industrial | Transição para Ciência de Dados
[LinkedIn](#) • [GitHub](#)
