# Insert witty name

## 200 points - First solved by kullia

Challenge instance ready at `88.198.219.20:45041`.

Having access to the site's source would be really useful, but we don't know how we could get it. All we know is that the site runs python.

## Steps
Since its a python framework running this website we could try to access some python files.

In a previous challange we accessed a `txt` with the `/static?f=[file]` so lets try it again.

After a few trys we found `/static?f=main.py` which we can download.

Looking at the file we can find the flag.

## Flag
ractf{d3velopersM4keM1stake5}
