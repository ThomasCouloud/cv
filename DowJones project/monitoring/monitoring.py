import pandas as pd
import matplotlib.pyplot as plt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import sys
import logging
from encryption_utils import load_key, decrypt_data

logging.basicConfig(
    filename="monitoring.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

base_dir = os.path.dirname(os.path.dirname(__file__))
chemin_fichier_log = os.path.join(
    os.path.dirname(__file__), "encrypted_credentials.dat"
)

with open(chemin_fichier_log, "r") as log_file:
    log_content = log_file.read()
    logging.info(log_content)

path_to_api = os.path.join(base_dir, "api")
path_to_csv = os.path.join(base_dir, "mse_records.csv")


graph_directory = os.path.join(os.path.dirname(__file__), "graph")

key = load_key()
with open("encrypted_credentials.dat", "rb") as file:
    encrypted_data = file.read()

decrypted_data = decrypt_data(encrypted_data, key)
credentials = {}
for line in decrypted_data.split("\n"):
    k, value = line.split("=")
    credentials[k] = value

EMAIL_USER = credentials.get("EMAIL_USER")
EMAIL_PASS = credentials.get("EMAIL_PASS")


def check_model_performance():
    try:
        plt.figure(figsize=(12, 12))
        df = pd.read_csv(path_to_csv, names=["DateTime", "Symbol", "ID", "MSE"])
        most_recent_mse = df["MSE"].iloc[-1]

        plt.plot(df["DateTime"], df["MSE"])
        plt.title("Evolution de la performance du modèle")
        plt.xlabel("Date")
        plt.ylabel("MSE")

        THRESHOLD = 0.01
        if most_recent_mse > THRESHOLD:
            above_threshold_indices = df[df["MSE"] > THRESHOLD].index.tolist()

            largest_gap = max(
                [
                    (b - a)
                    for a, b in zip(
                        above_threshold_indices[:-1], above_threshold_indices[1:]
                    )
                ]
            )
            center_idx = above_threshold_indices[
                above_threshold_indices.index(largest_gap // 2)
            ]

            start_idx = max(0, center_idx - 50)
            end_idx = min(len(df), center_idx + 50)

            plt.xlim(df["DateTime"].iloc[start_idx], df["DateTime"].iloc[end_idx])

            graph_filename = "performance_graph_zoomed.png"
            graph_path = os.path.join(graph_directory, graph_filename)
            plt.xticks(rotation=45)
            plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
            plt.savefig(graph_path)

            send_email(graph_path)

            print("Performance du modèle en dessous du seuil - email envoyé")
            logging.warning("Performance du modèle en dessous du seuil")
        else:
            logging.info("Performance du modèle acceptable")

    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")


def send_email(graph_path):
    recipients = [
        "thomascouloud@hotmail.fr",
        "sebastien.moitel@gmail.com",
        "richard.bonfils.data@gmail.com",
    ]

    email_send = ", ".join(recipients)
    subject = "Alerte Performance Modèle"
    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER

    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject
    body = "La performance du modèle est en dessous du seuil attendu. Voir le graphique en pièce jointe pour plus de détails."
    msg.attach(MIMEText(body, "plain"))

    with open(graph_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition", "attachment; filename=performance_graph.png"
        )
        msg.attach(part)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)
    server.sendmail(EMAIL_USER, email_send, msg.as_string())
    server.quit()


if __name__ == "__main__":
    check_model_performance()
