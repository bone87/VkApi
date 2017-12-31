*** Settings ***
Documentation    Send Birthday Messages Morning.
Resource  resource.robot
Suite Teardown  Suite Teardown

*** Test Cases ***
life_375255102578
    Send Messages    account_id=${life_375255102578}
    ...              offset=0

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
    Send Messages    account_id=${life_375259503668}
    ...              offset=150

mts_375298462344
    Send Messages    account_id=${life_375259504065}
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
    ...              offset=300

life_375255174804
    Send Messages    account_id=${life_375255174804}
    ...              offset=330

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

life_375259503743
    Send Messages    account_id=${life_375259503743}
    ...              offset=600

life_375259505623
    Send Messages    account_id=${life_375259505623}
    ...              offset=630

life_375259503749
    Send Messages    account_id=${life_375259503749}
    ...              offset=660

vlc_375296088061
    Send Messages    account_id=${vlc_375296088061}
    ...              offset=690

mts_375295731035
    Send Messages    account_id=${mts_375295731035}
    ...              offset=720

life_375259199963
    Send Messages    account_id=${life_375259199963}
    ...              offset=750

*** Keywords ***
Suite Teardown
    Run Keyword If  '${SUITE_STATUS}' == 'FAIL'
    ...    Send Email With Attach    attached_file=${LOG_FILE}
#    ...                              subject=${TEST_NAME}_FAIL