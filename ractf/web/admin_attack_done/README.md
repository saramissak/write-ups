#Admin Attack

##300 points - First solved by alex222

Challenge instance ready at `88.198.219.20:45041`.

Looks like we managed to get a list of users. That admin user looks particularly interesting, but we don't have their password. Try and attack the login form and see if you can get anything.

##Steps
We are greeted by a login screen lets just type `a' or 1=1--` in user and log in.

It worked! but there is only a logout button and we are logged in as a user called `xxslayer420`

Since we know the SQL-Injection worked lets just stick with it..
If we login with `a' or 1=1--` we are just a "simple" user. So lets see if we can login as an admin.

So we change the SQL-Injectino to `a' or username LIKE '%admin%'--`

And we are logged in as **jimmyTehAdmin**

##Flag
ractf{!!!4dm1n4buse!!!}