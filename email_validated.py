import re

padrao = (
    r"\w{2,50}@"     # Nome de usuário (2 a 50 caracteres)
    r"\w{2,15}\."    # Nome do domínio (2 a 15 caracteres) seguido por um ponto

    # Extensão do domínio (2 a 3 caracteres) seguida por um ponto opcional
    r"[a-z]{2,3}\.?"
    r"([a-z]{2,3})?"  # Subdomínio opcional (2 a 3 caracteres)
)


class EmailValidated:

    def __init__(self, texto):
        self.__texto = self.valida(texto)

    def __str__(self):
        return f"e-mail: {self.__texto}"

    def valida(self, email):
        result = re.search(padrao, email)

        return result.group() if result else "Nenhum e-mail encontrado!"
