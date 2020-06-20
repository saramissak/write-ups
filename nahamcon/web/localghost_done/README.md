#Localghost
##75 Points

BooOooOooOOoo! This spooOoOooky client-side cooOoOode sure is scary! What spoOoOoOoky secrets does he have in stooOoOoOore??

Connect here: `http://jh2i.com:50003`

**Note, this flag is not in the usual format.**

##Steps

Looking at the adress we see a little ghost and nothing special.
Besides that if we look at the `head` section we can find a `jscoll.js` which dosent provide any function so lets check it out.

The whole function is encoded but all it does is setting a `var _0xbcec`.

Lets see what the client side js console can tell us about it.

```
[
	5: "flag",
	6: "SkNURntzcG9vb29va3lfZ2hvc3RzX2luX3N0b3JhZ2V9",
	7: "setItem",
	8: "localStorage"
]
```

It returns a array containing a keyword `flag` as well as some strange string.
Lets put this into `CyberChef` and we can see its base64 encoded.

##Flag
JCTF{spoooooky_ghosts_in_storage}