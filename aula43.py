"""
Faça um jogo para o usuário adivinhar qual 
a palavra secreta.
- Você vai propor uma palavra secreta qualquer
e vai dar a possibilidade para o usuário digitar
apenas uma letra.
- Qual o usuário digitar uma letra, você vai 
conferir se a letra digitada está na palavra
secreta.
    - Se a letra digitada estiver na 
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
    """

# Palavra secreta escolhida
palavra_secreta = "python"
# Lista para armazenar o estado atual da palavra adivinhada
estado_atual = ["_"] * len(palavra_secreta)
# Contador de tentativas
tentativas = 0

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar a palavra secreta letra por letra.")
print("Palavra:", " ".join(estado_atual))

# Loop do jogo
while "_" in estado_atual:
    letra = input("Digite uma letra: ").lower()
    
    # Incrementa o contador de tentativas
    tentativas += 1
    
    if letra in palavra_secreta:
        for indice, char in enumerate(palavra_secreta):
            if char == letra:
                estado_atual[indice] = letra
        print("Boa! A letra está na palavra.")
    else:
        print("Ops! A letra não está na palavra.")
    
    # Mostrar o estado atual da palavra
    print("Palavra:", " ".join(estado_atual))
    print("Tentativas:", tentativas)

print("\nParabéns! Você adivinhou a palavra secreta:", palavra_secreta)
print("Total de tentativas:", tentativas)