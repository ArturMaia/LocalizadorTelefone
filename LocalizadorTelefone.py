import phonenumbers

# Dicionário com os códigos DDD e seus respectivos estados
ddd_estados = {
    '11': 'São Paulo', '12': 'São Paulo', '13': 'São Paulo', '14': 'São Paulo', '15': 'São Paulo',
    '16': 'São Paulo', '17': 'São Paulo', '18': 'São Paulo', '19': 'São Paulo',
    '21': 'Rio de Janeiro', '22': 'Rio de Janeiro', '24': 'Rio de Janeiro',
    '31': 'Minas Gerais', '32': 'Minas Gerais', '33': 'Minas Gerais', '34': 'Minas Gerais',
    '35': 'Minas Gerais', '37': 'Minas Gerais', '38': 'Minas Gerais',
    '41': 'Paraná', '42': 'Paraná', '43': 'Paraná', '44': 'Paraná',
    '45': 'Paraná', '46': 'Paraná',
    '51': 'Rio Grande do Sul', '53': 'Rio Grande do Sul', '54': 'Rio Grande do Sul', '55': 'Rio Grande do Sul',
    '61': 'Distrito Federal', '62': 'Goiás', '64': 'Goiás', '65': 'Mato Grosso', '66': 'Mato Grosso',
    '67': 'Mato Grosso do Sul', '68': 'Acre', '69': 'Rondônia',
    '71': 'Bahia', '73': 'Bahia', '74': 'Bahia', '75': 'Bahia', '77': 'Bahia',
    '81': 'Pernambuco', '82': 'Pernambuco', '83': 'Paraíba', '84': 'Rio Grande do Norte',
    '85': 'Ceará', '86': 'Piauí', '87': 'Pernambuco', '88': 'Ceará', '89': 'Piauí',
    '91': 'Pará', '92': 'Amazonas', '93': 'Pará', '94': 'Pará', '95': 'Espírito Santo',
    '96': 'Santa Catarina', '97': 'Amapá', '98': 'Maranhão', '99': 'Maranhão'
}

cod = 55  # Código do Brasil
estado = input("Digite o código DDD do estado: ")
contato = input("Digite o número de telefone: ")

# Verifica código DDD
estado_nome = ddd_estados.get(estado, "DDD não encontrado")

if estado_nome == "DDD não encontrado":
    print("Código DDD inválido.")
else:
    numero_completo = f'+{cod}{estado}{contato}'

    # Verificar se o número é válido
    if phonenumbers.is_valid_number(phonenumbers.parse(numero_completo)):
        # Exibir o resultado
        print("Este número é de:")
        print(f'Estado - {estado_nome}, País - Brasil.')
    else:
        print("Número de telefone inválido. Verifique o formato.")

