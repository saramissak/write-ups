#UGGC
##30 Points

Become the admin!

Connect here: `http://jh2i.com:50018`

##Steps
If we open the adress we come to a `username` input to login. We need to login as `admin` to get the flag.

So lets just try `admin` then. Darn the login for `admin` is disabled.
Maybe something else may work.. try `aaa` and voilà we are "logged in" as `aaa`.

lets have a look then how we can change to `admin`

If we look at the cookies we can see a cookie with the value `nnn`.. seems like the username is stored inside the cookie but ciphrated with the `caesar cipher`.

Quick look at how much we need to shift that which is 13.
Now lets ciphrate `admin` and we get `nqzva` which we set as our cookie value.

##Flag
flag{H4cK_aLL_7H3_C0okI3s} 