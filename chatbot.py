#! /bin/env python3
import re


def greet_back():
    print(f"Olá, eu sou o Vallet, o robô inteligente da cervejaria do futuro!")


def genki_back():
    print("Comigo está tudo bem, e com você?")


def bye():
    return "Tchau, até mais!"
    exit()


def go_to():
    for key, value in destinos.items():
        pattern = re.compile(key)
        groups = pattern.findall(command)
        if groups:
            print(f"OK, indo para {value}, em {coordenadas[value]}")
            return
    print("Não sei onde fica esse lugar")

intent_dict = {
    r"\b(?:[Oo][Ii]|ol[áa]|o[láa]|oii|oie)\b|\b(?:(?:[Bb]o[am])\s(tarde|dia|noite))": "greetings",
    r"\b(?:[Tt]udo)?\s?(?:(?:[bB]em)|(?:[bB]ão)|(?:[fF]irme)|(?:em\sriba))\?": "genki",
    r"\b(?:[Tt]chau|[Aa]deus|[Ff]ui|[Ss]air|[Ee]ncerrar|[Pp]arar|[Dd]esligar|[Ff]inalizar|[Ee]ncerrar|[Ee]ncerar|[Ee]ncerr)": "bye",
    r"\b(ir para|me leve até)\s+(\w+)": "go_to",
}

action_dict = {
    "greetings": greet_back,
    "genki": genki_back,
    "bye": bye,
    "go_to": go_to,
}

destinos = {
    r"\b(s?e?s?k?o?l)\b": "skol",
    r"br[aa]?mm?a|brahma": "brahma",
    r"ze|zé|zé delivery|delivery": "ze delivery",
    r"b[ea]ts?|bats|beets|bites|beates|bates|betes|beats": "beats",
    r"almo?x(?:erif(?:ado)?|arif(?:e|ado)?|cherif(?:ado|edo)?)": "almoxarifado",
}

coordenadas = {
    "almoxarifado": {"x": 0.0, "y": 0.0, "z": 0.0},
    "beats": {"x": 1.26, "y": 0.0, "z": 0.0},
    "brahma": {"x": 1.22, "y": -1.55, "z": 0.0},
    "ze delivery": {"x": 0.62, "y": -0.81, "z": 0.0},
    "skol": {"x": 0.0, "y": -1.55, "z": 0.0},
}

while True:
    command = input("Digite o seu comando: ")
    for key, value in intent_dict.items():
        pattern = re.compile(key)
        groups = pattern.findall(command)
        if groups:
            action_dict[value]()
            break
    else:
        print("Não entendi o que você quis dizer")

    print()
