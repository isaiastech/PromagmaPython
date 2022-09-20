from recepcao.arquivos_recepcao.utilidades.criarArquivosTXT import criar_arquivo


criar_arquivo('meuprimeiroarquivo.txt')
escrever = open('meuprimeiroarquivo', "a")

print('teste2', file=escrever)
