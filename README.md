# Sistema de Denúncias de Saneamento

## 📋 Descrição

Este é um sistema de gerenciamento de denúncias relacionadas a problemas de água e saneamento. O sistema permite registrar, gerenciar e acompanhar denúncias de problemas em diferentes bairros, com um sistema de priorização para atendimento.

![Captura de tela 2025-06-08 204423](https://github.com/user-attachments/assets/b5808fa6-7b69-4a41-9ecf-a259a28c090e)
Deploy: https://agua-potavel-e-saneamento-basico-m9gvteo9z.vercel.app/


## 🚀 Funcionalidades

- Cadastro de denúncias com informações detalhadas
- Sistema de priorização de atendimento
- Busca de denúncias por bairro
- Histórico de ações
- Fila de atendimento ordenada por prioridade
- Interface web moderna e responsiva

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Flask (Framework Web)
- HTML5
- CSS3
- Estrutura de dados: Árvore Binária de Busca

## 📦 Estrutura do Projeto

```
.
├── app.py              # Aplicação principal Flask
├── denuncia.py         # Lógica de negócio e estruturas de dados
├── inicio.py           # Script de inicialização
├── requirements.txt    # Dependências do projeto
├── static/            # Arquivos estáticos (CSS, JS, imagens)
└── templates/         # Templates HTML
```

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone [URL_DO_REPOSITÓRIO]
```

2. Crie um ambiente virtual:

```bash
python -m venv .venv
```

3. Ative o ambiente virtual:

- Windows:

```bash
.venv\Scripts\activate
```

- Linux/Mac:

```bash
source .venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

1. Ative o ambiente virtual (se ainda não estiver ativo)
2. Execute o servidor Flask:

```bash
python app.py
```

3. Acesse o sistema em seu navegador: `http://localhost:5000`

## 📝 Estrutura de Dados

O sistema utiliza uma Árvore Binária de Busca para organizar as denúncias por bairro, permitindo buscas eficientes. Cada denúncia contém:

- Tipo do problema
- Descrição
- Data
- Local (Bairro)
- Prioridade (Alta, Média, Baixa)

## 🎯 Exemplos de Uso

### Cadastro de Denúncia

1. Acesse a página inicial
2. Clique em "Nova Denúncia"
3. Preencha os campos:
   - Tipo do problema
   - Descrição detalhada
   - Data do ocorrido
   - Bairro
   - Nível de prioridade
4. Clique em "Enviar Denúncia"

### Busca por Bairro

1. Acesse a seção "Buscar Denúncias"
2. Digite o nome do bairro
3. Visualize todas as denúncias registradas para o bairro selecionado

### Atendimento de Denúncia

1. Acesse a seção "Fila de Atendimento"
2. As denúncias estarão ordenadas por prioridade
3. Selecione a denúncia para atendimento
4. Registre as ações tomadas

## 🔧 Solução de Problemas

### Problemas Comuns

1. **Servidor não inicia**

   - Verifique se o ambiente virtual está ativo
   - Confirme se todas as dependências foram instaladas
   - Verifique se a porta 5000 está disponível

2. **Erro ao instalar dependências**
   - Atualize o pip: `python -m pip install --upgrade pip`
   - Verifique a conexão com a internet
   - Tente instalar as dependências uma por uma



  
👩‍💻 Equipe de Desenvolvimento:

<a href="https://github.com/iSousadev">Rodolfo Sousa</a>, <a href="https://github.com/maria-ramos652">Maria Eduarda</a>, <a href="https://github.com/camscostney">Camila Costney</a>, <a href="https://github.com/Espakki">Winicius Passaia</a>, <a href="https://github.com/KaiqueCh">Kaique Chaves</a>

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
