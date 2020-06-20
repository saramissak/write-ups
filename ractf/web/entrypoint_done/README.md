# Entrypoint

## 200 points - First solved by kaovd

Challenge instance ready at `88.198.219.20:10322`.

Sadly it looks like there wasn't much to see in the python source. We suspect we may be able to login to the site using backup credentials, but we're not sure where they might be. Encase the password you find in **ractf{...}** to get the flag.

*This challenge does NOT have fake flags. If you found some other flags while solving this challenge, you may have found the solutions to the next challenges first :P*

## Steps
Ok lets open the given IP in our webbrowser.

First of **view the source**!
In the source code we find following comment:
```
<!--
    In case I forget: Backup password is at ./backup.txt
-->
```

So lets check `/backup.txt` and we are getting a `403 - Forbidden`.

We know what we need and now we just need to get it.
The system should have acess so lets just see how can get the system to give us the contents.

In the source code we can see how some files are provided:
```
<link rel="stylesheet" href="/static?f=index.css">
```

So lets check `/static?f=backup.txt` and boom we get:
```
develop    developerBackupCode4321

Make sure to log out after using!

TODO: Setup a new password manager for this
```

## Flag
ractf{developerBackupCode4321}
