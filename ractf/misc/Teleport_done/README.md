# Teleport

## 300 points - First solved by RGBsec3

Challenge instance ready at 88.198.219.20:54778.

One of our admins plays a strange game which can be accessed over TCP. He's been playing for a while but can't get the flag! See if you can help him out.

`teleport.py - 831 Bytes`


### Steps

connect to ip:
`nc 88.198.219.20 58829`

ape.py connect to ip and run script to reach destination

**Well that failed!**

lets look at the code.
```
    new_x = float(move[0])
    new_z = float(move[1])
    ...

    if dist > 10:
        print("You moved too far")
    else:
        x = new_x
        z = new_z
    if x == 10000000000000 and z == 10000000000000:
        print("ractf{#####################}")
        break

```

So what we input is parsed into a float number which is then checked if its less then 10.
If its not the we get a "You moved too far" otherwise our input will be set as the new `x` and `y`.
These two variables are then checked if they reachd their destination of 10000000000000.

One thing about the `float()` function is that you cann either pass a valid number but also `nan` and `inf` which are not exactly floats.

`Inf` will always be larger then 10 so the check would fail.. but `nan` isnt. 
Lets try out:

**connect to ip:**
`netcat 88.198.219.20 54778`

**response:**
`Current position: nan, nan`

well seems like it works. Sadly `nan != 10000000000000` so lets set the new float to the destination.

And it worked!!

## Flag
ractf{fl0at1ng_p01nt_15_h4rd}
