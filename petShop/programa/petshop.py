import lavador
animais_aceitos = ["CACHORO", "GATO", "COELHO", "PORQUINHO DA INDIA"]

class PetShop:
    def __init__(self):
        self.dinheiro = float(0)
        self.quntidade_de_funcinarios = int(1)
        self.quntidade_de_lavadores = int(1)
        self.quntidade_de_clinica = int(1)
        self.quntidade_animais = int(0)
        self.lavador = lavador.lavador()


    def __str__(self):
        return (f"""Relatorio:
Dinheiro: {self.dinheiro}
Quntidade de Funcionarios: {self.quntidade_de_funcinarios}
Quntidade de lavadores: {self.quntidade_de_lavadores}"""
                )
    
    def receber_animal(self, animal):
        resposta = 0
        # checagem para ver se o animal esta na lista de animais aceitos caso o animal e encaminhado para a area que ele nesecita
        if(str(animal).upper() in animais_aceitos):
            self.quntidade_animais += 1

            if (resposta == 1):
                self.lavador.checa_lavador_disponivel()
            
            elif(resposta == 2):
                # enviar para o veterinario
                pass

        # caso não esteja na lista o cliente e liberado 
        else:
            print(f"Não podemos tratar o seu {animal}")
