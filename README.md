# Como Instalar e Executar o Projeto

Siga os passos abaixo para configurar e executar este projeto em sua máquina local.

---

## Pré-requisitos

1. **Python**: Certifique-se de que você tem o Python instalado (versão 3.10 ou superior).
   - Para verificar, use:
     ```bash
     python --version
     ```
   - Se necessário, faça o download [aqui](https://www.python.org/downloads/).

2. **Pip**: O gerenciador de pacotes do Python deve estar instalado.
   - Para verificar, use:
     ```bash
     pip --version
     ```

3. **Virtualenv (Opcional)**: Recomendado para criar um ambiente virtual isolado.
   - Para instalar:
     ```bash
     pip install virtualenv
     ```

---

## Passo a Passo

### 1. Clone o repositório

Use o comando abaixo para clonar o projeto para o seu computador:
```bash
git clone <URL_DO_REPOSITORIO>
```

### 2. Navegue até o diretório do projeto

```bash
cd dashboard
```

### 3. Crie e ative um ambiente virtual (opcional, mas recomendado)

**No Windows:**
```bash
dashboard\Scripts\activate
```

**No Mac/Linux:**
```bash
source dashboard/bin/activate
```

### 4. Instale as dependências

Certifique-se de estar no diretório do projeto e instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### 5. Verifique as configurações do projeto

- Certifique-se de que os arquivos e caminhos utilizados no código estão corretos, especialmente para arquivos como `FCT_Compras.xlsx`.
- Caso necessário, atualize os caminhos diretamente no código ou mova os arquivos para os diretórios esperados.

### 6. Execute o projeto localmente

Inicie o aplicativo com o comando:
```bash
streamlit run app.py
```

### 7. Acesse o aplicativo

- Após executar o comando, um link será gerado no terminal (algo como `http://localhost:8501`).
- Abra esse link no navegador para acessar o projeto.

---

## Solução de Problemas

### Arquivo não encontrado

Se o erro `FileNotFoundError` ocorrer, verifique:
- Se o arquivo `FCT_Compras.xlsx` existe no caminho correto.
- Corrija o caminho no arquivo `bancoDeDados.py`.

### Dependências

Se encontrar erro relacionado a dependências:
- Certifique-se de ter executado o comando `pip install -r requirements.txt` corretamente.
- Use:
  ```bash
  pip install <nome_da_dependencia>
  ```
  para instalar dependências faltantes manualmente.

---

