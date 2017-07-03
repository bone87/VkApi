*** Settings ***
Documentation  Likes Users Photo Account
Library  ../steps/usersSteps.py
Library  ../steps/likesSteps.py
Resource  common.robot

*** Variables ***
${count}=  1000
${timedelta} =  2
${age_from} =  25
${age_to} =  35
${status_engaged} =  3

*** Test Cases ***
375298681142_Minsk_likes
    Like Users Photo    account_id=${ff_account_375298681142}
    ...                 age_from=24
    ...                 age_to=25
    ...                 sleep=2


375447693824_Minsk_likes
    Like Users Photo    account_id=${ff_account_375447693824}
    ...                 age_from=26
    ...                 age_to=27
    ...                 sleep=4

375298462344_Minsk_likes
    Like Users Photo    account_id=${account_375298462344}
    ...                 age_from=28
    ...                 age_to=29
    ...                 sleep=6

375298360265_Minsk_likes
    Like Users Photo    account_id=${account_375298360265}
    ...                 age_from=30
    ...                 age_to=31
    ...                 sleep=8

375445528788_Minsk_likes
    Like Users Photo    account_id=${ff_account_375445528788}
    ...                 age_from=30
    ...                 age_to=31
    ...                 sleep=10

375336610743_Minsk_likes
    Like Users Photo    account_id=${ff_account_375336610743}
    ...                 age_from=30
    ...                 age_to=31
    ...                 sleep=12

375292025693_Minsk_likes
    Like Users Photo    account_id=${ff_account_375292025693}
    ...                 age_from=30
    ...                 age_to=31
    ...                 sleep=14

Bone_Minsk_likes_engaged
    BuiltIn.Sleep    16
    ${users} =       Search Birthday Users    account_id=${account_bone}
    ...                                       count=1000
    ...                                       timedelta=${timedelta}
    ...                                       age_from=${age_from}
    ...                                       age_to=${age_to}
    ...                                       status=${status_engaged}
    Likes Users Photo Account                 account_id=${account_bone}
    ...                                       users=${users}

Prichello_Minsk_likes_engaged
    BuiltIn.Sleep    18
    ${users} =       Search Birthday Users    account_id=${account_prichello}
    ...                                       count=1000
    ...                                       timedelta=${timedelta}
    ...                                       age_from=${age_from}
    ...                                       age_to=${age_to}
    ...                                       status=${status_engaged}
    Likes Users Photo Account                 account_id=${account_prichello}
    ...                                       users=${users}

*** Keywords ***
Like Users Photo
    [Documentation]    Likes Users Photo Account
    [Arguments]  ${account_id}
    ...          ${age_from}
    ...          ${age_to}
    ...          ${sleep}
    BuiltIn.Sleep    ${sleep}
    ${users} =       Search Birthday Users    account_id=${account_id}
    ...                                       timedelta=${timedelta}
    ...                                       count=${count}
    ...                                       age_from=${age_from}
    ...                                       age_to=${age_to}
    Likes Users Photo Account                 account_id=${account_id}
    ...                                       users=${users}