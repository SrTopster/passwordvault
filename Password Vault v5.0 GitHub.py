import base64
import os
import string
import random
import pyperclip
import time
import sys
import stdiomask
import webbrowser
from colorama import init,Fore
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

memes = string.ascii_letters + string.digits + string.punctuation + 'ç'
os.system('title Password Vault')
init(autoreset=True)

rd = Fore.LIGHTRED_EX
gr = Fore.LIGHTGREEN_EX
cy = Fore.LIGHTCYAN_EX

def existe():
    try:
        file = open('database.crypt')
        file.close()
    except:
        print('='*75)
        print(rd+'Database não encontrado.')
        print('O arquivo database.crypt deve estar na mesma pasta que o programa.')
        print('='*75)
        print('Digite a senha para sua database nova')
        print('Essa senha será usada para acessar sua database')
        bd = input('> ')
        f = Fernet(key(bd))
        file = open('database.crypt','wb')
        file.write(f.encrypt('DATABASE'.encode()))
        file.close()
        print('='*75)
        print(gr+'Database criada')
        print('Abra o programa denovo para usa-lo')
        print('='*75)
        print('Enter para sair')
        input()
        sys.exit()

#Retorna a Chave
def key(fkey):
    password = str(fkey).encode()
    salt = b'yoursalthere'
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,)
    return base64.urlsafe_b64encode(kdf.derive(password))

#Salva em um txt
def txt():
    file = open('database.crypt','rb')
    data = file.read()
    file.close()
    file = open('database.txt','wt')
    onetap = True
    for i in data.decode().splitlines():
        if onetap == True:
            file.write(i)
            onetap = False
        else:
            file.write('\n'+i)
    file.write('\n')
    file.write('\n==================================================')
    file.write('\nEste arquivo não é seguro/Delete-o quando terminar')
    file.write('\n==================================================')
    file.close()
    os.startfile('database.txt')

#Mostrar no programa
def mostrar():
    file = open('database.crypt','rb')
    data = file.read()
    file.close()
    for i in data.decode().splitlines():
        print(cy+i)
        print('')

#Escreve uma senha no database
def write(dados):
    file = open('database.crypt','ab')
    file.write('\n'.encode()+dados.encode())
    file.close()

#Obvio
def crypt():
    f = Fernet(key(bd))
    file = open('database.crypt','rb')
    data = file.read()
    file.close()
    file = open('database.crypt','wb')
    file.write(f.encrypt(data))
    file.close()

#Obvio 2
def decrypt():
    f = Fernet(key(bd))
    file = open('database.crypt','rb')
    data = file.read()
    file.close()
    try:
        newdata = f.decrypt(data)
        file = open('database.crypt','wb')
        file.write(newdata)
        file.close()
    except:
        print('='*50)
        print(rd+'Senha Errada')
        print('='*50)
        input('Enter para sair')
        sys.exit()

#Obvio 3
def erro():
    print(rd+'Comando Incorreto')
    input('Enter para sair')
    sys.exit()

#obvio 4
def sucesso(num):
    frases = ['Dados salvos','O arquivo database.txt foi criado','Até a proxima vez','Todas as senhas foram extraidas']
    print('='*50)
    print(gr+frases[num])
    print('='*50)
    print('')
    print(gr+'Obrigado Por Usar Password Vault by Topster_')
    print('')
    print('='*50)
    input('Enter para sair')
    sys.exit()

#verifica se o database existe
existe()

#Começo
print('='*50)
print(cy+'Bem Vindo ao Password Vault')
print('='*50)
print('1 = Acessar o Banco de Dados')
print('2 = Adicionar Senha Customizada')
print('3 = Gerar Uma Senha')
choose = input('> ')
print('='*50)
if choose == '1':
    print(cy+'Deseja')
    print('='*50)
    print('1 = Mostar No Programa (Seguro)')
    print('2 = Extrair para um .txt (Não Seguro)')
    show = input('> ')
    print('='*50)
    print('Digite a senha para o banco de dados:')
    bd = stdiomask.getpass(prompt='> ')
    print('='*50)
    if show == '1':
        decrypt()
        mostrar()
        crypt()
        sucesso(3)
    elif show == '2':
        decrypt()
        txt()
        crypt()
        sucesso(1)
    else:
        erro()
