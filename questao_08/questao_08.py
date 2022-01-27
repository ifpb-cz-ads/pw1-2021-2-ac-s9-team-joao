from estados import Estado
from cidades import Cidade

ce = Estado("Ceará", "CE")
ce.adiciona_cidade(Cidade("Brejo Santo", 49842))
ce.adiciona_cidade(Cidade("Juazeiro do Norte", 276264))

pb = Estado("Paraíba", "PB")
pb.adiciona_cidade(Cidade("Cajazeiras", 62576))
pb.adiciona_cidade(Cidade("Campina Grande", 402912))

pe = Estado("Pernambuco", "PE")
pe.adiciona_cidade(Cidade("Recife", 1661017))
pe.adiciona_cidade(Cidade("Olinda", 393115))

for estado in [ce, pb, pe]:
    print(f"Estado: {estado.nome} Sigla: {estado.sigla}")
    for cidade in estado.cidades:
        print(f"Cidade: {cidade.nome} População: {cidade.população}")
    print(f"População do Estado: {estado.população()}\n")

