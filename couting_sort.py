def counting_sort(lista_personas):
    max_prioridad = max(persona.prioridad for persona in lista_personas)
    count = [0] * (max_prioridad + 1)
    
    for persona in lista_personas:
        count[persona.prioridad] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    output = [None] * len(lista_personas)
    
    for persona in reversed(lista_personas):
        index = count[persona.prioridad] - 1
        output[index] = persona
        count[persona.prioridad] -= 1
    
    for i in range(len(lista_personas)):
        lista_personas[i] = output[i]
    
    return lista_personas
