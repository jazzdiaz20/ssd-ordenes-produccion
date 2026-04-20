import pandas as pd
import pyodbc
from datetime import datetime
import yaml

def cargar_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def obtener_datos():
    config = cargar_config()
    conn = pyodbc.connect(config["database"]["connection_string"])

    query = """
    SELECT orden_id, producto, linea, estado, fecha_inicio
    FROM orden_produccion
    WHERE estado <> 'COMPLETA'
    """
    return pd.read_sql(query, conn)

def calcular_aging(df):
    df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'])
    df['aging'] = (datetime.now() - df['fecha_inicio']).dt.days
    return df
