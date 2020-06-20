# NASA
## 500 Points

Hey FBI Agent! Hacker going by the name of **al3xandr0vich1van** has just hacked into NASA and it's been said that he will leak some critical information! Can you track him down for us? I would suggest you that you check his childhood days, we all posted stuff at that time...

**Author : DreyAnd**

## Steps

With the help of `Sherlock` i was able to track down the username to the following site: `https://www.livelib.ru/reader/al3xandr0vich1van`

I translated the site so i could read and found a link in his bio to a googledrive image `https://drive.google.com/file/d/1KIwZxDwVoTXsuNQ_fakoW09xAsY0ipjh/view`

It seems to be some sort of cipher.
**Pigpen cipher** which deciphers to `httpstwittercomhavevisit` -> [https://twitter.com/havevisit](https://twitter.com/havevisit)

after playing with `https://29a.ch/photo-forensics/#level-sweep` i got what i desired and used `tesseract` to extract the flag

## Flag
zh3r0{y0u_b34t_d4_hax0r}
