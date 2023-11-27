import requests


class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)

        if self.valida(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.formata()

    def valida(self, cep):
        return len(cep) == 8

    def formata(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()

        return (
            dados["bairro"],
            dados["localidade"],
            dados["uf"]
        )
