*** Settings ***
Documentation    Send Birthday Messages Morning.
Resource  resource.robot

*** Test Cases ***
life_375255102578
    Send Messages    account_id=${life_375255102578}
    ...              offset=0
#    ...              test_name=life_375255102578

life_375255100893
    Send Messages    account_id=${life_375255100893}
    ...              offset=30

mts_375292463065
    Send Messages    account_id=${mts_375292463065}
    ...              offset=60

vlc_375299403419
    Send Messages    account_id=${vlc_375299403419}
    ...              offset=90

life_375255220296
    Send Messages    account_id=${life_375255220296}
    ...              offset=120

vlc_375447693824
    Send Messages    account_id=${vlc_375447693824}
    ...              offset=150

mts_375298462344
    Send Messages    account_id=${mts_375298462344}
    ...              offset=180

mts_375298360265
    Send Messages    account_id=${mts_375298360265}
    ...              offset=210

life_375255145904
    Send Messages    account_id=${life_375255145904}
    ...              offset=240

life_375255157173
    Send Messages    account_id=${life_375255157173}
    ...              offset=270

life_375255218247
    Send Messages    account_id=${life_375255218247}
    ...              offset=301

life_375255174804
    Log    BLOCKED
#    Send Messages    account_id=${life_375255174804}
#    ...              offset=330

life_375255095305
    Send Messages    account_id=${life_375255095305}
    ...              offset=360

life_375255092593
    Send Messages    account_id=${life_375255092593}
    ...              offset=390

life_375255092031
    Send Messages    account_id=${life_375255092031}
    ...              offset=420

life_375257214755
    Send Messages    account_id=${life_375257214755}
    ...              offset=450

life_375257246699
    Send Messages    account_id=${life_375257246699}
    ...              offset=480

life_375257291142
    Send Messages    account_id=${life_375257291142}
    ...              offset=510

life_375257316475
    Send Messages    account_id=${life_375257316475}
    ...              offset=540

life_375257182374
    Send Messages    account_id=${life_375257182374}
    ...              offset=570
