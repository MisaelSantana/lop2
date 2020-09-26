from pasta_classes.loja import Cliente
from pasta_classes.loja import Produto
from pasta_classes.loja import Encomenda
from pasta_classes.loja import relatorio

cliente1 = Cliente('Misael Santana', '0478840-1086', 'R. Dilson Funaro, Ulysses Guimarães, Joinville, 89230648', '111.222.333-44')
print(cliente1.verificarCpf())

produto1 = Produto('Mesa', 'Mesa de centro', '20cm', '35cm', '35cm', '5kg', 'Verniz', 100.00)
print(produto1.verificarPreco())

encomenda1 = Encomenda(2)
relatorio(cliente1, produto1, encomenda1)