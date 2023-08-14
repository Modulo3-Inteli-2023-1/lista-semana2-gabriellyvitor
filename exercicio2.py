#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def is_anagram(str1, str2):
    # Remove espaços em branco e converte as strings para minúsculas
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Verifica se os comprimentos das strings são iguais
    if len(str1) != len(str2):
        return False

    # Cria dicionários para armazenar a contagem de caracteres em cada string
    char_count1 = {}
    char_count2 = {}

    # Conta a ocorrência de cada caractere na primeira string
    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1

    # Conta a ocorrência de cada caractere na segunda string
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1

    # Compara os dicionários de contagem
    return char_count1 == char_count2

# Teste da função
string1 = "listen"
string2 = "silent"
resultado = is_anagram(string1, string2)
if resultado:
    print(f"'{string1}' e '{string2}' são anagramas.")
else:
    print(f"'{string1}' e '{string2}' não são anagramas.")






# Teste a sua função aqui (caso ache necessário)











