# Ponderada 3, módulo 8

Esta ponderada tem como objetivo a criação de um chatbot simples em Python baseado em regex, com um dicionário de intenções e um de ações. Isso deve ser feito como um nó de ROS2.

## Instalação

1. Clone este repositório em seu ambiente ROS 2:

    ```bash
    git clone https://github.com/seu_usuario/seu_repositorio.git
    ```

2. Navegue até o diretório do repositório:

    ```bash
    cd sm3p8
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

Isso é tudo! Agora, o nó ROS 2 deve estar em execução.

## Demo

<video width="320" height="240" controls>
  <source src="https://github.com/elisaflemer/m8p3/blob/main/demo.webm" type="video/webm">
</video>