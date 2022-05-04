#!/bin/bash

export LOAD_TEST_OFFLINE_TOKEN=...
export LOAD_TEST_LOGIN_URL=...
export LOAD_TEST_CLIENT_ID=...
export LOAD_TEST_API_URL=https://console.redhat.com
export LOAD_TEST_ORGANIZATION=...
export LOAD_TEST_LOGIN_MODE=token
export LOAD_TEST_USERNAME=...
export LOAD_TEST_PASSWORD=...
export LOAD_TEST_PROXY=...    

export GEVENT_SUPPORT=True
export LOG_LEVEL=ERROR
export USERS_NO=10
export TEST_TIME=1m

cd load_tester
locust --headless -t $TEST_TIME --users $USERS_NO --spawn-rate 1 --csv locust --host $LOAD_TEST_API_URL --loglevel $LOG_LEVEL