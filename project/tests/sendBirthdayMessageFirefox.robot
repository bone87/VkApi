*** Settings ***
Documentation    Suite description
Library  ../steps/usersSteps.py
Library  ../steps/messagesSteps.py

*** Variables ***
${opera_account} =  310582170
${ff_account} =  291495044
${age_from} =  28
${age_to} =  28
*** Test Cases ***
Test title
    ${users} =          Search Birthday Users            account_id=${ff_account}     age_from=${age_from}		age_to=${age_to}
                        Send Birthday Messages           account_id=${ff_account}     users=${users}
