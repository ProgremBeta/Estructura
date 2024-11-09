def BusquedaBinaria(NumeroBuscar, Lista):
	PrimerDato = 1
	UltimoDato = len(Lista)-1

	while PrimerDato <= UltimoDato:
		Mitad = (PrimerDato + UltimoDato)//2
		if Lista[Mitad].numero_documento == NumeroBuscar:
			return Lista[Mitad]
		elif NumeroBuscar < Lista[Mitad].numero_documento:
				UltimoDato = Mitad - 1
		else:
			PrimerDato = Mitad + 1
	return None