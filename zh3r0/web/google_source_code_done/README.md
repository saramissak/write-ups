#Google Source code
##500 Points
Chall Link : `http://web.zh3r0.ml:7777/`

you dont get anything free except the source code. Try to search it and also I never liked to upload my homework in google classroom. Help me hack this website please :)

**Author : careless_finch** 

##Steps
In the Source-Code of the site we can find a hint
`<!-- get the 'page' :eyes: -->`

so i just guessed `web.zh3r0.ml:7777?page=upload`
which leads to an upload formular

lets upload a php shell and try to access it

`http://web.zh3r0.ml:7777/?page=shell&cmd=ls`

it works! lets find the flag!
After a bit tweaking i got a extendet shell running which i could access by `http://web.zh3r0.ml:7777/?page=pwny`

To see what we are dealing with `ls -la` and we see a bunch of weirdly named folders.. 

lets search them with `grep -nr 'zh3r0*'` and voilà the flag

##Flag
zh3r0{h3y_d1d_y0u_upl04d_php_c0rr3ct1y???_84651320}