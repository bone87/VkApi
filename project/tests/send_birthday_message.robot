*** Settings ***
Documentation    Send Birthday Messages Morning
Library  ../steps/usersSteps.py
Library  ../steps/messagesSteps.py
Resource  common.robot

*** Variables ***

${age_from} =  29
${age_to} =  34

*** Test Cases ***
375298462344_Minsk_offset_0
    BuiltIn.Sleep                         2
    ${users}=    Search Birthday Users    account_id=${account_375298462344}
    ...                                   offset=0
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${account_375298462344}
    ...                                   users=${users}

375298360265_Minsk_offset_30
    BuiltIn.Sleep                         4
    ${users}=    Search Birthday Users    account_id=${account_375298360265}
    ...                                   offset=30
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${account_375298360265}
    ...                                   users=${users}

375298681142_Minsk_offset_60
    BuiltIn.Sleep                         6
    ${users}=    Search Birthday Users    account_id=${ff_account_375298681142}
    ...                                   offset=60
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${ff_account_375298681142}
    ...                                   users=${users}

375447693824_Minsk_offset_90
    BuiltIn.Sleep                         8
    ${users}=    Search Birthday Users    account_id=${ff_account_375447693824}
    ...                                   offset=90
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${ff_account_375447693824}
    ...                                   users=${users}

375445528788_Minsk_offset_120
    BuiltIn.Sleep                         10
    ${users}=    Search Birthday Users    account_id=${ff_account_375445528788}
    ...                                   offset=120
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${ff_account_375445528788}
    ...                                   users=${users}

375336610743_Minsk_offset_150
    BuiltIn.Sleep                         12
    ${users}=    Search Birthday Users    account_id=${ff_account_375336610743}
    ...                                   offset=150
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${ff_account_375336610743}
    ...                                   users=${users}

375292025693_Minsk_offset_180
    BuiltIn.Sleep                         14
    ${users}=    Search Birthday Users    account_id=${ff_account_375292025693}
    ...                                   offset=180
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${ff_account_375292025693}
    ...                                   users=${users}
