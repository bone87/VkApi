*** Settings ***
Documentation    Suite description
Library  ../steps/usersSteps.py
Library  ../steps/likesSteps.py

*** Variables ***
${opera_account} =  310582170
${ff_account} =  291495044

*** Test Cases ***
Test title
    ${users} =          Search Users Minsk               account_id=${ff_account}
                        likes users photo account        account_id=${ff_account}        users=${users}
