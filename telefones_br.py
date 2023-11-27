import re


class TelefonesBr:

    def __init__(self, telefone):
        self.__padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"

        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto!")

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        resposta = re.findall(self.__padrao, telefone)

        return resposta

    def format_numero(self):
        resposta = re.search(self.__padrao, self.numero)

        if resposta:
            numero_formatado = (
                f"+{resposta.group(1)} ({resposta.group(2)})"
                f"{resposta.group(3)}-{resposta.group(4)}"
            )
            return numero_formatado
        else:
            raise ValueError("Número incorreto ou não formatável")
