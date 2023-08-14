#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def conta_palavras_unicas(frase):
    # Converte a string para minúsculas e divide em palavras
    palavras = frase.lower().split()

    # Cria um conjunto vazio para armazenar palavras únicas
    palavras_unicas = set()

    # Itera sobre as palavras e adiciona ao conjunto de palavras únicas
    for palavra in palavras:
        # Remove possíveis pontuações no final das palavras
        palavra = palavra.strip(".,!?")
        palavras_unicas.add(palavra)

    # Retorna a quantidade de palavras únicas contabilizadas
    return len(palavras_unicas)









# Teste a sua função aqui (caso ache necessário)

# Teste da função
frase = "Esta é uma frase de teste. Teste de contagem de palavras únicas."
quantidade_palavras_unicas = conta_palavras_unicas(frase)
print(f"A quantidade de palavras únicas na frase é: {quantidade_palavras_unicas}")









