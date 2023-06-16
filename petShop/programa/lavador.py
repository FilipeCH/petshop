class lavador:
    def __init__(self):
        
        
        self.quntidade_de_lavador = int(1)
        self.lavador_disponivel = int(1)
        
    def __str__(self):
        return (f"lavador disponivel: {self.lavador_disponivel}")


    # faz a checagem para ver se a lavador disponivel caso tenha o animal e mandadoo para o banho caso não o clinte tem de esperar
    # ou ir em bora
    def checa_lavador_disponivel(self):
        if(self.lavador_disponivel > 0):
            print("O animal foi enviado para o lavador!")
            self.lavador_disponivel -= 1
            return True
        else:
            print("Não a lavadores disponivel")
            return False
        

