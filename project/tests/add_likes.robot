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
vlc_375444106107_Minsk_likes
    Like Users Photo    account_id=${vlc_375444106107}
    ...                 age_from=20
    ...                 age_to=20
    ...                 sleep=2

vlc_375444106104_Minsk_likes
    Like Users Photo    account_id=${vlc_375444106104}
    ...                 age_from=21
    ...                 age_to=21
    ...                 sleep=4

vlc_375299403425_Minsk_likes
    Like Users Photo    account_id=${vlc_375299403425}
    ...                 age_from=22
    ...                 age_to=22
    ...                 sleep=6

vlc_375299403419_Minsk_likes
    Like Users Photo    account_id=${vlc_375299403419}
    ...                 age_from=23
    ...                 age_to=23
    ...                 sleep=8

vlc_375445528788_Minsk_likes
    Like Users Photo    account_id=${vlc_375445528788}
    ...                 age_from=24
    ...                 age_to=24
    ...                 sleep=10

vlc_375447693824_Minsk_likes
    Like Users Photo    account_id=${vlc_375447693824}
    ...                 age_from=25
    ...                 age_to=25
    ...                 sleep=12

mts_375298462344_Minsk_likes
    Like Users Photo    account_id=${mts_375298462344}
    ...                 age_from=26
    ...                 age_to=26
    ...                 sleep=14

mts_375298360265_Minsk_likes
    Like Users Photo    account_id=${mts_375298360265}
    ...                 age_from=27
    ...                 age_to=27
    ...                 sleep=16

mts_375292025693_Minsk_likes
    Like Users Photo    account_id=${mts_375292025693}
    ...                 age_from=28
    ...                 age_to=28
    ...                 sleep=18

mts_375298681142_Minsk_likes
    Like Users Photo    account_id=${mts_375298681142}
    ...                 age_from=29
    ...                 age_to=29
    ...                 sleep=20

mts_375336610743_Minsk_likes
    Like Users Photo    account_id=${mts_375336610743}
    ...                 age_from=30
    ...                 age_to=30
    ...                 sleep=22

mts_375298845346_Minsk_likes
    Like Users Photo    account_id=${mts_375298845346}
    ...                 age_from=31
    ...                 age_to=31
    ...                 sleep=24

mts_375292463065_Minsk_likes
    Like Users Photo    account_id=${mts_375298845346}
    ...                 age_from=32
    ...                 age_to=32
    ...                 sleep=2


Bone_Minsk_likes_engaged
    BuiltIn.Sleep    26
    ${users} =       Search Birthday Users    account_id=${account_bone}
    ...                                       count=1000
    ...                                       timedelta=${timedelta}
    ...                                       age_from=${age_from}
    ...                                       age_to=${age_to}
    ...                                       status=${status_engaged}
    Likes Users Photo Account                 account_id=${account_bone}
    ...                                       users=${users}

Prichello_Minsk_likes_engaged
    BuiltIn.Sleep    28
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
    ...          ${limit}=${None}
    BuiltIn.Sleep    ${sleep}
    ${users} =       Search Birthday Users    account_id=${account_id}
    ...                                       timedelta=${timedelta}
    ...                                       count=${count}
    ...                                       age_from=${age_from}
    ...                                       age_to=${age_to}
    Likes Users Photo Account                 account_id=${account_id}
    ...                                       users=${users}
    ...                                       limit=${limit}