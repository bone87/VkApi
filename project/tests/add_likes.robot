*** Settings ***
Documentation    Suite description
Library  ../steps/usersSteps.py
Library  ../steps/likesSteps.py

*** Variables ***
${account_375298462344} =  310582170
${account_+375298360265} =  291495044
${account_bone} =  62641084
${account_prichello} =  8649106
${age_from} =  25
${age_to} =  35
${status_engaged} =  3

*** Test Cases ***
375298462344_Minsk_likes
    ${users} =          Search Users Minsk               account_id=${account_375298462344}           age_from=${age_from}		age_to=${age_to}
                        likes users photo account        account_id=${account_375298462344}           users=${users}


375298360265_Minsk_likes
    ${users} =          Search Users Minsk               account_id=${account_+375298360265}          age_from=${age_from}		age_to=${age_to}
                        likes users photo account        account_id=${account_+375298360265}          users=${users}


Bone_Minsk_likes_engaged
    ${users} =          Search Users Minsk               account_id=${account_bone}                   age_from=${age_from}		age_to=${age_to}     status=${status_engaged}
                        likes users photo account        account_id=${account_bone}                   users=${users}


Prichello_Minsk_likes_engaged
    ${users} =          Search Users Minsk               account_id=${account_prichello}              age_from=${age_from}		age_to=${age_to}     status=${status_engaged}
                        likes users photo account        account_id=${account_prichello}              users=${users}

