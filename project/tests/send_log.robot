*** Settings ***
Documentation    Send Log File.
Library  ../../framework/utils/email_sender.py

*** Test Cases ***
Log Sender
    Send Email With Attach    attached_file=${LOG_FILE}
    ...                       subject=Test Finished.
