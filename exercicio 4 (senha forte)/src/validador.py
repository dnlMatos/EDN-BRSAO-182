def senha_forte(senha: str) -> bool:
    if len(senha) < 8:
        return False
    return any(char.isdigit() for char in senha)
