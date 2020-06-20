# Quarantine - Hidden information

## 150 points - First solved by teknoas

Challenge instance ready at `88.198.219.20:30807`.

We think there's a file they don't want people to see hidden somewhere! See if you can find it, it's gotta be on their webapp somewhere...

## Steps

Lets get nmap going and see what we get.
`nmap -sC -sV -p 30807 88.198.219.20`

**Well look at that:**
```
Starting Nmap 7.60 ( https://nmap.org ) at 2020-06-10 09:27 CEST
Nmap scan report for static.88.198.219.20.clients.your-server.de (88.198.219.20)
Host is up (0.027s latency).

PORT      STATE SERVICE VERSION
30807/tcp open  http    Werkzeug httpd 1.0.1 (Python 3.8.3)
| http-robots.txt: 1 disallowed entry 
|_/admin-stash
|_http-title: Really Awesome Quarantine Entertainment

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.39 seconds
```
Seems there is a hidden dir called `/admin-stash`

## Flag
ractf{1m_n0t_4_r0b0T}
