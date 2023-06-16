from random import randrange

nome = ["Abel", "Abelarda", "Abelardo",
        "Baloo", "Babalu", "Bambi", "Baby",
        "Capitu", "Caco", "Calvin",
        "Da Vinci", "Dalila", "Dark", "Duck",
        "Ed", "Eddie", "Elvis", "Emma",
        "Falcão", "Fred", "Fanta",
        "Gaia", "Gigi", "Gretha", "Gloomer",
        "Hadija", "Half", "Halley", "Hooper",
        "Ice", "Iky", "Indiana", "Iago",
        "Jack", "Jade", "James", "Java",
        "Kaká", "Kate", "Kauã", "Kacau",
        "Lady", "Lana", "Lola", "Lee", "Lilica",
        ]

animais = ["CACHORO", "GATO", "COELHO", "PORQUINHO DA INDIA"]
status_posivel = ["sujo", "doente"]


class Animal:
    def __init__(self):
        self.nome = self.define_nome()
        self.especie = self.define_especie()
        self.status = self.define_status()

    def __str__(self):
        return f"Nome: {self.nome} | Especie: {animais[self.especie]} | Status: {status_posivel[self.status]}"


    # define se o animal esta doente ou esta sujo
    def define_status(self):
        sujo = [i for i in range(1, 71)]
        doente = [i for i in range(70, 101)]
        valor = randrange(1, 101)
        
        if (valor in sujo):
            return 0

        elif (valor in doente):
            return 1
        

    # define a especie do animal
    def define_especie(self):
        valor = randrange(0, 3)
        return valor

    # define o nome do animal 
    def define_nome(self):
        valor = randrange(len(nome))
        return nome[valor]
