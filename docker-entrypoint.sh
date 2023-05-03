#!/bin/bash

ln -s /opt/jdk/bin/java  /usr/local/bin/java
ln -s /opt/allure/bin/allure  /usr/local/bin/allure

exec "$@"
