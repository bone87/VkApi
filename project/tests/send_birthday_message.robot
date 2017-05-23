*** Settings ***
Documentation    Suite description
Library  ../steps/usersSteps.py
Library  ../steps/messagesSteps.py

*** Variables ***
${opera_account} =  310582170
${ff_account} =  291495044
${ff_account_375298681142} =  286454976
${ff_account_375447693824} =  286454510

*** Test Cases ***
+375298681142_Minsk_26
    ${users} =          Search Birthday Users            account_id=${ff_account_375298681142}    age_from=26	        age_to=26
                        Send Birthday Messages           account_id=${ff_account_375298681142}    users=${users}


+375447693824_Minsk_27
    ${users} =          Search Birthday Users            account_id=${ff_account_375447693824}    age_from=27		    age_to=27
                        Send Birthday Messages           account_id=${ff_account_375447693824}    users=${users}


+375298681142_Minsk_28
    ${users} =          Search Birthday Users            account_id=${ff_account_375298681142}    age_from=28		    age_to=28
                        Send Birthday Messages           account_id=${ff_account_375298681142}    users=${users}


+375447693824_Minsk_29
    ${users} =          Search Birthday Users            account_id=${ff_account_375447693824}    age_from=29		    age_to=29
                        Send Birthday Messages           account_id=${ff_account_375447693824}    users=${users}




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