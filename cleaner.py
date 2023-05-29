import os

for field in os.listdir(os.getcwd()+'\css'):
    print(field)
    try:
        with open(os.getcwd()+os.sep+'css'+os.sep+field,'r') as doc:
            cadena = str(doc.read())

            cadena = cadena.split('}')
            print('\n} \n\n'.join(cadena))


            doc.close()
    except:
        print('Error de lectura')

