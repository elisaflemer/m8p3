# Ponderada 3, módulo 8

Esta ponderada tem como objetivo a criação de um chatbot simples em Python baseado em regex, com um dicionário de intenções e um de ações. Isso deve ser feito como um nó de ROS2.

## Recursos

### Reconhecimento de Intenção
O chatbot utiliza um conjunto de expressões regulares para reconhecer as intenções do usuário. O dicionário intent_dict mapeia expressões regulares para intenções específicas, como saudações, perguntas sobre o bem-estar, despedidas e solicitações de navegação. Por exemplo, expressões como "olá", "como você está" e "adeus" estão associadas às intenções "greetings", "genki" e "bye", respectivamente.

### Execução de Ações
Ao reconhecer a intenção do usuário, o chatbot executa ações correspondentes usando o dicionário action_dict. As ações variam de respostas amigáveis a navegação do robô para destinos específicos. Por exemplo, a ação "greet_back" responde com um cumprimento, enquanto a ação "go_to" calcula e exibe as coordenadas de destinos pré-definidos com base nos comandos do usuário.

### Mapeamento de Destinos e Coordenadas
O chatbot inclui destinos pré-definidos (destinos) e suas coordenadas correspondentes (coordenadas). Esses mapeamentos facilitam a navegação do robô quando o usuário emite comandos para ir a um lugar específico. Por exemplo, locais como "skol", "brahma" e "ze delivery" estão associados às suas respectivas coordenadas no espaço, permitindo que o robô navegue autonomamente.

## Instalação

1. Clone este repositório em seu ambiente ROS 2:

    ```bash
    git clone https://github.com/seu_usuario/seu_repositorio.git
    ```

2. Navegue até o diretório do repositório:

    ```bash
    cd m8p3
    ```
    
3. Construa o workspace ROS 2:

    ```bash
    colcon build
    ```

## Configuração do Ambiente

1. Execute o comando a seguir para adicionar os executáveis do seu workspace ao seu ambiente:

    ```bash
    source install/setup.bash
    ```

    Certifique-se de executar este comando sempre que abrir uma nova sessão do terminal ou adicione-o ao seu arquivo de inicialização, como `.bashrc` ou `.zshrc`.

## Execução do Nó

1. Execute o nó `chatbot` com o pacote 'chatbot':

    ```bash
    ros2 run chatbot chatbot
    ```

Isso é tudo! Agora, o nó ROS 2 deve estar em execução. Para começar a conversar com o robô, basta digitar "oi" e, depois, para onde deseja ir. Ele entenderá expressões como "vai para", "ir até", "me leve até", etc.

## Demo

[demo.webm](https://github.com/elisaflemer/m8p3/assets/99259251/758926ae-7b8a-4422-abe2-2b0fddcc00f4)
