import smtplib
from email.mime.text import MIMEText
import yaml

def cargar_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def enviar_alerta(df):
    if df.empty:
        return

    config = cargar_config()

    mensaje = "Órdenes críticas:\n\n"
    for _, row in df.iterrows():
        mensaje += f"Orden: {row['orden_id']} | Aging: {row['aging']} | Línea: {row['linea']}\n"

    msg = MIMEText(mensaje)
    msg['Subject'] = 'ALERTA: Órdenes en riesgo ALTO'
    msg['From'] = config["email"]["user"]
    msg['To'] = config["email"]["to"]

    with smtplib.SMTP(config["email"]["smtp"], config["email"]["port"]) as server:
        server.starttls()
        server.login(config["email"]["user"], config["email"]["password"])
        server.send_message(msg)
