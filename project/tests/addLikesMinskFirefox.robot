*** Settings ***
Documentation    Suite description
Library  ../steps/usersSteps.py
Library  ../steps/likesSteps.py

*** Variables ***
${opera_account} =  310582170
${ff_account} =  291495044
${age_from} =  19
${age_to} =  24
*** Test Cases ***
Test title
    ${users} =          Search Users Minsk               account_id=${ff_account}        age_from=${age_from}		age_to=${age_to}
                        likes users photo account        account_id=${ff_account}        users=${users}
