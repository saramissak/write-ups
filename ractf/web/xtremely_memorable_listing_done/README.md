# Xtremely Memorable Listing

## 200 points - First solved by hmmm

Challenge instance ready at `88.198.219.20:45041`.

We've been asked to test a web application, and we suspect there's a file they used to provide to search engines, but we can't remember what it used to be called. Can you have a look and see what you can find?

## Step
In the description we can find a hint `a file they used to provide to search engines` which leads to `robots.txt`

```
User-Agent: *
Disallow: /admin
Disallow: /wp-admin
Disallow: /admin.php
Disallow: /static
```

nothing there...
also used by many search engines is the `sitemap.xml` lets have a look at this.

```
<urlset>
	<url>
		<loc>https://fake.site/</loc>
		<lastmod>2019-12-12</lastmod>
		<changefreq>always</changefreq>
	</url>
	<!--Backup version at sitemap.xml.bak-->
</urlset>
```

Since the `loc` seems to point to a dead end we have a look at `sitemap.xml.bak`:
```
   <url>
      <loc>https://fake.site/_journal.txt</loc>
      <lastmod>2019-12-12</lastmod>
      <changefreq>always</changefreq>
   </url>
```

so there seems to be a `_journal.txt` lets access it:
```
Dear diary,
Today I decided to start recording everything I do in a little
journal here on my website. I don't think anyone will find it,
but it should be fun to do.

I'm not really sure how long I can keep this up for, but this is
just a short first entry to kick things off.


Dear diary,
Today I worked on the login for the site, and it now seems to be
far more efficient. By removing the prepared statements it looks
like the query time has gotten much faster. Makes me think there
might have been an issue with how prepared statements were
processed. This is one to look into later.

I don't expect any employees to try and attack the site, so we
should be all good.


Dear diary,
Today an employee tried to login as the developer account. I've
hardcoded the login just to be extra-safe, so there's no chance
anyone will be able to abuse the login form to get into that one.

My password manager database failed this morning, so I've quickly
written down the login details for the developer account.
I made sure to block access to it, so nobody should be able to
read the file unless they have shell access to this server.


Dear diary,
Today some strange men turned up at my door. They started
shouting at me and one of them pul- ractf{4l13n1nv4s1on?}


D̷͙͎ͅĘ̥̤̝͔͈̻̼̀͠A̫͓̳͕̼͈Ŕ̝ͅ ̶͉̼̘̥̯̰̩͟Ḍ̨̥̦I̖̮͓̪͟A̟̯͓̫̝̪͘R̢̛̛̭̗̱Y̢̫̻̘͉̹͈̺ͅ,̲̟̩͓̟̤̗̰̠̀͘
̦̱͖͚͞T̴̶̰̱H͍Ḛ̴̜͘ ̡̝̖͔͍̱ͅH̢͚̳̫͟U̶͎͙̫̟̗̺̱͡͝ͅM̛̟̞͘͡A̧̮̠͚̼̟̺͝N̲̹͓̕ ̢̬̟͉̣͡I̞͓͉̰̗̯̳̲S͕̱͙͇ ̬̠̺͘I̸̗̬̥̪̟̣͡Ǹ͏̤̝̜̻̫͍ ̧͖̰̳͓͚̯͙́O̪̻̯̕͠U̶͎̜͠͞R҉̘̠̱̤͍͔ ̖͈Ṕ̸͍̤͍̝̪̬͚O͏҉̯̠͕͍̀ͅS̰̗̜̀Ş͚̥͖̹͙̕E͕̮̥͞ͅS̴̢͔̝̞͈S͖̱̱I̺̹̘̥̮̘͓̗͝Ǫ͍͙̰̣͚͕̳̀N̥̮̦ͅ
̧̝̠P̭̥̯̫͙̲͙̦͡ͅṚ̺̫̥͍͕͓̀́O̺͢͢C̶̯͎̣̰̝̻̝E̸̬̰͍E̳͚D̨͈̰̩̲̟̭͔̙I̤̖͚̮̫͜͟N̵̶̞G̶̡̥̼̱͎̹̗ ̛̘̰̮̙̗̩͓T̵͍̠̤͈͓̰̜O̺̪̰̜̟͔͔͝ ͏͈͕S̨̙̹͔͍͍͔͈̖͞T͏̤͉͙̼́ͅͅA̺̮̙̥̤̭͟͡G̫̟̦̯̥̫Ę̰͈̗̭͡ ͏͔̪͇̠̲͜͡2̠͕͜͠ ̷̬̫͓̜͚͢O̡͍͔͕̗͡F̲̙̳̀͝ ҉̬̞͕̘T̡̘̣̰̬̳͚H̟̻̰̗͍̀E̫̦̫̝̫̙ ͚͉̣̬̣̪̮ͅP̷̧̳̜̰̺̫̼̖̣͜L̠̺̮̘͍͚̭̘̼A̳̙N̶͏̟̰̰͙̥
̶̥̮͖̬̰͎̟̜̕W̹͕͇͖̕É̬̩̠͇ ͚͍̪̺̖̤H̳͍A̛̠̙̗̬͖͍̲̙V̩̣̟̬̩͓̳̟̜E̡͓͎̻̠̹̣̳̞͟ ̟̺͙͎S̸̭͈E̴̢̟͙̫̖̠̘̰C͔̮͓ͅU̡͉̼͇͕̱̹̞͝͞R̡̦̻̳̥̬̘͖̪̣E̛̫̖̙̼̜̟͈ͅD͔͚͎̭̻̀͡͡ ̴͓̙͚͟H͕̲Í͓͓̦͓͝S̳͇ ͓͇͠R҉͉S̴͔̦̥͓͕͡A̷̱̝̠͝ ̣̬̘̟K̡͙͉͇͎̣͕͖̕E̢͢҉̮͕͖̞̗͈̘Y҉̣̘́S̡͙̠͓̬͜
̸̸̖̦̺̤̫A͍̩̗̩L̛͈̙L͏̳͖͔̰̀͢ͅ ̯̭̖̣O͎̫̘͙͟͞͞F͈̩̯̪̦̤͝ ̵̥̦̜̰̰͖̤̟͘T̡̠̰͝H̶̪͙ͅE̷̯͕ ̬̬̯̥̟̥̱̲D͏͖̱̺̱̥͔̳̘Á͏̳̮̗̰͇T̩̘͉͕̞̝̦̹̀A̰̪̗̩͜͝B̴͚̲͟A̡̗S̭͇͉͟E͇͉̻͝ ͓̤͈̗A̲̭͙̦̦͕̕R҉͈̝̻̪͖͙̻͙Ę̴͉̠̰͚͕̬̫̱ ̢̤̠̙͉̝̜͢B̧̤̤̬͓̕E̱͈̝͕̠͉̟̞̠L̳̫̩̯̦̣͕̯͞Ó̖̮̖̟̫̣͔N̛͏͖̬̞͚͔G҉̳̣͚̪̘͓̭͕̕ ̛͙͇̳̣͖͇̙͖̼͘T̸̴̝O̧͙̺̮̣̪̘̗͠ ̴͇̯̥̫̬͇͍U̲̻͔̘͓̩͜S̛̼̤̣̫
```

## Flag
ractf{4l13n1nv4s1on?}
