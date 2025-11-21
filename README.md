# Classificação de Câncer Colorretal em Imagens WSI

Este projeto implementa um modelo de aprendizado profundo para classificar tipos de tecidos em imagens histológicas de câncer colorretal (WSI - Whole Slide Images). O projeto utiliza uma rede neural convolucional (CNN) baseada na arquitetura ResNet-18.

## Sobre o Projeto

O objetivo é classificar imagens em diferentes categorias histológicas utilizando o dataset **EBHI-SEG** disponível no Kaggle. O código realiza o download, pré-processamento, treinamento e validação do modelo.

### Principais Características
- **Modelo**: ResNet-18 pré-treinada (ImageNet).
- **Framework**: PyTorch.
- **Dataset**: Colorectal Cancer WSI (EBHI-SEG).
- **Métricas**: Acurácia, Perda (Loss) e Matriz de Confusão.

## Pré-requisitos

As bibliotecas necessárias para executar este projeto estão listadas no arquivo `requirements.txt`. As principais dependências são:

- `torch`
- `torchvision`
- `pandas`
- `scikit-learn`
- `seaborn`
- `matplotlib`
- `kagglehub`

Para instalar as dependências, execute:

```bash
pip install -r requirements.txt
```

## Como Usar

1.  **Clone o repositório**:
    ```bash
    git clone <url-do-repositorio>
    cd crc_wsi_classification
    ```

2.  **Execute o Notebook**:
    O projeto está contido no notebook `Trabalho_Grau_B_Alessandro_Tyska.ipynb`. Você pode executá-lo localmente usando Jupyter Notebook ou no Google Colab.

    O notebook realiza os seguintes passos automaticamente:
    - Download do dataset via `kagglehub`.
    - Reestruturação das pastas do dataset (remoção de pastas `label` e organização das imagens).
    - Divisão dos dados em treino (80%) e validação (20%).
    - Treinamento do modelo ResNet-18 por um número definido de épocas.
    - Salvamento do modelo treinado em `crc_wsi_model.pth`.
    - Avaliação do modelo e geração da matriz de confusão.

## Estrutura de Arquivos

- `Trabalho_Grau_B_Alessandro_Tyska.ipynb`: Notebook principal com todo o código.
- `requirements.txt`: Lista de dependências.
- `crc_wsi_model.pth`: Arquivo do modelo treinado (gerado após a execução).
- `README.md`: Este arquivo de documentação.

## Resultados

O modelo é avaliado utilizando a acurácia no conjunto de validação e uma matriz de confusão é gerada para visualizar o desempenho em cada classe.

## Autor

Alessandro Tyska
