import paramiko
import os

server = '172.16.5.202'
username = 'test4'
password = '1111'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server, username=username, password=password)

ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('df -h')

msg = ssh_stdout.read().decode('euc-kr')
print('stdout : ', msg)

# ssh.close()