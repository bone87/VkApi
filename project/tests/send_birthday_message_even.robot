*** Settings ***
Documentation    Send Birthday Messages Evening
Library  ../steps/usersSteps.py
Library  ../steps/messagesSteps.py
Resource  common.robot

*** Variables ***

${age_from} =  29
${age_to} =  34

*** Test Cases ***
375298462344_Minsk_offset_210
    BuiltIn.Sleep                         2
    ${users}=    Search Birthday Users    account_id=${account_375298462344}
    ...                                   offset=210
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${account_375298462344}
    ...                                   users=${users}

375298360265_Minsk_offset_240
    BuiltIn.Sleep                         4
    ${users}=    Search Birthday Users    account_id=${account_375298360265}
    ...                                   offset=240
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${account_375298360265}
    ...                                   users=${users}

375298681142_Minsk_offset_270
    BuiltIn.Sleep                         6
    ${users}=    Search Birthday Users    account_id=${ff_account_375298681142}
    ...                                   offset=270
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${ff_account_375298681142}
    ...                                   users=${users}

375447693824_Minsk_offset_300
    BuiltIn.Sleep                         8
    ${users}=    Search Birthday Users    account_id=${ff_account_375447693824}
    ...                                   offset=300
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${ff_account_375447693824}
    ...                                   users=${users}

375445528788_Minsk_offset_330
    BuiltIn.Sleep                         10
    ${users}=    Search Birthday Users    account_id=${ff_account_375445528788}
    ...                                   offset=330
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${ff_account_375445528788}
    ...                                   users=${users}


375336610743_Minsk_offset_360
    BuiltIn.Sleep                         12
    ${users}=    Search Birthday Users    account_id=${ff_account_375336610743}
    ...                                   offset=360
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${ff_account_375336610743}
    ...                                   users=${users}

375292025693_Minsk_offset_390
    BuiltIn.Sleep                         14
    ${users}=    Search Birthday Users    account_id=${ff_account_375292025693}
    ...                                   offset=390
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${ff_account_375292025693}
    ...                                   users=${users}
