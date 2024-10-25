def manutencao(*args, **kwargs):
    ##Variavel para configuração de carreta e valors possiveis das variaveis
    #2 EIXOS
    #3 EIXOS
    #BI TREM 7 EIXOS
    #VARDERLEIA  
    #4 EIXOS (3+1)
    #BI TREM 9 EIXOS
    #RODOTREM / TRITREM
    config = int(Element("config").value)

    ##Variavel para distancia percorrida
    #A ser digitada pelo usuario
    distance = int(Element("distance").value)

    #variavel para tipo de eixo (4x2,6x2,6x4)
    axle = int(Element("axle").value)

    ##variavel para condição da estrada
    #Regular
    #Irregular
    road_condition = int(Element("road_condition").value)

    ##variavel para tipo de topografia
    #Predominantemente plana
    #Acidentada
    #Muito acidentada
    topography = int(Element("topography").value)

    ##variavel para tipo de trafego
    #Rodovia expressa
    #Rodovia intensa
    #Extra urbano expresso
    #Extra urbano intenso
    #Urbano / Fora de estrada expresso
    condition_traffic = int(Element("condition_traffic").value)

    ##Variavel tipo de transporte
    #50%
    #100%
    transport = int(Element("transport").value)

    ##variavel para condições ambientais
    #Sim
    #Não
    #Extremo
    environment = Element("environment").value

    ##variavel para condições ambientais
    #Sim
    #Não
    utilization = Element("utilization").value


    #Tratadando os fatos de por faixa de quilometragem

    if distance > 80000:
        distance_treted = 9
    elif distance > 80000 and distance < 40000:
        distance_treted = 27
    elif distance > 20000 and distance < 40000:
        distance_treted = 45
    else:
        distance_treted = 72




    #realizando o somatorios dos fatores obtidos no frond-end
    values_to_sum = (config,distance_treted,axle,road_condition,topography,condition_traffic,transport)
    total = sum(values_to_sum)




    #Especificando o tipo de manutenção conforme regras

    if distance_treted == 72:
        tipo_plano = "Plano de manutenção recomendado: HORAS revisões a cada 500Km \n"
    elif total > 0 and total <= 160 and axle == "6x2":
        tipo_plano = "Plano de manutenção recomendado: Leve com Revisões a cada 60.000Km \n"
    elif total > 160 and total <= 290 and axle == "6x2":
        tipo_plano = "Plano de manutenção recomendado: Padrão com Revisões a cada 45.000Km \n"
    elif total > 290 and total <= 580 and axle == "6x2"
        tipo_plano = "Plano de manutenção recomendado: Severo com Revisões a cada 30.000Km \n"
    elif total > 0 and total <= 160 and axle == "6x4":
        tipo_plano = "Plano de manutenção recomendado: Leve com Revisões a cada 45.000Km \n"
    elif total > 160 and total <= 290 and axle == "6x4":
        tipo_plano = "Plano de manutenção recomendado: Padrão com Revisões a cada 30.000Km \n"
    elif total > 290 and total <= 580 and axle == "6x4"
        tipo_plano = "Plano de manutenção recomendado: Severo com Revisões a cada 20.000Km \n"
    elif total > 580:
        tipo_plano = "Plano de manutenção recomendado: Muito Severo com Revisões a cada 20.000Km \n"
    else:
        tipo_plano = "Condição de uso não parametrizada, por favor, procure seu representante IVECO \n"

    if environment == "Sim":
        tipo_filtro = "recomendado troca do filtro de ar em todas as revisões." 
    elif environment == "Extremo":
        tipo_filtro = "recomendado utilização do filtro de ar para aplicações especiais."
    else:
        tipo_filtro = ""


    result = Element("output")
    result.write(tipo_plano + "\n" + tipo_filtro)
