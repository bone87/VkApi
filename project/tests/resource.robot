*** Settings ***
Documentation    Resource File.
Library  ../steps/usersSteps.py
Library  ../steps/messagesSteps.py
Resource  common.robot

*** Variables ***
${age_from} =  29
${age_to} =  34

*** Keywords ***
Send Messages
    [Documentation]    Send Birthday Messages To Users
    [Arguments]  ${account_id}
    ...          ${offset}
    ...          ${sleep}
    BuiltIn.Sleep    ${sleep}
    ${users}=    Search Birthday Users    account_id=${account_id}
    ...                                   offset=${offset}
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${account_id}
    ...                                   users=${users}