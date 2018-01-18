*** Settings ***
Documentation    Send Birthday Messages Morning.
Library  tempTest.py

*** Variables ***
${age_from} =  24
${age_to} =  35

*** Test Cases ***
Birthday Sender
    Run Sender    age_from=${age_from}
    ...           age_to=${age_to}
    fail
