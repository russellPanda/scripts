#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time : 2021/4/29 9:43
# @Author : russell
# @File :  testMakeData

from faker import Faker


#%%
fake = Faker('it_IT')
for _ in range(10):
    print(fake.user_name())
    print(fake.company_email())
    print(fake.phone_number())


# Onceas#11