# --->    Python 2.7    <--- #


import datetime,os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
from email.Utils import COMMASPACE, formatdate

#funcao para envio do email
def envia_email(servidor, porta, FROM, PASS, TO, subject, texto, anexo=[]):
  global saida
  servidor = servidor
  porta = porta
  FROM = FROM
  PASS = PASS
  TO = TO
  subject = subject
  texto = texto
  msg = MIMEMultipart()
  msg['From'] = FROM
  msg['To'] = TO
  msg['Subject'] = subject
  msg.attach(MIMEText(texto))

# Anexa os arquivos
  for f in anexo:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(f, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment;filename="%s"'% os.path.basename(f))
    msg.attach(part)

  try:
    gm = smtplib.SMTP(servidor,porta)
    gm.ehlo()
    gm.starttls()
    gm.ehlo()
    gm.login(FROM, PASS)
    gm.sendmail(FROM, TO, msg.as_string())
    gm.close()

  except Exception == e:
    errorMsg = ("Nao Foi Possivel Enviar o Email.\n Error: {}".format(str(e)))
    print (errorMsg)

print("\n")
print("{:^80}".format("AGUARDE, NAO FECHE ESTA JANELA!!!"))
print("")
print("{:^70}".format("               .-.-.-._."))
print("{:^70}".format("                .~\ /~\_/ \_."))
print("{:^70}".format("              .~\_/~\_/ \_/~\_."))
print("{:^70}".format("               .~\_/ \_/ \_/ \_/~\."))
print("{:^70}".format("   .----.      /\_/ \_/ \_/ \_/ \_/\."))
print("{:^70}".format("   /(o)(o)`\__ /_/ \_/ \_/ \_/ \_/ \_\."))
print("{:^70}".format("  |           \_/ \_/ \_/ \_/ \_/ \\. \."))
print("{:^70}".format("        \ \__/      |\_/ \_/ \_/ \_/ \_/ \_/~\...'"))
print("{:^70}".format("           `----´`----\/_\-/-\_/-\-/ \_/-\_.-/''''"))
print("{:^70}".format("              /~/===| |=====| |==\~\ "))
print("{:^70}".format("            _/ /   _| |    _| |   \ \ "))
print("{:^70}".format("           (___|  (___|   (___|  (___|"))
print("\n\n")
print("{:^80}".format("ENVIANDO E-MAIL DA LISTAGEM DAS MATRICULAS RECADASTRADAS "))
print("{:^80}".format("E ACESSOS PARA seuemail@gmail.com!!!"))


# data_hora contem data e hora atual filtrada para remover os milesimos e
# espacos substituidos por '_'
data_hora = datetime.datetime.now()
data_hora = str(data_hora).split('.')[0].replace(' ','_')

#O email para o qual sera enviado o arquivo
#destinatario
destinatario = 'seuemail@gmail.com'

#Assunto do email
assunto = 'Backup do arquivo tal referente a %s' %data_hora

#mensagem do corpo do email
mensagem = 'Segue em anexo o backup do(s) aquivos: acessos.txt e controle.ods, referente ao dia %s'%data_hora

#neste caso estou usando o gmail, mas pode ser qualquer outro email,
#inclusive o email da empresa que vc trabalha, por exemplo,
#contanto que seja especificado o endereco do servidor smtp e a porta

#Endereco do servidor smtp do gmail
servidor= 'smtp.gmail.com'

#porta smtp do gmail
porta = 587

#email e senha do remetente. Neste caso, do gmail
#lembrando que os dados referem-se a um email e
#senha ficticios, ou seja, substitua pelos seus
#dados de acesso
remetente = 'seuemail@gmail.com'
senha = 'suasenha'

#"/tmp/teste.txt" e "/tmp/teste1.txt" sao os arquivos que serao
# anexados ao email
#chamada a funcao de envio do email
envia_email(servidor, porta, remetente, senha, destinatario, assunto, mensagem, ["G:/Gerador Seq/Gerenciador de Sequencias - Base Real/acessos.txt", "G:/Gerador Seq/Gerenciador de Sequencias - Base Real/controle.ods"])
