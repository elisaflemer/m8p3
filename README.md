# Ponderada 3, módulo 8

Esta ponderada tem como objetivo a criação de um chatbot simples em Python baseado em regex, com um dicionário de intenções e um de ações. Isso deve ser feito como um nó de ROS2.

## Instalação

1. Clone este repositório em seu ambiente ROS 2:

    ```bash
    git clone https://github.com/seu_usuario/seu_repositorio.git
    ```

2. Navegue até o diretório do repositório:

    ```bash
    cd m8p3
    ```
/demo.webm
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

Isso é tudo! Agora, o nó ROS 2 deve estar em execução.

## Demo

[demo.webm](https://github.com/elisaflemer/m8p3/assets/99259251/758926ae-7b8a-4422-abe2-2b0fddcc00f4)
