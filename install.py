with open('.envtest', 'w') as file_dot_env:

    secrets = [
        'TWILIO_ACCOUNT_SID = ',
        'TWILIO_AUTH_TOKEN = ',
        'URL = ',
        'body_message = ',
        'from_number = +',
        'to_number = +'
        ]

    if input('If <.env> exists, it will be rewrite (y/n)? ') == 'y':

        for i in secrets:
            file_dot_env.write(f'{i}{input(i)}\n')
