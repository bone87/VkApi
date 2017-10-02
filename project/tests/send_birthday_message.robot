*** Settings ***
Documentation    Send Birthday Messages Morning.
Resource  resource.robot

*** Test Cases ***
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

mts_375292025693_Minsk_offset_240
    Send Messages    account_id=${mts_375292025693}
    ...              offset=240
    ...              sleep=18

mts_375298681142_Minsk_offset_270
    Send Messages    account_id=${mts_375298681142}
    ...              offset=270
    ...              sleep=20

mts_375336610743_Minsk_offset_300
    Send Messages    account_id=${mts_375336610743}
    ...              offset=301
    ...              sleep=22

mts_375298845346_Minsk_offset_330
    Send Messages    account_id=${mts_375298845346}
    ...              offset=330
    ...              sleep=24
