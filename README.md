# Validação de dados no padrão nacional

- [Algoritmo para Validar CPF](https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/)
- [PyPI](https://pypi.org/)
- [validate-docbr](https://github.com/alvarofpp/validate-docbr)

## Factory

- [Artigo 1](https://pt.wikipedia.org/wiki/Factory_Method)
- [Artigo 2](https://www.thiengo.com.br/padrao-de-projeto-factory-method)
- [Artigo 3](https://sourcemaking.com/design_patterns/factory_method)
- [Artigo 4](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html)

## Expressões Regulares (REGEX)

As expressões regulares servem para encontrar **padrões bem definidos** dentro de uma **cadeia de caracteres** em um texto ou str maiores. Por exemplo, se temos um e-mail com um volume textual enorme contendo um número de telefone específico, poderemos extraí-lo sem precisarmos ler todo o conteúdo.

- Os colchetes `[]` são caracteres especiais que definem um range ou um grupo de caracteres, como `[0-9], [a-z]` ou `[abc]` por exemplo;
- Já o * pega uma ou mais ocorrências do padrão definido anteriormente;
- As chaves `{}` nos permitem definir uma quantidade específica de vezes que queremos que o padrão se repita ou um intervalo de possibilidades, como `[abc]{5}` por exemplo;
- O `\w` pode ser qualquer número de zero a nove ou letra de `"A" a "Z"`;
- A barra `|` representa uma coisa ou outra como em `@|$` por exemplo;
- Os parênteses `()` capturam um grupo, e veremos sua importância mais adiante.
- [Python RegEx](https://www.w3schools.com/python/python_regex.asp)


## Date Time

- [Date time - doc](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
- [Introdução: Python datetime](https://blog.alura.com.br/lidando-com-datas-e-horarios-no-python/?_gl=1*18sdlk6*_ga*Nzc3MzI5MjEuMTY5NTA2NDY2Ng..*_ga_1EPWSW3PCS*MTcwMDkzNjU2OC4xNzguMS4xNzAwOTM4MzMxLjAuMC4w*_fplc*M0JKOHpoWWtmY3JGTk85TXkzNmlzMXFNbWZUYjJNSUE4eGolMkJNeGdpeGp0MENxbCUyRnY5T0ZkczlaQVhNdkZWV29NamdHMzZ5WSUyQm93N0lxSmV0ZkhmTkRENE91NVRzbDRjMXVsanF2ODRIcmpGcUVITW5ZRUIwM1ZCQkROR05BJTNEJTNE)

|Caracteres | Descrição                   | Exemplos           |
|-----------|-----------------------------|--------------------|
| `%A`	    | Dias da semana por extenso  | Sunday, Monday, ...|
| `%d`	    | Dias do mês                 | 01, 02, ..., 31    |
| `%m`	    | Meses em formato de números | 01, 02, ..., 12    |
| `%y`	    | Ano em formato de 2 dígitos | 99, 15             |
| `%Y`	    | Ano em formato de 4 dígitos | 1993, 2011         |
| `%H`	    | Hora em formato decimal     | 00, 01, ..., 23    |
| `%M`	    | Minuto em formato decimal   | 00, 01, ..., 59    |
| `%S`	    | Segundo em formato decimal  | 00, 01, ..., 59    |

## API CEP

- [Via Cep](https://viacep.com.br/)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [Como funciona uma requisição HTTP](https://medium.com/clebertech/como-funciona-uma-requisi%C3%A7%C3%A3o-http-cf76f66fe36e)
- [Python: Formatação de moeda e internacionalização](https://www.alura.com.br/artigos/formatando-moeda-no-python)