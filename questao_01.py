class Televisao:
    def __init__(self, marca, tamanho):
        self.ligada = False
        self.canal = 2
        self.marca = marca
        self.tamanho = tamanho
    def muda_canal_para_baixo(self):
        self.canal -= 1
    def muda_canal_para_cima(self):
        self.canal += 1

tv = Televisao('LGTV', '52 polegadas')
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_baixo()
print(tv.canal)
print('Televisão 1: Marca:', tv.marca,', tamanho:', tv.tamanho)

tv2 = Televisao('TCL', '46 polegadas')
print('Televisão 1: Marca:', tv2.marca,', tamanho:', tv2.tamanho)