# 📍 in the provided notes we have :  

import arrow

brewing_time = arrow.utcnow()
brewing_time = brewing_time.to("Europe/Rome")
print(brewing_time)

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])
gingerChai = chaiProfile(flavor='ginger', aroma='strong')
print(gingerChai)
print(gingerChai.flavor)
print(gingerChai.aroma)

# - head to notes-breakdown.md