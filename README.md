

<b>main.py</b> - runs on the remote client, attempts to connect to server.py via ssh. After connection, a reverse shell is maintained.

<b>server.py</b> - accepts the incoming ssh connection and issues commands to the remote client.

<b>id_rsa</b> - use ssh-keygen to generate your own private key on the server

<b>poetry.lock</b> and <b>pyproject.toml</b> - Packager files

<br>
<br>
/>>reset

Listening for connection...

Command Shell Open



/>>ls /usr/sbin | grep user

adduser
deluser
newusers
useradd
userdel
usermod

/>>python -V

Python 3.8.2

/>>curl ifconfig.me

35.223.251.99

/>> lscpu

neIntel

cpu family	: 6

model		: 63

model name	: Intel(R) Xeon(R) CPU @ 2.30GHz

stepping	: 0

microcode	: 0x1

cpu MHz		: 2299.998

cache size	: 46080 KB

physical id	: 0

siblings	: 4

core id		: 1

cpu cores	: 2

/>> cat /proc/meminfo

MemTotal:       26694668 kB

MemFree:        19898648 kB

MemAvailable:   23455560 kB

Buffers:          315700 kB
