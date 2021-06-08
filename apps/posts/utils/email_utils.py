from django.core.mail import EmailMessage


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
        email.send()

    def send_recovery_password_email(self):
        pass