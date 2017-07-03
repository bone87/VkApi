*** Settings ***
Documentation    Send Birthday Messages Evening
Resource  resource.robot

*** Test Cases ***
375298462344_Minsk_offset_210
    Send Messages    account_id=${account_375298462344}
    ...              offset=210
    ...              sleep=2

375298360265_Minsk_offset_240
    Send Messages    account_id=${account_375298360265}
    ...              offset=240
    ...              sleep=4

375298681142_Minsk_offset_270
    Send Messages    account_id=${ff_account_375298681142}
    ...              offset=270
    ...              sleep=6

375447693824_Minsk_offset_300
    Send Messages    account_id=${ff_account_375447693824}
    ...              offset=300
    ...              sleep=8

375445528788_Minsk_offset_330
    Send Messages    account_id=${ff_account_375445528788}
    ...              offset=330
    ...              sleep=10

375336610743_Minsk_offset_360
    Send Messages    account_id=${ff_account_375336610743}
    ...              offset=360
    ...              sleep=12

375292025693_Minsk_offset_390
    Send Messages    account_id=${ff_account_375292025693}
    ...              offset=390
    ...              sleep=14
