*** Settings ***
Documentation    Send Birthday Messages Morning.
Resource  resource.robot

*** Test Cases ***
life_375255102578_Minsk_offset_0
    Send Messages    account_id=${life_375255102578}
    ...              offset=0
    ...              sleep=2

life_375255100893_Minsk_offset_30
    Send Messages    account_id=${life_375255100893}
    ...              offset=30
    ...              sleep=4

mts_375292463065_Minsk_offset_60
    Send Messages    account_id=${mts_375292463065}
    ...              offset=60
    ...              sleep=6

vlc_375299403419_Minsk_offset_90
    Send Messages    account_id=${vlc_375299403419}
    ...              offset=90
    ...              sleep=8

life_375255220296_Minsk_offset_120
    Send Messages    account_id=${life_375255220296}
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

life_375255145904_Minsk_offset_240
    Send Messages    account_id=${life_375255145904}
    ...              offset=240
    ...              sleep=18

life_375255157173_Minsk_offset_270
    Send Messages    account_id=${life_375255157173}
    ...              offset=270
    ...              sleep=20

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

life_375255092593_Minsk_offset_390
    Send Messages    account_id=${life_375255092593}
    ...              offset=390
    ...              sleep=28

life_375255092031_Minsk_offset_420
    Send Messages    account_id=${life_375255092031}
    ...              offset=420
    ...              sleep=30

life_375257214755_Minsk_offset_450
    Send Messages    account_id=${life_375257214755}
    ...              offset=450
    ...              sleep=32

life_375257246699_Minsk_offset_480
    Send Messages    account_id=${life_375257246699}
    ...              offset=480
    ...              sleep=34

life_375257291142_Minsk_offset_510
    Send Messages    account_id=${life_375257291142}
    ...              offset=510
    ...              sleep=36

life_375257316475_Minsk_offset_540
    Send Messages    account_id=${life_375257316475}
    ...              offset=540
    ...              sleep=38

life_375257182374_Minsk_offset_570
    Send Messages    account_id=${life_375257182374}
    ...              offset=570
    ...              sleep=40
    ...              max_count=${10}