*** Settings ***
Documentation    Suite description
Library  ../steps/usersSteps.py
Library  ../steps/likesSteps.py

*** Variables ***
${prichello_account} =  8649106
${age_from} =  25
${age_to} =  35
${status_engaged} =  3
*** Test Cases ***
Test title
    ${users} =          Search Users Minsk               account_id=${prichello_account}        age_from=${age_from}		age_to=${age_to}        status=${status_engaged}
                        Likes Users Photo Account        account_id=${prichello_account}        users=${users}
