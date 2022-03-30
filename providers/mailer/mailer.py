import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from configPy import JSONConfigParser

from providers.mailer.content import CONTENT_FACTORY
from providers.mailer.standards.return_codes import RETURN_CODES

# Import Server Configurations
configObject = JSONConfigParser(configFilePath="server-config.json")
__mailer_server_configs = configObject.getConfigurations()

port = __mailer_server_configs['port']
serverAddress = __mailer_server_configs['mail-server']
sender = __mailer_server_configs['sender']
password = __mailer_server_configs['password']

# Import Mail Templates Configurations
configObject = JSONConfigParser(configFilePath=".configs/mailer.config.json")
tempates_config = configObject.getConfigurations()


class MAILER:

    def __init__(self, mailer_mode) -> None:
        self.mailer_mode = mailer_mode

    def prepare_mail(self, payload) -> None:
        content = self.mailer_mode

        if self.mailer_mode == CONTENT_FACTORY.VERIFIED_MAIL:
            content["replacement_string"] = payload
            html_mail_template_file = tempates_config["verified-mail-template-file"]
        elif self.mailer_mode == CONTENT_FACTORY.OTP_MAIL:
            content["replacement_string"] = payload
            html_mail_template_file = tempates_config["otp-genertation-template-file"]

        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = content["subject"]
        self.message["From"] = sender

        self.template = open(html_mail_template_file).read().replace(
            content["replacement_token"],
            content["replacement_string"]
        )

        self.mail_body = MIMEText(self.template, "html")
        self.message.attach(self.mail_body)

    def send_mail(self, recipient):
        self.message["To"] = recipient
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(serverAddress, port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, self.message.as_string())

        return RETURN_CODES.MLS01

