import html
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from string import Template

from config import EMAIL, PASSWORD, SMTP_SERVER, SMTP_PORT


def send_email(receiver_email, name, topic, resource_url, html_template):
    template = Template(html_template)

    html_body = template.substitute(
        name=html.escape(name),
        topic=html.escape(topic),
        resource_url=html.escape(resource_url, quote=True),
    )

    message = EmailMessage()
    message["Subject"] = f"Your {topic} learning resource"
    message["From"] = formataddr(
        ("Sabir's Learning Project", EMAIL)
    )
    message["To"] = receiver_email

    message.set_content(
        f"Hello {name},\n\n"
        f"Here is a learning resource for {topic}:\n"
        f"{resource_url}\n\n"
        "Keep learning, one step at a time.\n\n"
        "Best regards,\n"
        "Sabir's Learning Project"
    )

    message.add_alternative(html_body, subtype="html")

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(EMAIL, PASSWORD)
        server.send_message(message)