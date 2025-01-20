import re

def is_valid_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    if len(cpf) != 11:
        return False
    
    # Validação simples: CPF não pode ser uma sequência de números repetidos
    if cpf == cpf[0] * 11:
        return False

    # Algoritmo de validação do CPF
    def calculate_digit(cpf, factor):
        total = sum(int(cpf[i]) * factor[i] for i in range(len(factor)))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    # Fatores para calcular os dois dígitos
    factor_first = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    factor_second = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    # Calculando os dois dígitos verificadores
    first_digit = calculate_digit(cpf, factor_first)
    second_digit = calculate_digit(cpf, factor_second)

    return cpf[-2:] == f"{first_digit}{second_digit}"

def main(req):
    # Obtém o CPF da solicitação
    cpf = req.params.get('cpf')
    if not cpf:
        return func.HttpResponse("CPF não fornecido", status_code=400)
    
    # Validação do CPF
    if is_valid_cpf(cpf):
        return func.HttpResponse("CPF Válido", status_code=200)
    else:
        return func.HttpResponse("CPF Inválido", status_code=400)
