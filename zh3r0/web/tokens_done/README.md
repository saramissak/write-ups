# Tokens
## 497 Points

The flag was sent by Mr.4N0NYM4U5 to my victim. But i dont have the username and password of the victim to login into the discord account. The only thing i have is a god damn token. Can you help me to get the flag. Ill give you the token and it is all you need. Token : `NzIwMjk1NTYyMzU1NjcxMTIw.XuD_mw.Tl6_E4jtr3UBnwBwX8M8CJrQXbc`

**Author : Mr.4N0NYM4U5**

## Steps
Ok so first i tried going over the discord API and login with the token but that got me just `{"message": "401: Unauthorized", "code": 0}`

so what i found out later was...
If you go on the discord website `discord.com` you should see `open discord in browser`. (if not login to the site and logout)

Go to the `localStorage` and provide a new set with `token` and `"your token"`. After refreshing the page we are able to open discord in the browser and are logged in as the user/bot.

## Flag
zh3r0{1et_7he_F0rce_8e_With_YoU}
