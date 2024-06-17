import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    """
    Gera uma senha segura baseada nos critérios definidos pelo usuário.
    
    :param length: Comprimento da senha
    :param use_uppercase: Incluir letras maiúsculas
    :param use_numbers: Incluir números
    :param use_special: Incluir caracteres especiais
    :return: Senha gerada
    """
    
    if length < 1:
        raise ValueError("O comprimento da senha deve ser pelo menos 1")
    
    # Caracteres básicos
    characters = list(string.ascii_lowercase)
    
    # Adiciona caracteres adicionais conforme os critérios do usuário
    if use_uppercase:
        characters.extend(string.ascii_uppercase)
    if use_numbers:
        characters.extend(string.digits)
    if use_special:
        characters.extend(string.punctuation)
    
    # Garante que a senha gerada contenha pelo menos um caractere de cada tipo solicitado
    password = []
    
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    
    # Preenche o restante da senha
    while len(password) < length:
        password.append(random.choice(characters))
    
    # Embaralha os caracteres para evitar padrões previsíveis
    random.shuffle(password)
    
    return ''.join(password[:length])

if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Senhas Seguras!")

    try:
        length = int(input("Digite o comprimento da senha desejada: "))
        use_uppercase = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'
        use_numbers = input("Incluir números? (s/n): ").strip().lower() == 's'
        use_special = input("Incluir caracteres especiais? (s/n): ").strip().lower() == 's'

        password = generate_password(length, use_uppercase, use_numbers, use_special)
        print(f"Sua senha gerada é: {password}")
    except ValueError as e:
        print(f"Erro: {e}")