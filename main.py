import requests


def program():
    inicio_busca()


def inicio_busca():
    print("-"*23)
    print("--- Buscador de CEP ---")
    print("-"*23)

    try:
        cep = int(input("\nDigite um cep: "))
    except ValueError:
        print('\nO CEP digitado é inválido. Digite um CEP válido.')
        inicio_busca()
    except:
        print('ERRO...')
        raise
    else:
        busca_cep(cep)


def busca_cep(cep):
    response = requests.get(f'https://brasilapi.com.br/api/cep/v2/{cep}')
    result = response.json()

    # breakpoint
    # __import__('pdb').set_trace()

    if response.status_code != 200:
        print(f'O cep {cep} não é válido.')
        inicio_busca()
    else:
        imprime_dados(result)


def imprime_dados(result):
    rua = result['street']
    cidade = result['city']
    estado = result['state']

    print(rua)
    print(f'Cidade {cidade}')
    print(f'Estado {estado}')


if __name__ == '__main__':
    program()
