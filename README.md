
Simulador de Alocação de Blocos

Este projeto é um simulador de alocação de blocos de memória em disco, implementado com Python e uma interface gráfica utilizando Tkinter. Ele permite alocar, visualizar e excluir arquivos de acordo com três métodos de alocação: contígua, encadeada e indexada.

---

⚙️ Funcionalidades

1. Alocação de Arquivos:
   - Permite criar arquivos com um nome e um número de blocos.
   - Suporta três modos de alocação:
     - Contígua: Aloca blocos consecutivos no disco.
     - Encadeada: Aloca blocos livres, mas conectados logicamente.
     - Indexada: Usa um bloco como índice para apontar para outros blocos alocados.

2. Exclusão de Arquivos:
   - Remove os arquivos selecionados, liberando os blocos ocupados.

3. Visualização Gráfica:
   - Mostra o estado do disco com blocos preenchidos e livres.
   - Realça os blocos de um arquivo selecionado.

4. Tabela de Arquivos:
   - Lista os arquivos armazenados com seus respectivos blocos alocados.

---

🚀 Como Executar o Código

1. Instalar o Python
   - Acesse o site oficial do Python: https://www.python.org/
   - Faça o download da versão mais recente para o seu sistema operacional.
   - Durante a instalação, marque a opção "Add Python to PATH".
   - Verifique a instalação abrindo o terminal e digitando:
     python --version
     Ou, em alguns casos:
     python3 --version

2. Baixar o Código
   - Faça o download do arquivo disk_simulator.py ou clone o repositório.
     git clone https://github.com/eduardo198272/memory_control_soII.git
     cd memory_control_soII

3. Executar o Programa
   - Abra o terminal na pasta do projeto.
   - Execute o seguinte comando:
     python disk_simulator.py
     Ou, caso necessário:
     python3 disk_simulator.py

4. A interface gráfica será exibida, pronta para uso.

---

🖥️ Como Usar a Interface

1. Criar Arquivos
   - Preencha os campos:
     - Nome do Arquivo: Nome para identificar o arquivo.
     - Blocos: Número de blocos necessários para o arquivo.
   - Escolha o Modo de Alocação:
     - Contígua, Encadeada ou Indexada.
   - Clique em Criar Arquivo.

2. Excluir Arquivos
   - Digite o nome do arquivo no campo Nome do Arquivo.
   - Clique em Excluir Arquivo.

3. Visualizar Arquivos e Blocos
   - A tabela lista os arquivos e seus blocos alocados.
   - Clique em um item na tabela para destacar visualmente os blocos no disco.

---

⚠️ Observações Importantes

1. Alterar o Tamanho do Disco
   - O tamanho do disco (quantidade de blocos) é definido pela constante DISK_SIZE no início do código.
   - Para modificar, edite o valor diretamente no código:
     DISK_SIZE = 100  # Altere para o número de blocos desejado.

2. Requisitos do Sistema
   - O programa requer apenas Python e não utiliza bibliotecas externas.

3. Limitações
   - O tamanho do disco é fixo durante a execução.
   - A interface e os blocos simulados são uma representação gráfica simples.

---

📂 Estrutura do Código

- DiskSimulator
  - Classe principal que gerencia a alocação, exclusão e visualização dos blocos.
- SimulatorGUI
  - Classe responsável pela interface gráfica e interatividade com o usuário.

---

🎉 Conclusão

Este simulador é uma ferramenta educativa para entender os diferentes métodos de alocação de blocos em sistemas de arquivos. Modifique o tamanho do disco ou o comportamento do simulador para explorar mais possibilidades!
