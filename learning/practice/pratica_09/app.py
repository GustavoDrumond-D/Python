from models.carro import ModelCarro
from models.moto import ModelMoto

carro_prisma = ModelCarro('chevrolet', 'prisma', 4)
carro_gol = ModelCarro('volkswagen', 'gol', 4)
carro_saveiro = ModelCarro('fiat', 'saveiro', 5)

moto_XRE_190 = ModelMoto('Honda', 'XRE 190', 'sport')
moto_XRE_200 = ModelMoto('Honda', 'XRE 200', 'sport')
moto_XRE_300 = ModelMoto('Honda', 'XRE 300', 'sport')

print(carro_prisma)
print(carro_gol)
print(carro_saveiro)
print(moto_XRE_190)
print(moto_XRE_200)
print(moto_XRE_300)