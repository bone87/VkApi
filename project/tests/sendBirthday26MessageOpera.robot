*** Settings ***
Documentation    Suite description
Library  ../steps/usersSteps.py
Library  ../steps/messagesSteps.py

*** Variables ***
${opera_account} =  310582170
${ff_account} =  291495044
${age_from} =  26
${age_to} =  26
*** Test Cases ***
Test title
    ${users} =          Search Birthday Users            account_id=${opera_account}     age_from=${age_from}		age_to=${age_to}
                        Send Birthday Messages           account_id=${opera_account}     users=${users}
