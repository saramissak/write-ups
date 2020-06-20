# CLIsay
## 20 Points

cowsay is hiding something from us!

Download the file below.

## Steps

Lets download the file and see what it is with `file clisay`
```
clisay: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=70e60678f1c0b75ea3aae2a4e8e1e8978e3c6fc0, for GNU/Linux 3.2.0, not stripped
```

With this information we can know proceed and simply excecute it to see what happens (kinda a safty issue but i was curious)

```
  __________________________________
/ Sorry, I'm not allow to reveal any \
\ secrets...                         /
  ----------------------------------
         \   ^__^ 
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||


```

well lets dig deeper. Lets check the binary for useful strings with `strings clisay` and voilá:

```
[]A\A]A^A_
flag{Y0u_c4n_
  __________________________________
/ Sorry, I'm not allow to reveal any \
\ secrets...                         /
  ----------------------------------
         \   ^__^ 
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
r3Ad_M1nd5}
:*3$"

```

## Flag
flag{Y0u_c4n_r3Ad_M1nd5}
