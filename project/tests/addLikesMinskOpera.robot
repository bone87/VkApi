*** Settings ***
Documentation    Suite description
Library  ../steps/usersSteps.py
Library  ../steps/likesSteps.py

*** Variables ***
${opera_account} =  310582170

*** Test Cases ***
Test title
    ${users} =          Search Users Minsk               account_id=${opera_account}
                        likes users photo account        account_id=${opera_account}        users=${users}
