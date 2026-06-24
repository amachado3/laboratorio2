from cryptography.fernet import Fernet
chave = Fernet.generate_key()
with open("Q4/GillesLibert/chave.key", "wb") as f:
    f.write(chave)

print("Chave gerada e gravada em chave.key")
