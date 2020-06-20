#Spentalkux

##300 points - First solved by clubby789

Spentalkux 🐍📦

##Steps
Since `Spentalkux` is not a term to me i just googled it and found a **python package** (which would explain the emojis behind the word)

As of the [pypi.org website](https://pypi.org/project/spentalkux/) it dosent seems to be a usable package.
`I dare you to import this`

In the release history there are two versions called `0.9` and `13.37` which is the current version.

Lets download both, gunzip them, tar them and have a look.

###13.37
Inside the files we can find a python string which gets executet after encoded..

```
aW1wb3J0IHRpbWUKCmdvX2F3YXlfbXNncyA9IFsiR29vZGJ5ZSBub3cuIiwgIlRoYXQncyB5b3VyIGN1ZSB0byBsZWF2ZSwgYnJvIiwgIkV4aXQgc3RhZ2UgbGVmdCwgcGFsIiwgIk9GRiBZT1UgUE9QLiIsICJZb3Uga25vdyB3aGF0IEkgaGF2ZW4ndCBnb3QgdGltZSBmb3IgdGhpcyIsICJGb3JraW5nIGFuZCBleGVjdXRpbmcgcm0gLXJmLiJdCgp0aW1lLnNsZWVwKDEpCnByaW50KCJIZWxsby4iKQp0aW1lLnNsZWVwKDIpCnByaW50KCJDYW4gSSBoZWxwIHlvdT8iKQp0aW1lLnNsZWVwKDIpCnByaW50KCJPaCwgeW91J3JlIGxvb2tpbmcgZm9yIHNvbWV0aGluZyB0byBkbyB3aXRoICp0aGF0Ki4iKQp0aW1lLnNsZWVwKDIpCnByaW50KCJNeSBjcmVhdG9yIGxlZnQgdGhpcyBiZWhpbmQgYnV0LCBJIHdvbmRlciB3aGF0IHRoZSBrZXkgaXM/IEkgZG9uJ3Qga25vdywgYnV0IGlmIEkgZGlkIEkgd291bGQgc2F5IGl0J3MgYWJvdXQgMTAgY2hhcmFjdGVycy4iKQp0aW1lLnNsZWVwKDQpCnByaW50KCJFbmpveSB0aGlzLiIpCnRpbWUuc2xlZXAoMSkKcHJpbnQoIlp0cHloLCBJcSBpaXInanQgdnJ0ZHR4YSBxenh3IGxodSdnbyBneGZwa3J3IHR6IHBja3YgYmMgeWJ0ZXZ5Li4uICpmZmlpZXlhbm8qLiBOZXcgY2lrbSBzZWthYiBndSB4dXggY3NrZml3Y2tyIGJzIHpmeW8gc2kgbGdtcGQ6Ly96dXBsdGZ2Zy5jencvbHhvL1FHdk0wc2E2IikKdGltZS5zbGVlcCg1KQpmb3IgaSBpbiBnb19hd2F5X21zZ3M6CiAgICB0aW1lLnNsZWVwKDMpCiAgICBwcmludChpKQp0aW1lLnNsZWVwKDAuNSk=
```

lets use [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=YVcxd2IzSjBJSFJwYldVS0NtZHZYMkYzWVhsZmJYTm5jeUE5SUZzaVIyOXZaR0o1WlNCdWIzY3VJaXdnSWxSb1lYUW5jeUI1YjNWeUlHTjFaU0IwYnlCc1pXRjJaU3dnWW5Kdklpd2dJa1Y0YVhRZ2MzUmhaMlVnYkdWbWRDd2djR0ZzSWl3Z0lrOUdSaUJaVDFVZ1VFOVFMaUlzSUNKWmIzVWdhMjV2ZHlCM2FHRjBJRWtnYUdGMlpXNG5kQ0JuYjNRZ2RHbHRaU0JtYjNJZ2RHaHBjeUlzSUNKR2IzSnJhVzVuSUdGdVpDQmxlR1ZqZFhScGJtY2djbTBnTFhKbUxpSmRDZ3AwYVcxbExuTnNaV1Z3S0RFcENuQnlhVzUwS0NKSVpXeHNieTRpS1FwMGFXMWxMbk5zWldWd0tESXBDbkJ5YVc1MEtDSkRZVzRnU1NCb1pXeHdJSGx2ZFQ4aUtRcDBhVzFsTG5Oc1pXVndLRElwQ25CeWFXNTBLQ0pQYUN3Z2VXOTFKM0psSUd4dmIydHBibWNnWm05eUlITnZiV1YwYUdsdVp5QjBieUJrYnlCM2FYUm9JQ3AwYUdGMEtpNGlLUXAwYVcxbExuTnNaV1Z3S0RJcENuQnlhVzUwS0NKTmVTQmpjbVZoZEc5eUlHeGxablFnZEdocGN5QmlaV2hwYm1RZ1luVjBMQ0JKSUhkdmJtUmxjaUIzYUdGMElIUm9aU0JyWlhrZ2FYTS9JRWtnWkc5dUozUWdhMjV2ZHl3Z1luVjBJR2xtSUVrZ1pHbGtJRWtnZDI5MWJHUWdjMkY1SUdsMEozTWdZV0p2ZFhRZ01UQWdZMmhoY21GamRHVnljeTRpS1FwMGFXMWxMbk5zWldWd0tEUXBDbkJ5YVc1MEtDSkZibXB2ZVNCMGFHbHpMaUlwQ25ScGJXVXVjMnhsWlhBb01Ta0tjSEpwYm5Rb0lscDBjSGxvTENCSmNTQnBhWEluYW5RZ2RuSjBaSFI0WVNCeGVuaDNJR3hvZFNkbmJ5Qm5lR1p3YTNKM0lIUjZJSEJqYTNZZ1ltTWdlV0owWlhaNUxpNHVJQ3BtWm1scFpYbGhibThxTGlCT1pYY2dZMmxyYlNCelpXdGhZaUJuZFNCNGRYZ2dZM05yWm1sM1kydHlJR0p6SUhwbWVXOGdjMmtnYkdkdGNHUTZMeTk2ZFhCc2RHWjJaeTVqZW5jdmJIaHZMMUZIZGswd2MyRTJJaWtLZEdsdFpTNXpiR1ZsY0NnMUtRcG1iM0lnYVNCcGJpQm5iMTloZDJGNVgyMXpaM002Q2lBZ0lDQjBhVzFsTG5Oc1pXVndLRE1wQ2lBZ0lDQndjbWx1ZENocEtRcDBhVzFsTG5Oc1pXVndLREF1TlNrPQ) and we get:

```
import time

go_away_msgs = ["Goodbye now.", "That's your cue to leave, bro", "Exit stage left, pal", "OFF YOU POP.", "You know what I haven't got time for this", "Forking and executing rm -rf."]

time.sleep(1)
print("Hello.")
time.sleep(2)
print("Can I help you?")
time.sleep(2)
print("Oh, you're looking for something to do with *that*.")
time.sleep(2)
print("My creator left this behind but, I wonder what the key is? I don't know, but if I did I would say it's about 10 characters.")
time.sleep(4)
print("Enjoy this.")
time.sleep(1)
print("Ztpyh, Iq iir'jt vrtdtxa qzxw lhu'go gxfpkrw tz pckv bc ybtevy... *ffiieyano*. New cikm sekab gu xux cskfiwckr bs zfyo si lgmpd://zupltfvg.czw/lxo/QGvM0sa6")
time.sleep(5)
for i in go_away_msgs:
    time.sleep(3)
    print(i)
time.sleep(0.5)
```
The intersting part is `Ztpyh, Iq iir'jt vrtdtxa qzxw lhu'go gxfpkrw tz pckv bc ybtevy... *ffiieyano*. New cikm sekab gu xux cskfiwckr bs zfyo si lgmpd://zupltfvg.czw/lxo/QGvM0sa6`

Lets indentify this cypher.
Its a **Vigenere Cipher** lets encode it with [this vigenere-solver](https://www.guballa.de/vigenere-solver):

`Hello, If you're reading this you've managed to find my little... *interface*. The next stage of the challenge is over at https://pastebin.com/raw/BCiT0sp6`

The pastebin link contains a huge hex. 
After downloading it we can convert it to an image with `xxd -r -p BCiT0sp6 image.png`

The image shows text on a red background which we can get with `tesseract image.png text`

```
look back into the past...

find what you have forgotten...

01011111 01101000 01100101 01110010 01110010 01101001 01101110 01100111
```

The binary encodes to `_herring`... Given the background color is red its a **red_herring**.

as stated above we need to look into the `past`.

##0.9
Lets go again!
Again its a base64 string

```
import time

go_away_msgs = ["This is the part where you *leave*, bro.", "Look, if you don't get outta here soon ima run rm -rf on ya", "I don't want you here. GO AWAY.", "Leave me alone now.", "GOODBYE!", "I used to want you dead but...", "now I only want you gone."]

time.sleep(1)
print("Urgh. Not you again.")
time.sleep(2)
print("Fine. I'll tell you more.")
time.sleep(2)
print("...")
time.sleep(2)
print("But, being the chaotic evil I am, I'm not giving it to you in plaintext.")
time.sleep(4)
print("Enjoy this.")
time.sleep(1)
print("JA2HGSKBJI4DSZ2WGRAS6KZRLJKVEYKFJFAWSOCTNNTFCKZRF5HTGZRXJV2EKQTGJVTXUOLSIMXWI2KYNVEUCNLIKN5HK3RTJBHGIQTCM5RHIVSQGJ3C6MRLJRXXOTJYGM3XORSIJN4FUYTNIU4XAULGONGE6YLJJRAUYODLOZEWWNCNIJWWCMJXOVTEQULCJFFEGWDPK5HFUWSLI5IFOQRVKFWGU5SYJF2VQT3NNUYFGZ2MNF4EU5ZYJBJEGOCUMJWXUN3YGVSUS43QPFYGCWSIKNLWE2RYMNAWQZDKNRUTEV2VNNJDC43WGJSFU3LXLBUFU3CENZEWGQ3MGBDXS4SGLA3GMS3LIJCUEVCCONYSWOLVLEZEKY3VM4ZFEZRQPB2GCSTMJZSFSSTVPBVFAOLLMNSDCTCPK4XWMUKYORRDC43EGNTFGVCHLBDFI6BTKVVGMR2GPA3HKSSHNJSUSQKBIE")
time.sleep(5)
for i in go_away_msgs:
    time.sleep(2)
    print(i)
time.sleep(0.5)
```

To encrypt the string this time we use [CyberChef](https://gchq.github.io/CyberChef/) again.
With the `magic` module we can get the following recipe: `from base32 -> from base64 -> gunzip -> from binary -> from binary -> from hex`

Which results into:

```
Ea`I"Ap[6t20:Wp0ed`-?SQG?1NI(a@l$>t
```

Once more decode it with Base85 and we get the flag!

##Flag
ractf{My5t3r10u5_1nt3rf4c3?}