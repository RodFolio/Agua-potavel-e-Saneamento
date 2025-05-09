# Agua-potavel-e-Saneamento

Workspace: # Sistema de Denúncias de Saneamento

## Descrição
O **Sistema de Denúncias de Saneamento** é uma aplicação em Python que permite o registro, consulta e gerenciamento de denúncias relacionadas a problemas de saneamento básico em diferentes bairros. O sistema organiza as denúncias em uma estrutura de árvore binária, facilitando a busca por bairro, além de manter um histórico de ações e uma fila de atendimento para priorização.

## Funcionalidades
1. **Cadastrar nova denúncia**  
   Permite registrar uma nova denúncia informando:
   - Tipo do problema
   - Descrição do problema
   - Data do ocorrido
   - Bairro onde ocorreu
   - Prioridade (Alta, Média ou Baixa)

2. **Ver todas as denúncias**  
   Exibe todas as denúncias registradas no sistema.

3. **Ver fila de atendimento**  
   Mostra a fila de atendimento, ordenada pela ordem de registro das denúncias.

4. **Ver histórico de ações**  
   Exibe o histórico de ações realizadas no sistema, como o registro de novas denúncias.

5. **Buscar denúncias por bairro**  
   Permite buscar todas as denúncias registradas em um bairro específico.

6. **Sair do sistema**  
   Encerra a execução do programa.

## Estrutura do Código
O código está dividido em funções e classes que implementam as funcionalidades do sistema:

### Classes
- **

Denuncia_bairro

**  
  Representa uma denúncia, contendo:
  - Tipo do problema
  - Descrição
  - Data
  - Local (bairro)
  - Prioridade

- **

NoBairro

**  
  Representa um nó da árvore binária de bairros, contendo:
  - Nome do bairro
  - Lista de denúncias associadas ao bairro
  - Referências para os nós esquerdo e direito da árvore

### Funções
- **`inserir_bairro(raiz, bairro, denuncia)`**  
  Insere um novo bairro na árvore binária ou adiciona uma denúncia a um bairro existente.

- **`buscar_denuncias_bairro(raiz, bairro)`**  
  Busca todas as denúncias associadas a um bairro específico na árvore binária.

- **

sistema_denuncias()

**  
  Função principal que implementa o menu interativo do sistema e gerencia as opções escolhidas pelo usuário.

- **

loading_animado()

** *(definida em 

inicio.py

)*  
  Exibe uma animação de carregamento ao iniciar o sistema.

## Estrutura de Dados
- **Árvore Binária**  
  Utilizada para organizar os bairros e suas respectivas denúncias, permitindo buscas eficientes.

- **Deque**  
  Utilizado para gerenciar a fila de atendimento.

- **Lista**  
  Utilizada para armazenar o histórico de ações e todas as denúncias registradas.

## Fluxo de Execução
1. O programa inicia com uma animação de carregamento.
2. O menu principal é exibido, permitindo ao usuário escolher uma das opções disponíveis.
3. Dependendo da opção escolhida, o sistema realiza a ação correspondente:
   - Registrar uma nova denúncia
   - Exibir todas as denúncias
   - Mostrar a fila de atendimento
   - Exibir o histórico de ações
   - Buscar denúncias por bairro
   - Encerrar o sistema

## Exemplo de Uso
### Cadastro de Denúncia
1. Escolha a opção **1** no menu.
2. Insira os dados da denúncia:
   - Tipo: "Falta de água"
   - Descrição: "Falta de água há 3 dias"
   - Data: "10/10/2025"
   - Bairro: "Centro"
   - Prioridade: "1" (Alta)
3. A denúncia será registrada e adicionada à árvore binária, à lista de denúncias e à fila de atendimento.

### Busca por Bairro
1. Escolha a opção **5** no menu.
2. Insira o nome do bairro, por exemplo, "Centro".
3. O sistema exibirá todas as denúncias registradas para o bairro informado.

## Requisitos
- **Python 3.6+**
- Biblioteca padrão do Python (não são necessárias dependências externas)

## Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/agua-potavel-e-saneamento.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd agua-potavel-e-saneamento
   ```
3. Execute o programa:
   ```bash
   python inicio.py
   ```

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

## Autor
Desenvolvido por **RodFolio**.

RodFolio: @workspace Quais seções você gostaria de adicionar?

Workspace: Pelo contexto do código e da aplicação, seria interessante adicionar as seguintes seções ao README para torná-lo mais completo e informativo:

1. **Visão Geral**  
   Uma breve explicação sobre o propósito do sistema e o problema que ele resolve.

2. **Tecnologias Utilizadas**  
   Lista das tecnologias e bibliotecas usadas no projeto.

3. **Instalação e Configuração**  
   Instruções detalhadas para configurar e executar o sistema localmente.

4. **Exemplos de Uso**  
   Exemplos práticos de como interagir com o sistema, incluindo entradas e saídas esperadas.

5. **Estrutura do Projeto**  
   Explicação sobre a organização dos arquivos e diretórios no projeto.

6. **Contribuição**  
   Orientações para quem deseja contribuir com o projeto.

7. **Licença**  
   Detalhes sobre a licença do projeto (já está presente, mas pode ser expandida).