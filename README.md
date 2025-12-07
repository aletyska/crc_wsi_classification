# Classificação de Câncer Colorretal em Imagens Histológicas (WSI)

Este projeto tem como objetivo classificar imagens de lâminas histológicas (Whole Slide Images - WSI) de câncer colorretal em 6 categorias distintas, utilizando redes neurais convolucionais (CNNs).

## 📊 Dataset

O conjunto de dados utilizado é o **EBHI-SEG**, obtido através do Kaggle. O projeto faz o download e a organização automática do dataset utilizando a biblioteca `kagglehub` e scripts auxiliares.

As imagens são classificadas em 6 categorias:
- **Normal**
- **Polyp** (Pólipo)
- **Low-grade IN** (Neoplasia Intraepitelial de Baixo Grau)
- **High-grade IN** (Neoplasia Intraepitelial de Alto Grau)
- **Serrated adenoma** (Adenoma Serrilhado)
- **Adenocarcinoma**

### Pré-processamento
As imagens são redimensionadas para **224x224** pixels e normalizadas utilizando as médias e desvios padrão do ImageNet, garantindo compatibilidade com os modelos pré-treinados.

## 🧠 Modelos Implementados

O projeto compara dois arquiteturas de CNN:

1.  **ResNet-18**
    -   Modelo base leve e eficiente.
    -   Otimizador: Adam
    -   Resultados: Acurácia aproximada de **~85%**.

2.  **ConvNeXt-Tiny**
    -   Arquitetura moderna baseada em Transformers (mas puramente convolucional).
    -   Otimizador: AdamW com Cosine Annealing.
    -   Resultados: Acurácia superior, atingindo **~92% a 99%** no conjunto de validação.

## 📂 Estrutura do Projeto

```
.
├── requirements.txt       # Dependências do projeto
├── README.md              # Documentação
└── src/
    ├── CNN-ResNet18.ipynb # Notebook para treino/validação da ResNet-18
    ├── CNN-ConvNeXt.ipynb # Notebook para treino/validação da ConvNeXt
    ├── utils.py           # Scripts para download e estruturação do dataset
    └── datasets/          # Arquivos CSV definindo os splits de treino/validação
```

## 🚀 Como Executar

### Pré-requisitos
Certifique-se de ter Python instalado (recomendado 3.8+).

### Instalação
Instale as dependências listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Treinamento e Avaliação
Para reproduzir os resultados, execute os notebooks localizados na pasta `src/`:

1.  Abra o notebook desejado (ex: `src/CNN-ConvNeXt.ipynb`) no Jupyter Lab, VS Code ou Google Colab.
2.  Execute todas as células.
    -   O script irá baixar o dataset automaticamente na primeira execução.
    -   O dataset será reestruturado e dividido em treino/validação conforme definido em `src/datasets/`.
    -   O modelo será treinado e avaliado, gerando métricas (Acurácia, F1-Score) e Matriz de Confusão.

## 📈 Resultados e Métricas

A avaliação inclui:
-   **Acurácia Global**
-   **Precision, Recall e F1-Score** por classe.
-   **Matriz de Confusão** para visualização de erros por categoria.

O modelo **ConvNeXt-Tiny** demonstrou desempenho superior, especialmente na diferenciação entre classes complexas como neoplasias de alto e baixo grau.
