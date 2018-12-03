//
//  HTTPHeaderField.m
//  Lottery
//
//  Created by Johnson on 2018/12/3.
//  Copyright © 2018 tg. All rights reserved.
//

#import "HTTPHeaderField.h"
#import "SecureUDID.h"

@interface HTTPHeaderField()
@property (nonatomic, copy) NSString *deviceId;
@property (nonatomic, copy) NSString *deviceName;
@property (nonatomic, copy) NSString *version;
@property (nonatomic, copy) NSString *packageName;
@property (nonatomic, copy) NSString *User_Agent;

@end

@implementation HTTPHeaderField

+ (instancetype)instance;
{
    HTTPHeaderField *instance = [HTTPHeaderField new];

    NSUInteger index = arc4random() % 1;
    switch (index) {
        case 0://ios
            instance.packageName = [[NSBundle mainBundle] infoDictionary][(NSString *)kCFBundleIdentifierKey];
            instance.deviceId = [SecureUDID UDIDForDomain:instance.packageName usingKey:@""];
            instance.deviceName = [self allIOSDeviceNames][arc4random() % [self allIOSDeviceNames].count];
            instance.version = @"1.5.0";
            instance.User_Agent = @"ios";
            break;

        case 01://android
            instance.packageName = @"Production";
            instance.deviceId = @(867246029172906 + arc4random() % 123456789).stringValue;
            instance.deviceName = [self allANDROIDDeviceNames][arc4random() % [self allANDROIDDeviceNames].count];
            instance.version = @"V1.4.5";
            instance.User_Agent = @"android";
            break;

        default:
            break;
    }
    return instance;
}


+ (NSArray *)allIOSDeviceNames
{
    return @[
             @"iPhone 5s (A1453/A1533)",
             @"iPhone 5s (A1457/A1518/A1528/A1530)",
             @"iPhone 6 Plus (A1522/A1524)",
             @"iPhone 6 (A1549/A1586)",
             @"iPhone 6s (A1633/A1688/A1691/A1700)",
             @"iPhone 6s Plus (A1634/A1687/A1690/A1699)",
             @"iPhoneSE (A1662/A1723/A1724)",
             @"iPhone 7 (A1660/A1779/A1780)",
             @"iPhone 7 Plus (A1661/A1785/A1786)",
             @"iPhone 7 (A1778)",
             @"iPhone 7 Plus(A1784)",
             @"iPhone 8 (A1863/A1906/A1907)",
             @"iPhone 8 (A1905)",
             @"iPhone 8 Plus(A1864/A1898/A1899)",
             @"iPhone 8 Plus(A1897)",
             @"iPhone X (A1865/A1902)",
             @"iPhone X (A1901)",
             @"iPhone XR (A1984/A2105/A2106/A2108)",
             @"iPhone XS (A1920/A2097/A2098/A2100)",
             @"iPhone XS Max (A1921/A2101/A2102/A2104)",
             ];
}

+ (NSArray *)allANDROIDDeviceNames
{
    return @[
             @"Redmi 4",
             @"Redmi 5",
             @"Redmi 6",
             @"Redmi 6Pro",
             @"Redmi 6A",
             @"Redmi 4",
             @"Redmi Note4",
             @"Redmi Note4X",
             @"Redmi Note5",
             @"HUAWEI Mate 20 RS",
             @"HUAWEI Mate 20 Pro",
             @"HUAWEI Mate 20",
             @"HUAWEI nova 3",
             @"HUAWEI P20",
             @"HUAWEI nova 3i",
             @"HUAWEI nova 2s",
             @"XIAO MI MIX3",
             @"XIAO MI MIX",
             @"XIAO MI MIX2",
             @"XIAO MI MIX2s",
             @"XIAO MI8",
             @"XIAO MI MAX",
             @"XIAO MI MAX2",
             @"XIAO MI MAX3",
             ];
}
@end
