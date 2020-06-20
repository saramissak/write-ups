#Quarantine

##200 points - First solved by clubby789

Challenge instance ready at `88.198.219.20:30807`.

See if you can get access to an account on the webapp.

##Steps

Open the provided ip and port in a webbrowser and you get a webpage.
Broken sign-up but you get a sign-in.

Some gibberish only gets you `invalid username / password.`

Lets try a simple SQL-Injection:
User: `Admin`
Password: `a' or '1'='1'--`

Sadly this gets us following response: `Attempting to login as more than one user!??`

Since the text and the system behind seems to get more than one result lets just `LIMIT` the results

Password: `a' or '1'='1' LIMIT 1--`

**GOTCHA!**

##Flag
ractf{Y0u_B3tt3r_N0t_h4v3_us3d_sqlm4p}