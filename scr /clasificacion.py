def clasificar_riesgos(df):
    def clasificar(row):
        if row['aging'] >= 5 and row['linea'] in ['L1', 'L2']:
            return 'ALTO'
        elif row['aging'] >= 3:
            return 'MEDIO'
        return 'BAJO'

    df['riesgo'] = df.apply(clasificar, axis=1)
    return df
