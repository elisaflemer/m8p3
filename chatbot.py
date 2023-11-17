#!/usr/bin/env python3
import re
import rclpy
from rclpy.node import Node

class ValletNode(Node):
    def __init__(self):
        super().__init__('vallet_node')
        
        self.destinos = {
            r"\b(s?e?s?k?o?l)\b": "skol",
            r"br[aa]?mm?a|brahma": "brahma",
            r"ze|zé|zé delivery|delivery": "ze delivery",
            r"b[ea]ts?|bats|beets|bites|beates|bates|betes|beats": "beats",
            r"almo?x(?:erif(?:ado)?|arif(?:e|ado)?|cherif(?:ado|edo)?)": "almoxarifado",
        }

        self.coordenadas = {
            "almoxarifado": {"x": 0.0, "y": 0.0, "z": 0.0},
            "beats": {"x": 1.26, "y": 0.0, "z": 0.0},
            "brahma": {"x": 1.22, "y": -1.55, "z": 0.0},
            "ze delivery": {"x": 0.62, "y": -0.81, "z": 0.0},
            "skol": {"x": 0.0, "y": -1.55, "z": 0.0},
        }

        self.intent_dict = {
            r"\b(?:[Oo][Ii]|ol[áa]|o[láa]|oii|oie)\b|\b(?:(?:[Bb]o[am])\s(tarde|dia|noite))": "greetings",
            r"\b(?:[Tt]udo)?\s?(?:(?:[bB]em)|(?:[bB]ão)|(?:[fF]irme)|(?:em\sriba))\?": "genki",
            r"\b(?:[Tt]chau|[Aa]deus|[Ff]ui|[Ss]air|[Ee]ncerrar|[Pp]arar|[Dd]esligar|[Ff]inalizar|[Ee]ncerrar|[Ee]ncerar|[Ee]ncerr)": "bye",
            r"\b(ir para|me leve até|vai para|vai pra|vamos pra)\s+(\w+)": "go_to",
        }

        self.action_dict = {
            "greetings": self.greet_back,
            "genki": self.genki_back,
            "bye": self.bye,
            "go_to": self.go_to,
        }

        self.get_logger().info("Vallet ROS 2 Node has been initialized.")

    def greet_back(self):
        self.get_logger().info("Olá, eu sou o Vallet, o robô inteligente da cervejaria do futuro!")

    def genki_back(self):
        self.get_logger().info("Comigo está tudo bem!")

    def bye(self):
        self.get_logger().info("Tchau, até mais!")
        rclpy.shutdown()
        exit()

    def go_to(self):
        command = input("Digite o seu comando: ")
        for key, value in self.destinos.items():
            pattern = re.compile(key)
            groups = pattern.findall(command)
            if groups:
                self.get_logger().info(f"OK, indo para {value}, em {self.coordenadas[value]}")
                return
        self.get_logger().info("Não sei onde fica esse lugar")

    def run(self):
        while rclpy.ok():
            command = input("Digite o seu comando: ")
            for key, value in self.intent_dict.items():
                pattern = re.compile(key)
                groups = pattern.findall(command)
                if groups:
                    self.action_dict[value]()
                    break
            else:
                self.get_logger().info("Não entendi o que você quis dizer")

            print()

def main():
    rclpy.init()
    vallet_node = ValletNode()
    vallet_node.run()
    rclpy.spin(vallet_node)
    vallet_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
