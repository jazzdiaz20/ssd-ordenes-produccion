from procesamiento import obtener_datos, calcular_aging
from clasificacion import clasificar_riesgos
from notificaciones import enviar_alerta

def main():
    df = obtener_datos()
    df = calcular_aging(df)
    df = clasificar_riesgos(df)

    alertas = df[df['riesgo'] == 'ALTO']
    enviar_alerta(alertas)

if __name__ == "__main__":
    main()
