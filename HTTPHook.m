//
//  HTTPHook.m
//  Lottery
//
//  Created by Johnson on 2018/12/2.
//  Copyright © 2018年 tg. All rights reserved.
//

#import "HTTPHook.h"
#import <Aspects/Aspects.h>
#import <AFNetworking/AFNetworking.h>
#import "SecureUDID.h"

@implementation HTTPHook
{
    NSString *_deviceId;
    NSString *_deviceName;
    NSString *_version;
    NSString *_packageName;
}

+ (void)load
{
    [AFHTTPSessionManager aspect_hookSelector:@selector(POST:parameters:progress:success:failure:) withOptions:AspectPositionBefore usingBlock:^(id<AspectInfo> info) {
        
        AFHTTPSessionManager *manager = [info instance];
        [manager.requestSerializer setValue:[HTTPHook shareInstance]->_deviceId forHTTPHeaderField:@"deviceId"];
        [manager.requestSerializer setValue:[HTTPHook shareInstance]->_deviceName forHTTPHeaderField:@"deviceName"];
        [manager.requestSerializer setValue:[HTTPHook shareInstance]->_version forHTTPHeaderField:@"version"];
        [manager.requestSerializer setValue:[HTTPHook shareInstance]->_packageName forHTTPHeaderField:@"packageName"];
        
    } error:nil];
}

+ (instancetype)shareInstance;
{
    static HTTPHook *instance = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        instance = [HTTPHook new];
        
        instance->_packageName = [[NSBundle mainBundle] infoDictionary][(NSString *)kCFBundleIdentifierKey];
        instance->_deviceId = [SecureUDID UDIDForDomain:instance->_packageName usingKey:instance->_packageName];
        instance->_deviceName = [self allDevieNames][arc4random() % [self allDevieNames].count];
        instance->_version = @"1.5.0";
    });
    return instance;
}

+ (NSArray *)allDevieNames
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

@end
