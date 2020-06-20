# Finding server information

## 350 points - First solved by cr0wn

Challenge instance ready at `88.198.219.20:30807`.

See if you can find the source, we think it's called `app.py`

## Steps

If you click on a video you get to the `\watch\[filename].mp4` section.
There is a video played based on the `file` provided in the URL.

By inspecting the element the video is base64 encoded.

Lets just try the `app.py` as file and look at the base64 encoded source.
`data:video/mp4;base64,ractf{qu3ry5tr1ng_m4n1pul4ti0n}`

## Flag
ractf{qu3ry5tr1ng_m4n1pul4ti0n}
