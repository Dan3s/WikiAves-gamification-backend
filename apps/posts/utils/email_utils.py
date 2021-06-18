from django.core.mail import EmailMessage

import threading


class EmailThread(threading.Thread):  # Mejora la velocidad del envío de emails

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class EmailUtils(object):

    def send_notification_email(self, destination_email, trigger_username, contribution_value=None):
        body = ''
        if contribution_value is not None:
            if contribution_value:
                body = 'El usuario ' + trigger_username + ' está de acuerdo con la información de tu ' \
                                                          'avistamiento '
            else:
                body = 'El usuario ' + trigger_username + ' está en desacuerdo con la información de ' \
                                                          'tu avistamiento. Tranquilo, puede no ser ' \
                                                          'un experto ;) '
        else:
            body = 'Al usuario ' + trigger_username + ' le ha gustado tu avistamiento'

        email = EmailMessage(subject='¡Han interactuado con tu avistamiento!', body=body, to=destination_email)
        EmailThread(email).start()

    def send_email(self, data):
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        EmailThread(email).start()
