
def counting_sort(personas):
    max_documento = max(persona.numero_documento for persona in personas)
    min_documento = min(persona.numero_documento for persona in personas)
    rango = max_documento - min_documento + 1
    count = [0] * rango
    output = [None] * len(personas)
    
    for persona in personas:
        count[persona.numero_documento - min_documento] += 1
        
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for persona in reversed(personas):
        index = count[persona.numero_documento - min_documento] - 1
        output[index] = persona
        count[persona.numero_documento - min_documento] -= 1

    return output
