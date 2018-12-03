//
//  HTTPHeaderField.h
//  Lottery
//
//  Created by Johnson on 2018/12/3.
//  Copyright © 2018 tg. All rights reserved.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface HTTPHeaderField : NSObject
@property (nonatomic, copy, readonly) NSString *deviceId;
@property (nonatomic, copy, readonly) NSString *deviceName;
@property (nonatomic, copy, readonly) NSString *version;
@property (nonatomic, copy, readonly) NSString *packageName;

@property (nonatomic, copy, readonly) NSString *User_Agent;
+ (instancetype)instance;
@end

NS_ASSUME_NONNULL_END
