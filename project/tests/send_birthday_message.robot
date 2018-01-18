*** Settings ***
Documentation    Send Birthday Messages Morning.
Library  tempTest.py
Library  ../../framework/utils/email_sender.py
Suite Teardown  Suite Teardown

*** Variables ***
${age_from} =  24
${age_to} =  35

*** Test Cases ***
Birthday Sender
    Run Sender    age_from=${age_from}
    ...           age_to=${age_to}

*** Keywords ***
Suite Teardown
    log    ${LOG_FILE}
    Send Email With Attach    attached_file=${LOG_FILE}
    ...                       subject=${SUITE_NAME} - ${SUITE_STATUS}