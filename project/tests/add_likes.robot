*** Settings ***
Documentation    Suite description
Library  ../steps/usersSteps.py
Library  ../steps/likesSteps.py

*** Variables ***
${account_375298462344} =  310582170
${account_375298360265} =  291495044
${account_bone} =  62641084
${account_prichello} =  8649106
${ff_account_375298681142} =  286454976
${ff_account_375447693824} =  286454510
${ff_account_375445528788} =  280826200
${offset} =  100
${timedelta} =  2
${age_from} =  25
${age_to} =  35
${status_engaged} =  3

*** Test Cases ***
375298681142_Minsk_likes
    BuiltIn.Sleep    2
    ${users} =       Search Birthday Users    account_id=${ff_account_375298681142}
    ...                                       timedelta=${timedelta}
    ...                                       count=1000
    ...                                       age_from=24
    ...                                       age_to=25
    Likes Users Photo Account                 account_id=${ff_account_375298681142}
    ...                                       users=${users}


375447693824_Minsk_likes
    BuiltIn.Sleep    4
    ${users} =       Search Birthday Users    account_id=${ff_account_375447693824}
    ...                                       timedelta=${timedelta}
    ...                                       count=1000
    ...                                       age_from=26
    ...                                       age_to=27
    Likes Users Photo Account                 account_id=${ff_account_375447693824}
    ...                                       users=${users}

375298462344_Minsk_likes
    BuiltIn.Sleep    6
    ${users} =       Search Birthday Users    account_id=${account_375298462344}
    ...                                       timedelta=${timedelta}
    ...                                       count=1000
    ...                                       age_from=28
    ...                                       age_to=29
    Likes Users Photo Account                 account_id=${account_375298462344}
    ...                                       users=${users}

375298360265_Minsk_likes
    BuiltIn.Sleep    8
    ${users} =       Search Birthday Users    account_id=${account_375298360265}
    ...                                       timedelta=${timedelta}
    ...                                       count=1000
    ...                                       age_from=30
    ...                                       age_to=31
    Likes Users Photo Account                 account_id=${account_375298360265}
    ...                                       users=${users}

375445528788_Minsk_likes
    BuiltIn.Sleep    10
    ${users} =       Search Birthday Users    account_id=${ff_account_375445528788}
    ...                                       timedelta=${timedelta}
    ...                                       count=1000
    ...                                       age_from=32
    ...                                       age_to=33
    Likes Users Photo Account                 account_id=${ff_account_375445528788}
    ...                                       users=${users}

Bone_Minsk_likes_engaged
    BuiltIn.Sleep    12
    ${users} =       Search Birthday Users    account_id=${account_bone}
    ...                                       count=1000
    ...                                       timedelta=${timedelta}
    ...                                       age_from=${age_from}
    ...                                       age_to=${age_to}
    ...                                       status=${status_engaged}
    Likes Users Photo Account                 account_id=${account_bone}
    ...                                       users=${users}

Prichello_Minsk_likes_engaged
    BuiltIn.Sleep    14
    ${users} =       Search Birthday Users    account_id=${account_prichello}
    ...                                       count=1000
    ...                                       timedelta=${timedelta}
    ...                                       age_from=${age_from}
    ...                                       age_to=${age_to}
    ...                                       status=${status_engaged}
    Likes Users Photo Account                 account_id=${account_prichello}
    ...                                       users=${users}