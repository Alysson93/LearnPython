from Escritor import Escritor
from Ferramenta import Ferramenta

escritor = Escritor('Alysson')
f = Ferramenta('Caneta')
escritor.ferramenta = f
print(escritor.ferramenta.escrever())