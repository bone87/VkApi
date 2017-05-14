*** Settings ***
Documentation    Suite description
Library  ../steps/usersSteps.py
Library  ../steps/likesSteps.py

*** Variables ***
${chrome_account} =  62641084
${ff_account} =  291495044
${age_from} =  21
${age_to} =  35
${status_engaged} =  3
*** Test Cases ***
Test title
    ${users} =          Search Users Minsk               account_id=${chrome_account}        age_from=${age_from}		age_to=${age_to}        status=${status_engaged}
                        Likes Users Photo Account        account_id=${chrome_account}        users=${users}
