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
#import "HTTPHeaderField.h"
#import "PushServices.h"
#import <RongIMLib/RongIMLib.h>
#import "RCHBMessage.h"
#import "Account.h"

@implementation HTTPHook

+ (void)load
{
    
    HTTPHeaderField *header = [HTTPHeaderField instance];

    [AFJSONRequestSerializer aspect_hookSelector:@selector(setValue:forHTTPHeaderField:) withOptions:AspectPositionAfter usingBlock:^(id<AspectInfo> info) {
        AFHTTPRequestSerializer *requestSerializer = [info instance];
        NSArray *arguments = [info arguments];
        NSString *key = arguments.lastObject;

        //特殊的key,  -对应_
        NSString *specialKey = [key containsString:@"-"] ? [key stringByReplacingOccurrencesOfString:@"-" withString:@"_"] : nil;
        key = specialKey ?: key;

        //获取新值,并还原key
        NSString *newValue = [header respondsToSelector:NSSelectorFromString(key)] ? [header valueForKey:key] : nil;
        key = specialKey ? [key stringByReplacingOccurrencesOfString:@"_" withString:@"-"] : key;

        if (newValue && ![requestSerializer.HTTPRequestHeaders[key] isEqualToString:newValue]) {
            [requestSerializer setValue:newValue forHTTPHeaderField:key];
        }

    } error:nil];


    [[[NSNotificationCenter defaultCenter] rac_addObserverForName:RCKitDispatchMessageNotification object:nil] subscribeNext:^(NSNotification * _Nullable x) {
        RCMessage *message = x.object;

        if ([message.content isKindOfClass:[RCHBMessage class]]) {

            RCHBMessage *hbMessage = message.content;

            NSDictionary *dic = @{@"redpacketChatId": [hbMessage.extra mj_JSONObject][@"redpacketChatId"]};

            [[APIClient sharedManager] postUserRedpacketStatus:dic Success:^(NSDictionary *respone) {
                if (![dic[@"redpacketStatus"] isEqualToString:@"02"]) {

                    [[APIClient sharedManager] postUserReceiveRedpacket:@{@"redpacketChatId": dic[@"redpacketChatId"]} Success:^(NSDictionary *respone) {
                        NSLog(@"👍bb: %@", respone);
                    } failure:nil];
                }
            } failure:nil];
        }
    }];

;
}

+ (instancetype)shareInstance;
{
    static HTTPHook *instance = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        instance = [HTTPHook new];
    });
    return instance;
}

@end
