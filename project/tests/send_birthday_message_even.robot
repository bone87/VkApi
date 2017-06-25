*** Settings ***
Documentation    Suite description
Library  ../steps/usersSteps.py
Library  ../steps/messagesSteps.py

*** Variables ***
${opera_account} =  310582170
${ff_account} =  291495044
${ff_account_375298681142} =  286454976
${ff_account_375447693824} =  286454510
${ff_account_375445528788} =  280826200
${age_from} =  29
${age_to} =  34

*** Test Cases ***
375298462344_Minsk_offset_150
    ${users}=    Search Birthday Users    account_id=${opera_account}
    ...                                   offset=150
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${opera_account}
    ...                                   users=${users}

375298360265_Minsk_offset_180
    ${users}=    Search Birthday Users    account_id=${ff_account}
    ...                                   offset=180
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${ff_account}
    ...                                   users=${users}

375298681142_Minsk_offset_210
    ${users}=    Search Birthday Users    account_id=${ff_account_375298681142}
    ...                                   offset=210
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${ff_account_375298681142}
    ...                                   users=${users}

375447693824_Minsk_offset_240
    ${users}=    Search Birthday Users    account_id=${ff_account_375447693824}
    ...                                   offset=240
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${ff_account_375447693824}
    ...                                   users=${users}

375445528788_Minsk_offset_270
    ${users}=    Search Birthday Users    account_id=${ff_account_375445528788}
    ...                                   offset=270
    ...                                   age_from=${age_from}
    ...                                   age_to=${age_to}
    Send Birthday Messages                account_id=${ff_account_375445528788}
    ...                                   users=${users}


