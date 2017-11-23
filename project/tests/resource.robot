*** Settings ***
Documentation    Resource File.
Library  ../steps/usersSteps.py
Library  ../steps/messagesSteps.py
Resource  common.robot

*** Variables ***
${age_from} =  24
${age_to} =  35

*** Keywords ***
Send Messages
    [Documentation]    Send Birthday Messages To Users
    [Arguments]  ${account_id}
    ...          ${offset}
    ...          ${sleep}
    ...          ${max_count}=${20}
    BuiltIn.Sleep    ${sleep}
    ${users}=    Search Birthday Users    account_id=${account_id}
    ...                                   offset=${offset}
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
#    Send Birthday Messages                account_id=${account_id}
#    ...                                   users=${users}
#    ...                                   max_count=${max_count}
