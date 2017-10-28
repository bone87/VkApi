*** Settings ***
Documentation    Send Birthday Messages Morning.
Resource  resource.robot

*** Test Cases ***
life_375255102578_Minsk_offset_0
    Send Messages    account_id=${life_375255102578}
    ...              offset=0
    ...              sleep=2
    ...              max_count=${10}

life_375255100893_Minsk_offset_30
    Send Messages    account_id=${life_375255100893}
    ...              offset=30
    ...              sleep=4
    ...              max_count=${10}

mts_375292463065_Minsk_offset_60
    Send Messages    account_id=${mts_375292463065}
    ...              offset=60
    ...              sleep=6
    ...              max_count=${10}

vlc_375299403419_Minsk_offset_90
    Send Messages    account_id=${vlc_375299403419}
    ...              offset=90
    ...              sleep=8

vlc_375445528788_Minsk_offset_120
    Send Messages    account_id=${vlc_375445528788}
    ...              offset=121
    ...              sleep=10

vlc_375447693824_Minsk_offset_150
    Send Messages    account_id=${vlc_375447693824}
    ...              offset=150
    ...              sleep=12

mts_375298462344_Minsk_offset_180
    Send Messages    account_id=${mts_375298462344}
    ...              offset=181
    ...              sleep=14

mts_375298360265_Minsk_offset_210
    Send Messages    account_id=${mts_375298360265}
    ...              offset=210
    ...              sleep=16
    ...              max_count=${10}

life_375255145904_Minsk_offset_240
    Send Messages    account_id=${life_375255145904}
    ...              offset=240
    ...              sleep=18

life_375255157173_Minsk_offset_270
    Send Messages    account_id=${life_375255157173}
    ...              offset=270
    ...              sleep=20
    ...              max_count=${10}

life_375255218247_Minsk_offset_300
    Send Messages    account_id=${life_375255218247}
    ...              offset=301
    ...              sleep=22

life_375255174804_Minsk_offset_330
    Send Messages    account_id=${life_375255174804}
    ...              offset=330
    ...              sleep=24

life_375255095305_Minsk_offset_360
    Send Messages    account_id=${life_375255095305}
    ...              offset=360
    ...              sleep=26
    ...              max_count=${10}
