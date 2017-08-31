*** Settings ***
Documentation    Send Birthday Messages Morning.
Resource  resource.robot

*** Test Cases ***
375298462344_Minsk_offset_0
    Send Messages    account_id=${account_375298462344}
    ...              offset=0
    ...              sleep=2

375298360265_Minsk_offset_30
    Send Messages    account_id=${account_375298360265}
    ...              offset=30
    ...              sleep=4

375298681142_Minsk_offset_60
    Send Messages    account_id=${ff_account_375298681142}
    ...              offset=60
    ...              sleep=6

375447693824_Minsk_offset_90
    Send Messages    account_id=${ff_account_375447693824}
    ...              offset=90
    ...              sleep=8
    ...              count=10


375445528788_Minsk_offset_120
    Send Messages    account_id=${ff_account_375445528788}
    ...              offset=120
    ...              sleep=10

375336610743_Minsk_offset_150
    Send Messages    account_id=${ff_account_375336610743}
    ...              offset=150
    ...              sleep=12

375292025693_Minsk_offset_180
    Send Messages    account_id=${ff_account_375292025693}
    ...              offset=180
    ...              sleep=14

DRON_Mama_Minsk_offset_210
    Send Messages    account_id=${ff_account_DRON_Mama}
    ...              offset=210
    ...              sleep=16

375444106107_Minsk_offset_240
    Send Messages    account_id=${vlc_375444106107}
    ...              offset=240
    ...              sleep=18
    ...              count=10

375444106104_Minsk_offset_270
    Send Messages    account_id=${vlc_375444106107}
    ...              offset=270
    ...              sleep=20
    ...              count=10

