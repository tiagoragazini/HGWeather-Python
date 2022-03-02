def checar_clima_semana(detalhes_cidade):
    cidade_atual = detalhes_cidade["results"]["city"]

    data_da_semana = detalhes_cidade["results"]["forecast"][1]["date"]
    dia_da_semana = detalhes_cidade["results"]["forecast"][1]["weekday"]
    temperatura_min = detalhes_cidade["results"]["forecast"][1]["min"]
    temperatura_max = detalhes_cidade["results"]["forecast"][1]["max"]
    descricao_clima = detalhes_cidade["results"]["forecast"][1]["description"]

    print(f"Estas são as previsões climáticas para os próximos dias em {cidade_atual}")
    print(f"\nNo dia {data_da_semana} ({dia_da_semana}):")
    print(f"Situação climática: {descricao_clima}")
    print(f"Temperatura máxima: {temperatura_max}°C")
    print(f"Temperatura máxima: {temperatura_min}°C")



    data_da_semana = detalhes_cidade["results"]["forecast"][2]["date"]
    dia_da_semana = detalhes_cidade["results"]["forecast"][2]["weekday"]
    temperatura_min = detalhes_cidade["results"]["forecast"][2]["min"]
    temperatura_max = detalhes_cidade["results"]["forecast"][2]["max"]
    descricao_clima = detalhes_cidade["results"]["forecast"][2]["description"]

    print(f"\nNo dia {data_da_semana} ({dia_da_semana}):")
    print(f"Situação climática: {descricao_clima}")
    print(f"Temperatura máxima: {temperatura_max}°C")
    print(f"Temperatura máxima: {temperatura_min}°C")



    data_da_semana = detalhes_cidade["results"]["forecast"][3]["date"]
    dia_da_semana = detalhes_cidade["results"]["forecast"][3]["weekday"]
    temperatura_min = detalhes_cidade["results"]["forecast"][3]["min"]
    temperatura_max = detalhes_cidade["results"]["forecast"][3]["max"]
    descricao_clima = detalhes_cidade["results"]["forecast"][3]["description"]

    print(f"\nNo dia {data_da_semana} ({dia_da_semana}):")
    print(f"Situação climática: {descricao_clima}")
    print(f"Temperatura máxima: {temperatura_max}°C")
    print(f"Temperatura máxima: {temperatura_min}°C")



    data_da_semana = detalhes_cidade["results"]["forecast"][4]["date"]
    dia_da_semana = detalhes_cidade["results"]["forecast"][4]["weekday"]
    temperatura_min = detalhes_cidade["results"]["forecast"][4]["min"]
    temperatura_max = detalhes_cidade["results"]["forecast"][4]["max"]
    descricao_clima = detalhes_cidade["results"]["forecast"][4]["description"]

    print(f"\nNo dia {data_da_semana} ({dia_da_semana}):")
    print(f"Situação climática: {descricao_clima}")
    print(f"Temperatura máxima: {temperatura_max}°C")
    print(f"Temperatura máxima: {temperatura_min}°C")



    data_da_semana = detalhes_cidade["results"]["forecast"][5]["date"]
    dia_da_semana = detalhes_cidade["results"]["forecast"][5]["weekday"]
    temperatura_min = detalhes_cidade["results"]["forecast"][5]["min"]
    temperatura_max = detalhes_cidade["results"]["forecast"][5]["max"]
    descricao_clima = detalhes_cidade["results"]["forecast"][5]["description"]

    print(f"\nNo dia {data_da_semana} ({dia_da_semana}):")
    print(f"Situação climática: {descricao_clima}")
    print(f"Temperatura máxima: {temperatura_max}°C")
    print(f"Temperatura máxima: {temperatura_min}°C")



    data_da_semana = detalhes_cidade["results"]["forecast"][6]["date"]
    dia_da_semana = detalhes_cidade["results"]["forecast"][6]["weekday"]
    temperatura_min = detalhes_cidade["results"]["forecast"][6]["min"]
    temperatura_max = detalhes_cidade["results"]["forecast"][6]["max"]
    descricao_clima = detalhes_cidade["results"]["forecast"][6]["description"]

    print(f"\nNo dia {data_da_semana} ({dia_da_semana}):")
    print(f"Situação climática: {descricao_clima}")
    print(f"Temperatura máxima: {temperatura_max}°C")
    print(f"Temperatura máxima: {temperatura_min}°C")
