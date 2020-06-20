# C0llide?

## 250 points - First solved by insertish

Challenge instance ready at `88.198.219.20:42019`.

A target service is asking for two bits of information that have the same "custom hash", but can't be identical. Looks like we're going to have to generate a collision?

## Steps

```
const bodyParser = require("body-parser")
const express = require("express")
const fs = require("fs")
const customhash = require("./customhash")

const app = express()
app.use(bodyParser.json())

const port = 3000
const flag = "flag"
const secret_key = "Y0ure_g01nG_t0_h4v3_t0_go_1nto_h4rdc0r3_h4ck1ng_m0d3"

app.get('/', (req, res) => {
    console.log("[-] Source view")
    res.type("text")
    return fs.readFile("index.js", (err,data) => res.send(data.toString().replace(flag, "flag")))
})

app.post('/getflag', (req, res) => {
    console.log("[-] Getflag post")
    if (!req.body) {return res.send("400")}
    let one = req.body.one
    let two = req.body.two
    console.log(req.body)
    if (!one || !two) {
        return res.send("400")
    }
    if ((one.length !== two.length) || (one === two)) {
        return res.send("Strings are either too different or not different enough")
    }
    one = customhash.hash(secret_key + one)
    two = customhash.hash(secret_key + two)
    if (one == two) {
        console.log("[*] Flag get!")
        return res.send(flag)
    } else {
        return res.send(`${one} did not match ${two}!`)
    }
})

app.listen(port, () => console.log(`Listening on port ${port}`))
```

If we look at following parts:

```
if (!one || !two) {...

if (if ((one.length !== two.length) || (one === two)) {) {...

one = customhash.hash(secret_key + one)
two = customhash.hash(secret_key + two)
if (one == two) {...
```

We can see that we need to get past these three ifs.
To do so we first of need to request the page with data which contains the keys `one` and `two`.

After that the two keys should contain a value which isnt the same size as well as different in terms of value. Lets just use some `abc` and `def` to begin with.

If we send this to the server we get a message that the two hashes arent the same.
At this point the last condition hits in. To pass it we need to have the same hashes but also have to provide the conditions statet above.

This is where the term "type juggling" comes in handy.

[John Hammond - b00t2root19 CTF: EasyPHP [PHP Web Exploits]](https://youtu.be/KOy6QFKZFGQ?t=282)

The key is to provide two arrays instead of simple links. Since the comparsion in the second if-condition is strict the two arrays are different in lenght but the same if compared as such.

```
body = {
	'one': [{'a':1}],
	'two': [{'a':2}]
}
```

Before the last condition the script creates hashes based on a `secret_key` as well ass the variables provided by us. Since the variables are beeing used as strings both of our arrays are the same and generate the same hash since both arrays are just 0.

## Flag
ractf{Y0u_R_ab0uT_2_h4Ck_t1Me__4re_u_sur3?}
