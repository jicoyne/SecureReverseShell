Sometimes you get stuck with a secure environment where all the servers and end-clients are fully patched, updated and firewalled. Network firewall rules have been configured properly, and all internal clients are NATed to the Internet.


<b>main.py</b> - runs on the remote client, attempts to connect to server.py via ssh. After connection, a reverse shell is maintained.

<b>server.py</b> - accepts the incoming ssh connection and issues commands to the remote client.

<b>id_rsa</b> - use ssh-keygen to generate your own private key on the server

<b>poetry.lock</b> and <b>pyproject.toml</b> - Packager files for repl.it

<br>
<br>
<br>
<br>

<b>Copyright 2021 jicoyne@cisco.com</b>

<font size="1">Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</font>