elif choose == '2':
    print('Digite a senha que deseja salvar')
    custom = input('> ')
    print('Qual o nome/user dessa senha ?')
    name = input('> ')
    print('='*50)
    print('Digite a senha para o banco de dados:')
    bd = stdiomask.getpass(prompt='> ')
    decrypt()
    write(name +' : '+custom)
    crypt()
    sucesso(0)

elif choose == '3':
    print('Qual o tamanho da senha ?')
    tam = input('> ')
    if not str(tam).isnumeric():
        erro()
    senha1 = ''.join(random.choice(memes)for i in range(int(tam)))
    print('='*50)
    print('Sua senha: '+cy+senha1)
    pyperclip.copy(senha1)
    print(gr+'Senha Copiada')
    print('='*50)
    print('Deseja salvar essa senha ? (Y/N)')
    save = input('> ')
    if str(save).lower() == 'y':
        print('Qual o nome/user dessa senha ?')
        name = input('> ')
        print('='*50)
        print('Digite a senha para o banco de dados:')
        bd = stdiomask.getpass(prompt='> ')
        decrypt()
        write(name +' : '+senha1)
        crypt()
        sucesso(0)
    else:
        sucesso(2)

elif choose == 'credits':
    #EasterEgg
    urls = ['https://www.youtube.com/watch?v=grd-K33tOSM','https://www.youtube.com/watch?v=QH2-TGUlwu4','https://www.youtube.com/watch?v=s_eHTKuCkpc','https://www.youtube.com/watch?v=XUhVCoTsBaM','https://www.youtube.com/watch?v=NUYvbT6vTPs','https://www.youtube.com/watch?v=dQw4w9WgXcQ','https://www.youtube.com/watch?v=TJL4Y3aGPuA','https://www.youtube.com/watch?v=UcRtFYAz2Yo','https://www.youtube.com/watch?v=3rzgrP7VA_Q','https://www.youtube.com/watch?v=aW0DRWhdZyY']
    webbrowser.open(random.choice(urls))
    os.system('cls')
    art = """░░░░░░░░░░░███████░░░░░░░░░░░
░░░░░░░████░░░░░░░████░░░░░░░
░░░░░██░░░░░░░░░░░░░░░██░░░░░
░░░██░░░░░░░░░░░░░░░░░░░██░░░
░░█░░░░░░░░░░░░░░░░░░░░░░░█░░
░█░░████░░░░░░░░██████░░░░░█░
█░░█░░░██░░░░░░█░░░░███░░░░░█
█░█░░░░░░█░░░░░█░░░░░░░█░░░░█
█░█████████░░░░█████████░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░████████████████████░░░░█
░█░░░█▓▓▓▓▓▓▓▓█████▓▓▓█░░░░█░
░█░░░░█▓▓▓▓▓██░░░░██▓██░░░░█░
░░█░░░░██▓▓█░░░░░░░▒██░░░░█░░
░░░██░░░░██░░░░░░▒██░░░░██░░░
░░░░░██░░░░███████░░░░██░░░░░
░░░░░░░███░░░░░░░░░███░░░░░░░
░░░░░░░░░░█████████░░░░░░░░░░
"""
    print(art)
    print('='*50)
    print('Desenvolvedor: Topster_')
    print('Beta Tester: Lion Feng')
    print('Apoio Moral: Francisbacon919')
    print('Criado em: 09/04/2021')
    print('Ultima atualização: 05/11/2021')
    print('Notas do desenvolvedor:')
    print('Um bom dia a todos os josneis')
    print('='*50)
    
    colors = ['a','b','c','d','e','f']
    while True:
        for i in colors:
            os.system('color '+i)
            time.sleep(0.1)
else:
    erro()






