def BusquedaInterpolacion(NumeroBuscar,Lista):
	PrimerDato = 0
	UltimoDato = len(Lista) - 1

	while PrimerDato <= UltimoDato and NumeroBuscar >= Lista[PrimerDato].numero_documento and NumeroBuscar <= Lista[UltimoDato].numero_documento:
		Posicion = PrimerDato + ((NumeroBuscar - Lista[PrimerDato].numero_documento)*(UltimoDato - PrimerDato))//(Lista[UltimoDato].numero_documento - Lista[PrimerDato].numero_documento)

		if Posicion < PrimerDato or Posicion > UltimoDato:
			return None

		if Lista[Posicion].numero_documento == NumeroBuscar:
			return 1
		elif Lista[Posicion].numero_documento < NumeroBuscar:
			PrimerDato = Posicion + 1
		else:
			UltimoDato = Posicion - 1
	return None