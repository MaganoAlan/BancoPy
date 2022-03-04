from models.cliente import Cliente
from models.conta import Conta


alan: Cliente = Cliente('Alan Magano', 'maganoalan@gmail.com', '022.472.050-38', '24/08/1989')
fran: Cliente = Cliente('Franciane Magano', 'francianemagano@gmail.com', '022.480.910-52', '16/05/1992')

# print(alan)
# print(fran)

contaa: Conta = Conta(alan)
contaf: Conta = Conta(fran)

# print(contaa)
# print(contaf)

