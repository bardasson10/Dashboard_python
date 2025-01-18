# Como Instalar e Executar o Projeto

Siga os passos abaixo para configurar e executar este projeto em sua máquina local.

---

## Pré-requisitos

1. **Python 3.10 ou superior**  
   Verifique se o Python está instalado na sua máquina:
   ```bash
   python --version
   ```
   Caso necessário, faça o download [aqui](https://www.python.org/downloads/).

2. **Pip**  
   O gerenciador de pacotes do Python deve estar instalado. Verifique com:
   ```bash
   pip --version
   ```

3. **Virtualenv (Recomendado)**  
   É recomendado criar um ambiente virtual isolado para este projeto. Caso não tenha o `virtualenv` instalado:
   ```bash
   pip install virtualenv
   ```

---

## Passo a Passo para Configuração

### 1. Clone o repositório

Use o comando abaixo para clonar o projeto para sua máquina local:
```bash
git clone <URL_DO_REPOSITORIO>
```

### 2. Acesse o diretório do projeto

Navegue até o diretório clonado:
```bash
cd <NOME_DO_PROJETO>
```

### 3. Crie um ambiente virtual

Crie um ambiente virtual com o nome **`venv`**:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instale as dependências

Certifique-se de estar no diretório do projeto e execute:
```bash
pip install -r requirements.txt
```

---

## Execução do Projeto

### 1. Verifique as configurações

- Certifique-se de que os arquivos necessários, como `FCT_Compras.xlsx`, estão no diretório correto. 
- Caso necessário, atualize os caminhos no arquivo `bancoDeDados.py` ou mova os arquivos para os locais esperados.

### 2. Execute o aplicativo

Inicie o Streamlit com o comando:
```bash
streamlit run app.py
```

### 3. Acesse o projeto no navegador

- Após executar o comando, um link será gerado no terminal, como:  
  `http://localhost:8501`
- Abra esse link em seu navegador para visualizar o aplicativo.

---

## Solução de Problemas

### 1. Ambiente virtual não ativado
Certifique-se de que o ambiente virtual foi ativado antes de executar o projeto. Ative o ambiente novamente caso precise:
- **Windows:**  
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**  
  ```bash
  source venv/bin/activate
  ```

### 2. Erro `FileNotFoundError`
- Verifique se o arquivo `FCT_Compras.xlsx` está no caminho correto.
- Ajuste o caminho no código, se necessário.

### 3. Dependências ausentes
- Se algum erro relacionado a dependências ocorrer, certifique-se de ter instalado todas as bibliotecas com:
  ```bash
  pip install -r requirements.txt
  ```
- Para instalar uma dependência manualmente, use:
  ```bash
  pip install <nome_da_dependencia>
  ```

---

### Nota importante: 

Certifique-se de adicionar a pasta `venv` ao arquivo `.gitignore` para evitar que o ambiente virtual seja enviado ao repositório. O arquivo `.gitignore` já inclui uma linha para ignorar `venv/`. Caso não esteja, adicione:

```plaintext
venv/
```
