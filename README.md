<p align="center">
  <img src="https://github.com/ArturMaia/LocalizadorTelefone/blob/main/Telefonema.jpeg" alt="tel" style="width: 200px; border-radius: 10px;">
</p>

# Geolocalizador de Telefone Brasileiro

## Descrição

Este projeto, desenvolvido em **Python**, tem como objetivo validar números de telefone brasileiros e identificar a localização geográfica com base no código DDD fornecido. Ao inserir o DDD e o número de telefone, o programa informa o estado correspondente e valida a autenticidade do número. Isso pode ser útil para identificar rapidamente a origem de um número de telefone no Brasil.

## Linguagem Utilizada

- **Python**: Linguagem de programação utilizada para desenvolver o projeto.

## Bibliotecas Usadas

- **phonenumbers**: Para validar e formatar números de telefone.

## Como Usar

1. O programa solicita o código DDD do estado.
2. Em seguida, ele pede o número de telefone.
3. O programa valida o número e informa o estado e o país (Brasil), associando o DDD à sua localização geográfica.
4. Caso o número ou DDD seja inválido, uma mensagem de erro será exibida.

### Exemplo:

```
Digite o código DDD do estado: 91
Digite o número de telefone: 912345678
Este número é de:
Estado - Pará, País - Brasil.
```

Se o número for inválido:

```
Digite o código DDD do estado: 91
Digite o número de telefone: 91234567
Número de telefone inválido. Verifique o formato.
```

## Contribuições

Fique à vontade para contribuir! Faça um fork, adicione suas melhorias e envie um pull request.
