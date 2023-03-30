from Produto import Produto
from Carrinho import Carrinho

carrinho = Carrinho()
p1 = Produto('Caneta', 1.25)
p2 = Produto('Bolsa', 100)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()