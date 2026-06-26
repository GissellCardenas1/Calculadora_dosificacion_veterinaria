def Calcular_dosis_ml():
    medicamento = input("Nombre del farmaco que vas a suministrar: ").title()
    mascota = input("Nombre de la mascota: ").title()
    peso = float(input(f"Peso de {mascota} en kg: "))
    dosis_mg_kg = float(input(f"Cual es la dosis practica o dosis indicada por el MV para {medicamento}: "))
    concentracion_medicamento = float(input(f"Cual es la concentracion de {medicamento}: "))
    
    Resultado_ml = round((peso * dosis_mg_kg) / concentracion_medicamento, 2)
    print(f"{mascota} debe recibir {Resultado_ml} ml de {medicamento}.")
    
    if Resultado_ml > 0:
        print("""
======================================================================
ADVERTENCIA LEGAL Y EXENCIÓN DE RESPONSABILIDAD
======================================================================
Este software es una herramienta de apoyo al cálculo aritmético con 
fines estrictamente educativos. La determinación de la dosis definitiva 
es responsabilidad exclusiva del Médico Veterinario tratante, quien 
debe validar los resultados con base en el estado fisiológico, 
patológico y la anamnesis del paciente.

Los cálculos obtenidos no consideran variables críticas como la 
función renal, hepática o edad del animal. Por lo tanto, el autor 
se deslinda de toda responsabilidad por efectos adversos o errores 
derivados del uso de esta información sin supervisión profesional 
calificada.

Uso sujeto a la normativa de ética profesional (Ley 576 de 2000).
=====================================================================""")
    else:
        print("ALERTA: los datos ingresados no son validos, verifique peso y dosis.")

# Para ejecutarlo en tu consola descomenta la siguiente línea:
# Calcular_dosis_ml()