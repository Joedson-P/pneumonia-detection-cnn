# Detecção de Pneumonia via Raio-X com Deep Learning

Este projeto utiliza **Transfer Learning (MobileNetV2)** para classificar imagens de Raio-X de tórax em duas categorias: **Normal** ou **Pneumonia**. O modelo foi otimizado para alta sensibilidade (Recall), visando auxílio em triagem médica.

## Performance do Modelo
* **Acurácia:** 90%
* **Recall (Pneumonia):** 93%
* **Modelo Base:** MobileNetV2

## Tecnologias Utilizadas
* **Linguagem:** Python 3.12
* **Deep Learning:** TensorFlow / Keras
* **API:** FastAPI & Uvicorn
* **Container:** Docker

## Como Executar

### Via Docker (Recomendado)
1. Certifique-se de ter o Docker instalado.
2. Build da imagem:
   ```bash
   docker build -t pneumonia-api .
   ```
3. Rodar o contâiner:
    ```bash
    docker run -p 8000:8000 pneumonia-api
    ```
4. Acesse a documentação interativa: `http://localhost:8000/docs`

### Via Python Local
1. Crie e ative um ambiente virtual: 
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate
    ```
2. Instale as dependências
    ```bash
    pip install -r requirements.txt
    ```
3. Inicie o servidor:
    ```bash
    python app.py
    ```
4. Teste a API acessando: `http://127.0.0.1:8000/docs`

## Estrutura do Projeto
* `/notebooks`: EDA, Treinamento e Validação.
* `app.py`: Servidor FastAPI.
* `Dockerfile`: Configuração para deploy.