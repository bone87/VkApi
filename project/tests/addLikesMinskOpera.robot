*** Settings ***
Documentation    Suite description
Library  ../steps/usersSteps.py
Library  ../steps/likesSteps.py

*** Variables ***
${opera_account} =  310582170
${age_from} =  25
${age_to} =  29
*** Test Cases ***
Test title
    ${users} =          Search Users Minsk               account_id=${opera_account}        age_from=${age_from}		age_to=${age_to}
                        likes users photo account        account_id=${opera_account}        users=${users}
