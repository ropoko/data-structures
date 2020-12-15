import smtplib
import getpass

fromaddr = input(str('Seu email: '))
password = getpass.getpass('Senha: ')
toaddrs  = input(str('Para quem deseja enviar? '))
msg = input(str('A mensagem que deseja enviar: '))
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(fromaddr,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()