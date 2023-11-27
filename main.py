from documento import Documento
from telefones_br import TelefonesBr
from email_validated import EmailValidated
from datas_br import DatasBr
from busca_endereco import BuscaEndereco


documentos = {
    "cpf": Documento.cria_documento("15316264754"),
    "cnpj": Documento.cria_documento("35379838000112"),
    "telefone": TelefonesBr("552126481234"),
    "e-mail": EmailValidated("aaabbbcc evandro123@gmail.com.br ccbbbaaa"),
    "datas": {
        "data do cadastro": DatasBr().format_data(),
        "dia da semana": DatasBr().dia_semana(),
        "calculado": DatasBr().tempo_cadastro()
    },
    "CEP": BuscaEndereco("03922160").acessa_via_cep()
}

for key, value in documentos.items():
    print(f"{'':-^50}")  # > direita, < esquerda, ^ ambos
    print(f"{key}: {value}", end="\n")
