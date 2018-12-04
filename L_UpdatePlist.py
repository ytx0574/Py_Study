import biplist


accounts_path = '/Users/johnson/Desktop/1o2k1ppv.plist'
accounts = biplist.readPlist(accounts_path)
accounts



info_plist_path = '/Users/johnson/Desktop/TestRunScript/TestRunScript/Info.plist'
bundle_identifier = 'com.adc.'

info_plist = biplist.readPlist(info_plist_path)
print info_plist

info_plist["CFBundleIdentifier"] = bundle_identifier
print info_plist


biplist.writePlist(info_plist, info_plist_path, binary=False)


