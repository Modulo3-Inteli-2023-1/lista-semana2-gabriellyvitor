import exercicio1
import exercicio2


# test para conta_palavras_unicas
def test_conta_palavras_unicas():
    assert exercicio1.conta_palavras_unicas("banana") == 1
    assert exercicio1.conta_palavras_unicas("banana maçã") == 2
    assert exercicio1.conta_palavras_unicas("banana maçã maçã") == 2
    assert exercicio1.conta_palavras_unicas("banana maçã maçã maçã maçã maçã maçã maçã maçã maçã maçã maçã maçã maçã") == 2

# função test para is_anagram
def test_is_anagram():
    assert exercicio2.is_anagram("banana", "banana") == True
    assert exercicio2.is_anagram("banana", "maçã") == False
    assert exercicio2.is_anagram("amor", "roma") == True
    assert exercicio2.is_anagram("pedra", "padre") == True
    assert exercicio2.is_anagram("pedra", "pedro") == False
    assert exercicio2.is_anagram("perda", "pedra") == True
    assert exercicio2.is_anagram("perda", "pedro") == False
    assert exercicio2.is_anagram("perda", "padre") == True