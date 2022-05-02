texto = ''
while(texto != 'salir'):
    texto = input('>')
    texto = texto.replace(':)', '😀')
    texto = texto.replace(':D', '😃')
    texto = texto.replace(':(', '😔')
    texto = texto.replace(':*', '😘')
    texto = texto.replace(':/', '🤔')
    texto = texto.replace(':p', '😋')
    print(texto)

