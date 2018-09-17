from threading import Thread
from flask import Flask
from flask_mail import Mail,Message

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.163.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "yunweigroup@163.com"
app.config["MAIL_PASSWORD"] = "yunwei159"

mail = Mail(app)

@app.route("/send_mail")
def send_mail():
    """
    发送邮件
    """
    message = Message("标题",sender=app.config["USERNAME"],recipients=["78845906@qq.com"])
    message.body = "内容"

    t = Thread(target=send_email,args=(message,))
    t.start()

    return "发送成功"

def send_email(msg):
    with app.app_context():
        mail.send(msg)

if __name__ == "__main__":
    app.run()