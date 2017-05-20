*** Settings ***
Documentation    Suite description
Library  ../steps/usersSteps.py
Library  ../steps/messagesSteps.py

*** Variables ***
${opera_account} =  310582170
${ff_account} =  291495044

*** Test Cases ***
+375298462344_Minsk_30
    ${users} =          Search Birthday Users            account_id=${opera_account}    age_from=30		    age_to=30
                        Send Birthday Messages           account_id=${opera_account}    users=${users}

+375298360265_Minsk_31
    ${users} =          Search Birthday Users            account_id=${ff_account}       age_from=31		    age_to=31
                        Send Birthday Messages           account_id=${ff_account}       users=${users}

+375298462344_Minsk_32
    ${users} =          Search Birthday Users            account_id=${opera_account}    age_from=32		    age_to=32
                        Send Birthday Messages           account_id=${opera_account}    users=${users}

+375298360265_Minsk_33
    ${users} =          Search Birthday Users            account_id=${ff_account}       age_from=33		    age_to=33
                        Send Birthday Messages           account_id=${ff_account}       users=${users}