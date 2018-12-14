

import random
import hashlib
import json
import biplist


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

json_str = json.dumps(l)
print(json_str)

account_save_path = '/Users/johnson/Desktop/' + randomAccount() + '.plist'
biplist.writePlist(l, account_save_path, binary=False)


# f = open('/Users/johnson/Desktop/ccccccc.txt', 'w')
# f.write(json_str)
# f.close()



