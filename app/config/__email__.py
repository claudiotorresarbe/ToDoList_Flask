from themail import *
import threading

def prepareEmail(receiver,subject,body):
    email = Themail()
    send = email.send(receiver,subject,body)
    return send

def enviarEmail(receiver,subject,body):
    thread = threading.Thread(target=prepareEmail, args=(receiver, subject, body))
    thread.start()
    return 'ok'
    
def activeAccount(receiver,token):
    subject = 'Ative sua conta!'
    body = f'''<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ativação de Conta</title>
</head>
<body>
  <div style="max-width: 600px; margin: 0 auto; padding: 20px; font-family: Arial, sans-serif;">
    <h2 style="text-align: center; color: #333;">Ativação de Conta</h2>
    <p>Olá,</p>
    <p>Seu cadastro foi realizado com sucesso! Para começar a aproveitar os nossos serviços, por favor, ative a sua conta clicando no botão abaixo:</p>
    <div style="text-align: center; margin-top: 20px;">
      <a href="http://localhost:3000/active?token={token}" style="display: inline-block; padding: 10px 20px; background-color: #007bff; color: #fff; text-decoration: none; border-radius: 5px;">Ativar Conta</a>
    </div>
    <p style="text-align: center; margin-top: 20px; font-size: 14px;">Se o botão acima não funcionar, você também pode copiar e colar o seguinte link no seu navegador: <br><strong>http://localhost:3000/active?token={token}</strong></p>
    <p style="margin-top: 30px;">Atenciosamente,<br>Sua Equipe</p>
  </div>
</body>
</html>
    '''
    return enviarEmail(receiver,subject,body)

def updatePassword(receiver,newPassword):
    subject = 'Nova senha gerada!'
    body = f'''<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nova Senha de Acesso</title>
</head>
<body>
  <div style="max-width: 600px; margin: 0 auto; padding: 20px; font-family: Arial, sans-serif;">
    <h2 style="text-align: center; color: #333;">Recuperação de Senha</h2>
    <p>Olá,</p>
    <p>Você solicitou uma nova senha para acessar a sua conta. Abaixo está a sua nova senha:</p>
    <div style="text-align: center; margin-top: 20px;">
      <p style="font-size: 24px; font-weight: bold;">{newPassword}</p>
    </div>
    <p style="margin-top: 20px;">Por favor, faça o login utilizando a nova senha e, em seguida, altere-a para uma senha segura e memorável.</p>
    <p style="margin-top: 30px;">Se você não solicitou essa alteração ou se tiver qualquer dúvida, entre em contato conosco imediatamente.</p>
    <p style="margin-top: 30px;">Atenciosamente,<br>Sua Equipe</p>
  </div>
</body>
</html>
    '''
    return enviarEmail(receiver,subject,body)
