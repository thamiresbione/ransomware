import os 
import pyaes

 ## abrir o arquivo que está criptografado
 file_name = "teste.txt.trollransom"
 file = open(file_name, 'rb')
 file_data = file.read()
 file.close ()
 
  ## chave de descriptar
  
  key = b 'testeransomware'
  aes = pyaes.AESModeOfOperationCTR(key)
  decrypt)data = aes.decrypt(file_data)
  
  ## remover arquivo cript
  os.remove(file_name)
  
  ## criar um novo arquivo descriptografado
  new_file = 'test.txt'
  new_file = open(f'{new_file}', 'wb')
  new_file.write.(decrypt_data)
  new_file.close()
