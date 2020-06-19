#fsociety
##500 Points

Chall Link : `http://web.zh3r0.ml:8005/`
I hate this society.

**Author : Cryptonic007,Finch**

*Automated tools allowed.*

##Steps

ok so looking at the site dosent really show much. There is a gif and nothing else.

In the `robots.txt` file we can find that there is a `elliot.html` file. Lets check this out.

The `alt` tag of the gif says `check my js` so lets do this and we get:

```
(![]+[])[+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(+[![]]+[+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+!+[]]+[+[]]+[+[]]+[+[]])])[+!+[]+[+[]]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[+[]]
```

excecuting it we get `fsocietyislit`.
A bit of googleing reveals its `JSFuck`

lets see what else we can find with dirb:
`dirb http://web.zh3r0.ml:8005/ -z 100 -t -o dirb
`
*Note: -z 100 is used to get a ms timeout between tryes. Since the server respondet with 503 everytime*

ok `dirb` found a directory (`code`) and inside that we have a file `flag.php`

This file says: `
Elliot need to submit hash here to get the flag.
`

if we send a negativ hash we get `Dont try to mess with fsociety`

Dont seem to find anything useful so lets try to get them what they want.

If we send them the JSFuck keyword `fsocietyislit` hashed as md5 we get the flag!

##Flag
zh3r0{ell1ot_y0u_4r3_1n}