

import random
import string
import hashlib
import json


def randomAccount():

    seed = "1234567890abcdefghijklmnopqrstuvwxyz"
    sa = []
    for i in range(8):
        sa.append(random.choice(seed))

    return ''.join(sa)



l = []
md5 = hashlib.md5()
for i in range(20):

    account = randomAccount()
    md5.update(account)
    account_md5 = md5.hexdigest()[0:8]

    l.append({account: account_md5})

print json.dumps(l)