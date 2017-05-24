*** Settings ***
Documentation    Suite description
Library  ../steps/usersSteps.py
Library  ../steps/likesSteps.py

*** Variables ***
${account_375298462344} =  310582170
${account_+375298360265} =  291495044
${account_bone} =  62641084
${account_prichello} =  8649106
${ff_account_375298681142} =  286454976
${ff_account_375447693824} =  286454510
${ff_account_375445528788} =  280826200
${age_from} =  25
${age_to} =  35
${status_engaged} =  3

*** Test Cases ***
375298681142_Minsk_likes
    ${users} =          Search Users Minsk               account_id=${ff_account_375298681142}        age_from=21		        age_to=22
                        likes users photo account        account_id=${ff_account_375298681142}        users=${users}


375447693824_Minsk_likes
    ${users} =          Search Users Minsk               account_id=${ff_account_375447693824}        age_from=22		        age_to=23
                        likes users photo account        account_id=${ff_account_375447693824}        users=${users}



375298462344_Minsk_likes
    ${users} =          Search Users Minsk               account_id=${account_375298462344}           age_from=24		        age_to=25
                        likes users photo account        account_id=${account_375298462344}           users=${users}


375298360265_Minsk_likes
    ${users} =          Search Users Minsk               account_id=${account_+375298360265}          age_from=26		        age_to=27
                        likes users photo account        account_id=${account_+375298360265}          users=${users}

375445528788_Minsk_likes
    ${users} =          Search Users Minsk               account_id=${account_+375298360265}          age_from=28		        age_to=29
                        likes users photo account        account_id=${account_+375298360265}          users=${users}

Bone_Minsk_likes_engaged
    ${users} =          Search Users Minsk               account_id=${account_bone}                   age_from=${age_from}		age_to=${age_to}     status=${status_engaged}
                        likes users photo account        account_id=${account_bone}                   users=${users}


Prichello_Minsk_likes_engaged
    ${users} =          Search Users Minsk               account_id=${account_prichello}              age_from=${age_from}		age_to=${age_to}     status=${status_engaged}
                        likes users photo account        account_id=${account_prichello}              users=${users}

