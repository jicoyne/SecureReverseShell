Sometimes you get stuck with a secure environment where all the servers and end-clients are fully patched, updated and firewalled. Network firewall rules have been configured properly, and all internal clients are NATed to the Internet.
<br>
<br>

<b>main.py</b> - runs on the remote client, attempts to connect to server.py via ssh. After connection, a reverse shell is maintained.

<b>server.py</b> - accepts the incoming ssh connection and issues commands to the remote client.

<b>id_rsa</b> - use ssh-keygen to generate your own private key on the server

<b>poetry.lock</b> and <b>pyproject.toml</b> - Packager files for repl.it

<br>
<br>
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
apicid		: 2
initial apicid	: 2
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes

/>> cat /proc/meminfo

MemTotal:       26694668 kB
MemFree:        19898648 kB
MemAvailable:   23455560 kB
Buffers:          315700 kB
Cached:          2850172 kB
SwapCached:            0 kB
Active:          3122832 kB
Inactive:        1996740 kB
Active(anon):    1570556 kB
Inactive(anon):     2620 kB
Active(file):    1552276 kB
Inactive(file):  1994120 kB
Unevictable:       47420 kB
Mlocked:           47420 kB
SwapTotal:             0 kB
SwapFree:              0 kB
Dirty:               800 kB
Writeback:             0 kB
AnonPages:       2001056 kB
Mapped:           467124 kB
Shmem:             10520 kB
KReclaimable:     427948 kB
Slab:            1170044 kB
SReclaimable:     427948 kB
SUnreclaim:       742096 kB
KernelStack:      307552 kB
PageTables:        34192 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:    13347332 kB
Committed_AS:   32252560 kB
VmallocTotal:   34359738367 kB
VmallocUsed:      320072 kB
VmallocChunk:          0 kB
Percpu:            13808 kB
HardwareCorru

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


<font size="-1">Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</font>
