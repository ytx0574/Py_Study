import biplist


accounts_path = '/Users/johnson/Desktop/1o2k1ppv.plist'
accounts = biplist.readPlist(accounts_path)
accounts

# import random
#
# info_plist_path = '/Users/johnson/Desktop/TestPyScript/TestPyScript/Info.plist'
# bundle_identifier = 'com.adc.'
#
# seed = "1234567890abcdefghijklmnopqrstuvwxyz"
# sa = []
# for i in range(22):
#     sa.append(random.choice(seed))
#
# bundle_identifier = ''.join(sa)


info_plist = biplist.readPlist(info_plist_path)
print info_plist

info_plist["CFBundleIdentifier"] = bundle_identifier
print info_plist


biplist.writePlist(info_plist, info_plist_path, binary=False)



