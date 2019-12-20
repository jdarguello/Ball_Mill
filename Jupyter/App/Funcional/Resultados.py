def Ress(res):
    resultados = {
        'Resultados': {
            'Volumen [m3]': round(res['Vol']['V'],3),
            'Diámetro [m]': round(res['D'],3),
            'Longitud [m]': round(res['L'],3),
            'Velocidad de rotación [rpm]': round(res['N'],3),
            'Potencia [hp]': round(res['Pot'],3)
        }
    }
    return resultados