import requests
import json
import semana

print("Busque saber as condições climáticas de sua cidade com uma pesquisa rápida!")

key_token = "e12fcc07"

def checar_cidade_cliente():
    estado_cliente = input(str("Digite a sigla do estado que deseja buscar(EX.: SP, RJ): "))
    if len(estado_cliente) != 2:
        print("Não foi possível localizar!")
        checar_cidade_cliente()
    else:
        cidade_cliente = input(str("Digite a cidade que deseja pesquisar: "))
        request_api(estado_cliente, cidade_cliente)

def request_api(estado_cliente, cidade_cliente):
    url = "https://api.hgbrasil.com/weather?key="+ key_token +"&city_name="+ cidade_cliente +","+ estado_cliente
    resposta_url = requests.get(url)
    detalhes_cidade = json.loads(resposta_url.text)


    clima_hoje(detalhes_cidade)
    clima_semana(detalhes_cidade)

def clima_hoje(detalhes_cidade):
    temperatura_atual = detalhes_cidade["results"]["temp"]
    data_atual = detalhes_cidade["results"]["date"]
    hora_atual = detalhes_cidade["results"]["time"]
    cidade_atual = detalhes_cidade["results"]["city"]
    humidade_ar = detalhes_cidade["results"]["humidity"]
    velocidade_vento = detalhes_cidade["results"]["wind_speedy"]
    descricao_clima = detalhes_cidade["results"]["forecast"][0]["description"]

    print(f"Estas são as as condições climáticas de hoje({data_atual}) em {cidade_atual} às {hora_atual}:\n")
    print(f"Temperatura: {temperatura_atual}ºC")
    print(f"Situação climática: {descricao_clima}")
    print(f"Umidade do ar: {humidade_ar}%")
    print(f"Velocidade do vento: {velocidade_vento}\n\n")


def clima_semana(detalhes_cidade):
    print("Gostaria de checar a previsão do tempo para os próximos dias? Digite 1!")
    print("Ou digite qualquer outro número se desejar sair da aplicação.")
    escolha = int(input("Sua escolha: "))
    if escolha == 1:
        semana.checar_clima_semana(detalhes_cidade)
    else:
        print("Obrigado por testar minha aplicação! :)")
        quit()

if __name__ == '__main__':
    checar_cidade_cliente()
