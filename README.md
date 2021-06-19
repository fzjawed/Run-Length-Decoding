# Run-Length-Decoding
>19 June 2021 09:55 PM

I started watch this new donghua (???) - just randomly came across it and I found the animation to be so crisp and nice. The OP for the anime has them doing a choreography and I've always been weak to animated choreography.

***flashbacks to when Chika was animated***

O H M Y G O D

***Question: Given a string s, consisting of digits and lowercase alphabet characters, that's a run-length encoded string, return its decoded version.***

This one was simpler than the encoding one. I originally did this with isdigit() but I think isalpha() works well too. Also I almost forgot but since I'm iterating through a string my ``i`` is the actual character from the string - like I kept thinking of doing s[i] but that isn't necessary. So if the value i encounter isn't a number I just multiply it with the ``num`` value.

Hence storing num as i - anytime you encounter a number you store it in num and return the output.
