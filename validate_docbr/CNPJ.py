from .BaseDoc import BaseDoc
from random import sample


class CNPJ(BaseDoc):
    """Classe referente ao Cadastro Nacional da Pessoa Jurídica (CNPJ)."""

    def __init__(self):
        self.digits = list(range(10))
        self.weights_first = list(range(5, 1, -1)) + list(range(9, 1, -1))
        self.weights_second = list(range(6, 1, -1)) + list(range(9, 1, -1))

    def validate(self, doc):
        """Validar CNPJ."""

        if len(doc) != 14:
            return False

        return self._generate_first_digit(doc) == doc[12]\
               and self._generate_second_digit(doc) == doc[13]

    def generate(self):
        """Gerar CNPJ."""
        # Os doze primeiros dígitos
        cnpj = [str(sample(self.digits, 1)[0]) for i in range(12)]

        # Gerar os dígitos verificadores
        cnpj.append(self._generate_first_digit(cnpj))
        cnpj.append(self._generate_second_digit(cnpj))

        return "".join(cnpj)

    def _generate_first_digit(self, doc):
        """Gerar o primeiro dígito verificador do CNPJ."""
        sum = 0

        for i in range(12):
            sum += int(doc[i]) * self.weights_first[i]

        sum = sum % 11

        if sum < 2:
            sum = 0
        else:
            sum = 11 - sum

        return str(sum)

    def _generate_second_digit(self, doc):
        """Gerar o segundo dígito verificador do CNPJ."""
        sum = 0

        for i in range(13):
            sum += int(doc[i]) * self.weights_second[i]

        sum = sum % 11

        if sum < 2:
            sum = 0
        else:
            sum = 11 - sum

        return str(sum)
