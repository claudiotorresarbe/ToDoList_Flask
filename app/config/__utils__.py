
def generate_random_password(length=12):
    
    # Biblioteca
    import secrets
    import string

    # Expressão
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for i in range(length))

    return password

def validar_email(email):
    
    # Biblioteca
    import re
    
    #expressão
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    result = bool(re.match(pattern, email)) and ".." not in email
    
    return result
