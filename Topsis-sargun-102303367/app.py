import os

from flask import Flask, render_template, request
import re
import smtplib
from email.message import EmailMessage

# IMPORT TOPSIS FUNCTION
from topsis.topsis import topsis

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ================= EMAIL FUNCTION =================
def send_email(receiver_email, attachment_path):
    sender_email = "yourgmail@gmail.com"
    sender_password = "your_app_password"  # Gmail App Password

    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result File"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Please find attached the TOPSIS result file.")

    with open(attachment_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(attachment_path)
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

# ================= ROUTES =================
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    file = request.files["file"]
    weights = request.form["weights"]
    impacts = request.form["impacts"]
    email = request.form["email"]

    weights_list = weights.split(",")
    impacts_list = impacts.split(",")

    if len(weights_list) != len(impacts_list):
        return "Error: Number of weights must be equal to number of impacts"

    for i in impacts_list:
        if i not in ["+", "-"]:
            return "Error: Impacts must be either + or -"

    try:
        [float(w) for w in weights_list]
    except ValueError:
        return "Error: Weights must be numeric"

    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        return "Error: Invalid email format"

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(OUTPUT_FOLDER, "result_" + file.filename)
    file.save(input_path)

    topsis(input_path, weights, impacts, output_path)
    send_email(email, output_path)

    return "Result file has been sent to your email successfully!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
