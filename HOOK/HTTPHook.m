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
#import "AppRemoteConfig.h"

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
            
            NSDictionary *parameters = @{@"redpacketChatId": [hbMessage.extra mj_JSONObject][@"redpacketChatId"]};
            //获取红包状态
            [[APIClient sharedManager] postUserRedpacketStatus:parameters Success:^(NSDictionary *respone) {
                
                //抢红包
                [[APIClient sharedManager] postUserReceiveRedpacket:parameters Success:^(NSDictionary *respone) {
                    NSLog(@"👍bb: %@", respone);
                } failure:nil];
                
            } failure:nil];
            
            //获取抢包的状态
            [[APIClient sharedManager] postserRedpacketList:parameters Success:^(NSDictionary *respone) {
                NSString *redPacketListStr = [respone mj_JSONString];
                
                NSString *path = [NSHomeDirectory() stringByAppendingString:@"/Documents/log"];
                NSMutableString *str = [NSMutableString stringWithContentsOfFile:path encoding:NSUTF8StringEncoding error:nil] ?: [NSMutableString new];
                
                [str appendString:redPacketListStr];
                [str appendString:@"\n\n"];
                
                [str writeToFile:path atomically:YES encoding:NSUTF8StringEncoding error:nil];
            } failure:nil];
        }
    }];

    [[[NSNotificationCenter defaultCenter] rac_addObserverForName:kRemoteConfigJoinChatRoomSuccessNotification object:nil] subscribeNext:^(NSNotification * _Nullable x) {
        [UserInfoStatus isLoginStatus] ? [[APIClient sharedManager] postUserSingWithSuccess:nil failure:nil] : nil;
    }];
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

+ (void)saveToLoalValue:(id)value mark:(NSString *)mark;
{
    if (![value isKindOfClass:[NSString class]]) {
        value = [value mj_JSONString];
    }
    value = [value stringByAppendingString:@"\n"];
    NSString *path = [NSHomeDirectory() stringByAppendingFormat:@"/Documents/%@-%@", mark, [NSDate date]];
    [value writeToFile:path atomically:YES encoding:NSUTF8StringEncoding error:nil];
}

@end
