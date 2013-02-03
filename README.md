shortcom
========

Finds short .com domain for you.

Why do you need short `.com` domain for your serious business?  
You can ignore that almost every respected company is `.com`.  
But even iOS virtual keyboards have that `.com` key!  
Just imagine your `.co` users canceling autocompletion to `.com`, etc, etc.

There are NO 4-letter or less `.com` domains available at the time of writing.  
All in use or For $$$$ale by squatters.

But, there are a lot of 5-letter `.com`-s waiting for you, for about $10/year only.  
`google.com` is 6-letter, just like `denisr.com` is.

It is really hard to find great short `.com` domain just guessing.  
Tools I have seen did not satisfied me either.  

So I have created a simple [`shortcom.py`](https://github.com/denis-ryzhkov/shortcom/blob/master/shortcom.py) script.  
It starts with config section:

    #### config

    prefix = 'my'
    chars = 'abcdefghijklmnopqrstuvwxyz'
    quantity = 2
    postfix = 'x.com'
    skip_until = None
    sleep_seconds = 0.5

This means you are searching for `my??x.com` where `?` is `a-z`. You may change anything.  
Just keep `sleep_seconds` big enough to not abuse `whois` server.  
`skip_until` may be set to e.g. `'myrrx.com'` to resume from this point after any error or poweroff.

Result is displayed both to screen and saved to files `available.txt` and `taken.txt` respectively:

    $ ./shortcom.py
    myaax.com is taken
    myabx.com is taken
    myacx.com is available
    myadx.com is available
    myaex.com is taken
    ...

Optional [`spellable.py`](https://github.com/denis-ryzhkov/shortcom/blob/master/spellable.py) script
creates `spellable-1.txt` and `spellable-2.txt` files from `available.txt`,
assuming it is regularly hard to spell more than two consonants in a row. However it is not always the case.

That's all. Download the script, tailor config to your needs, and run it!

shortcom version 0.0.2  
Copyright (C) 2013 by Denis Ryzhkov <denisr@denisr.com>  
MIT License, see http://opensource.org/licenses/MIT
