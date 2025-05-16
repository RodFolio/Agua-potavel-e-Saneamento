# Sistema de Denúncias de Saneamento

## 📌 Descrição
O **Sistema de Denúncias de Saneamento** é uma aplicação em Python que permite o registro, consulta, atendimento e gerenciamento de denúncias relacionadas a problemas de saneamento básico em diferentes bairros. O sistema organiza as denúncias em uma **árvore binária** (para buscas por bairro), mantém uma **fila de atendimento priorizada**, e registra um **histórico de ações**.

## ⚙️ Funcionalidades

1. **Cadastrar nova denúncia**  
   Permite registrar uma nova denúncia com os seguintes dados:
   - Tipo do problema
   - Descrição
   - Data do ocorrido
   - Bairro (local)
   - Prioridade (Alta = 1, Média = 2, Baixa = 3)

2. **Ver todas as denúncias**  
   Lista todas as denúncias registradas no sistema.

3. **Ver fila de atendimento**  
   Exibe a fila de atendimento **ordenada por prioridade** (1 mais urgente → 3 menos urgente).

4. **Ver histórico de ações**  
   Mostra todas as ações realizadas, como denúncias registradas ou atendidas.

5. **Buscar denúncias por bairro**  
   Permite pesquisar todas as denúncias de um bairro específico.

6. **Atender próxima denúncia**  
   Remove da fila e atende a denúncia com **maior prioridade (menor valor)**, registrando no histórico.

0. **Sair do sistema**  
   Encerra a execução do programa.

## 🧱 Estrutura do Código

### 📦 Classes

#### `Denuncia_bairro`
Representa uma denúncia individual. Atributos:
- Tipo do problema
- Descrição
- Data
- Local (bairro)
- Prioridade (1, 2 ou 3)

#### `NoBairro`
Representa um nó na árvore binária. Atributos:
- Nome do bairro
- Lista de denúncias associadas
- Referências à esquerda e à direita (subárvores)

### 🔧 Funções

- `inserir_bairro(raiz, bairro, denuncia)`  
  Insere um novo bairro ou adiciona uma denúncia a um bairro existente na árvore binária.

- `buscar_denuncias_bairro(raiz, bairro)`  
  Retorna a lista de denúncias associadas a um bairro específico.

- `sistema_denuncias()`  
  Função principal que executa o menu interativo e gerencia as funcionalidades do sistema.

> 💡 **Nota**: A função `loading_animado()` (definida em `inicio.py`) pode ser chamada antes de `sistema_denuncias()` para exibir uma animação de carregamento ao iniciar.

## 🗂️ Estruturas de Dados Utilizadas

- **Árvore Binária**  
  Organiza os bairros e suas denúncias, otimizando a busca por nome.

- **Deque (Fila de Atendimento)**  
  Armazena denúncias pendentes. Na visualização ou atendimento, é ordenada por prioridade.

- **Lista**  
  Utilizada para:
  - Armazenar todas as denúncias
  - Registrar o histórico de ações

## 🔁 Fluxo de Execução

1. (Opcional) A animação de carregamento é exibida.
2. O usuário interage com o menu principal.
3. Cada opção chama a funcionalidade correspondente, como:
   - Registrar denúncia
   - Exibir dados
   - Atender denúncia mais urgente
   - Buscar por bairro
   - Encerrar o programa

## 🧪 Exemplos de Uso

### ✅ Cadastro de Denúncia
1. Escolha a opção `1` no menu.
2. Preencha os dados:
   - Tipo: `Falta de água`
   - Descrição: `Sem fornecimento há 3 dias`
   - Data: `10/10/2025`
   - Bairro: `Centro`
   - Prioridade: `1` (Alta)
3. A denúncia será adicionada à lista geral, à fila de atendimento e ao bairro na árvore binária.

### 🔍 Busca por Bairro
1. Escolha a opção `5`.
2. Digite o nome do bairro, como `Centro`.
3. O sistema listará todas as denúncias registradas para esse bairro.

### 🛠️ Atendimento de Denúncia
1. Escolha a opção `6`.
2. O sistema localizará e atenderá a **denúncia de maior prioridade** (prioridade 1 > 2 > 3).
3. A denúncia será removida da fila e adicionada ao histórico.

## 💻 Requisitos
- Python **3.6** ou superior
- Apenas bibliotecas padrão do Python (`collections`)

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/agua-potavel-e-saneamento.git
