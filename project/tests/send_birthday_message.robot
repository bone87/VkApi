*** Settings ***
Documentation    Suite description
Library  ../steps/usersSteps.py
Library  ../steps/messagesSteps.py

*** Variables ***
${opera_account} =  310582170
${ff_account} =  291495044

*** Test Cases ***
+375298462344_Minsk_25
    ${users} =          Search Birthday Users            account_id=${opera_account}    age_from=25		    age_to=25
                        Send Birthday Messages           account_id=${opera_account}    users=${users}

+375298360265_Minsk_26
    ${users} =          Search Birthday Users            account_id=${ff_account}       age_from=26		    age_to=26
                        Send Birthday Messages           account_id=${ff_account}       users=${users}

+375298462344_Minsk_27
    ${users} =          Search Birthday Users            account_id=${opera_account}    age_from=27		    age_to=27
                        Send Birthday Messages           account_id=${opera_account}    users=${users}

+375298360265_Minsk_28
    ${users} =          Search Birthday Users            account_id=${ff_account}       age_from=28		    age_to=28
                        Send Birthday Messages           account_id=${ff_account}       users=${users}