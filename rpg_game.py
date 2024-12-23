import random
import time
from colorama import Fore, Style, init

# Inicializa o colorama para garantir compatibilidade em todos os sistemas
init(autoreset=True)

class Tema:
    def __init__(self, nome, descricao, cenarios, inimigos, eventos, tesouros, historia):
        self.nome = nome
        self.descricao = descricao
        self.cenarios = cenarios
        self.inimigos = inimigos
        self.eventos = eventos
        self.tesouros = tesouros
        self.historia = historia

    def gerar_cenario(self):
        return random.choice(self.cenarios)

    def gerar_evento(self):
        return random.choice(self.eventos)

    def criar_inimigo(self):
        inimigo_base = random.choice(self.inimigos)
        atributos = {
            "nome": inimigo_base,
            "forca": random.randint(10, 20),
            "vida": random.randint(30, 60),
            "habilidade": random.choice([
                "Ataque Flamejante",
                "Golpe Sombrio",
                "Encantamento Arcano",
                "Resistência Rúnica"
            ]),
        }
        return atributos

class Personagem:
    def __init__(self, nome, classe, vida, forca, habilidades):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.forca = forca
        self.habilidades = habilidades
        self.inventario = []

    def atacar(self, inimigo):
        dano = random.randint(self.forca // 2, self.forca)
        inimigo["vida"] -= dano
        return dano

    def receber_dano(self, dano):
        self.vida -= dano

    def adicionar_item(self, item):
        self.inventario.append(item)

    def mostrar_inventario(self):
        return ", ".join(self.inventario) if self.inventario else "Inventário vazio"

    def usar_habilidade(self):
        habilidade = random.choice(self.habilidades)
        print(f"{Fore.GREEN}{self.nome} usa a habilidade: {Fore.YELLOW}{habilidade}{Style.RESET_ALL}!")

class Historia:
    def __init__(self, tema, jogador):
        self.tema = tema
        self.jogador = jogador

    def iniciar_historia(self):
        print(f"\n{Fore.CYAN}Bem-vindo ao mundo de {self.tema.nome}!{Style.RESET_ALL}")
        time.sleep(2)
        print(f"{Fore.WHITE}Descrição: {self.tema.descricao}{Style.RESET_ALL}")
        time.sleep(2)
        print(f"\n{Fore.LIGHTMAGENTA_EX}{self.tema.historia}{Style.RESET_ALL}")
        time.sleep(2)
        print(f"\nSua aventura começa agora... Que os dados estejam ao seu favor!")

    def interagir(self):
        while self.jogador.vida > 0:
            cenario = self.tema.gerar_cenario()
            print(f"\n{Fore.CYAN}Você está em {cenario}. O ambiente é repleto de intriga e mistério...{Style.RESET_ALL}")

            print("\nO que deseja fazer?")
            print("1. Explorar o local")
            print("2. Avançar pelo caminho")
            print("3. Descansar")
            print("4. Ver inventário")
            escolha = input("Escolha uma opção (1-4): ")

            if escolha == "1":
                evento = self.tema.gerar_evento()
                print(f"\n{Fore.YELLOW}Explorando... {evento}{Style.RESET_ALL}")
                time.sleep(1)
                if "tesouro" in evento.lower():
                    tesouro = random.choice(self.tema.tesouros)
                    print(f"{Fore.GREEN}Você encontrou um item lendário: {Fore.RED}{tesouro}{Style.RESET_ALL}! Seu poder cresce.")
                    self.jogador.adicionar_item(tesouro)
                elif "inimigo" in evento.lower():
                    inimigo = self.tema.criar_inimigo()
                    print(f"{Fore.RED}Cuidado! Você encontrou um {inimigo['nome']}! Prepare-se para a batalha.{Style.RESET_ALL}")
                    self.combate(inimigo)
            elif escolha == "2":
                inimigo = self.tema.criar_inimigo()
                print(f"\n{Fore.RED}Um {inimigo['nome']} bloqueia seu caminho! Prepare-se para lutar.{Style.RESET_ALL}")
                self.combate(inimigo)
            elif escolha == "3":
                print("\nVocê tira um momento para descansar e recuperar suas forças.")
                time.sleep(1)
                print(f"{Fore.GREEN}Você recupera 15 pontos de vida.{Style.RESET_ALL}")
                self.jogador.vida = min(self.jogador.vida + 15, 100)
            elif escolha == "4":
                print(f"\n{Fore.BLUE}Inventário: {self.jogador.mostrar_inventario()}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Opção inválida. Tente novamente.{Style.RESET_ALL}")

            print(f"\n{Fore.YELLOW}Status: Vida {self.jogador.vida}{Style.RESET_ALL}")
            if self.jogador.vida <= 0:
                print(f"\n{Fore.RED}Você sucumbiu às forças da floresta... Fim da aventura.{Style.RESET_ALL}")

    def combate(self, inimigo):
        while inimigo["vida"] > 0 and self.jogador.vida > 0:
            print("\nEscolha sua ação:")
            print("1. Atacar")
            print("2. Usar habilidade")
            print("3. Fugir")

            escolha = input("Escolha uma opção (1-3): ")
            
            if escolha == "1":
                dano = self.jogador.atacar(inimigo)
                print(f"\n{Fore.YELLOW}Você causa {dano} de dano ao {inimigo['nome']}!{Style.RESET_ALL}")
                if inimigo["vida"] > 0:
                    dano_inimigo = random.randint(inimigo["forca"] // 2, inimigo["forca"])
                    self.jogador.receber_dano(dano_inimigo)
                    print(f"{inimigo['nome']} revida causando {dano_inimigo} de dano!")
                else:
                    print(f"\n{Fore.GREEN}{inimigo['nome']} foi derrotado! O caminho está livre.{Style.RESET_ALL}")
            elif escolha == "2":
                self.jogador.usar_habilidade()
            elif escolha == "3":
                print("\nVocê foge para salvar sua vida!")
                break
            else:
                print(f"{Fore.RED}Opção inválida. Tente novamente.{Style.RESET_ALL}")

# Definindo o tema baseado em Dungeons & Dragons

tema = Tema(
    nome="Reinos Esquecidos",
    descricao="Um mundo repleto de magia, dragões e aventuras heroicas.",
    cenarios=["um castelo em ruínas", "uma floresta sombria", "um pântano fétido", "uma cidade medieval"],
    inimigos=["Dragão Negro", "Ladrão das Sombras", "Beholder", "Mago do Caos"],
    eventos=["Você encontra um mapa do tesouro!", "Um trovão ecoa no horizonte...", "Um inimigo se esconde na escuridão!"],
    tesouros=["Espada Longa +1", "Poção de Cura", "Amuleto do Poder Arcano"],
    historia="Você é um aventureiro em busca de fama e fortuna, enfrentando perigos inimagináveis nos Reinos Esquecidos."
)

personagem = Personagem(
    nome="Elrand", 
    classe="Guerreiro", 
    vida=100, 
    forca=25, 
    habilidades=["Golpe Devastador", "Escudo Divino", "Investida Heroica"]
)

historia = Historia(tema=tema, jogador=personagem)

historia.iniciar_historia()
historia.interagir()
