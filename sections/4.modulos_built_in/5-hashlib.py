import hashlib

print(hashlib.algorithms_available)

print(hashlib.algorithms_guaranteed)

algorithm = hashlib.sha256()
print(algorithm.digest())
message = "A melhor forma de prever o futuro é cria-lo".encode()
algorithm.update(message)
print(algorithm.hexdigest())

md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())