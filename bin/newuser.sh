#!/bin/bash

PASSWORD=${NEWUSER_PASSWORD}

if [ -z $PASSWORD ]
then
  PASSWORD="password"
fi

echo '[newuser] password is' $PASSWORD

for USERNAME in "$@"
do
  echo '[newuser] adding user' $USERNAME
  sudo adduser --disable-password --gecos "" $USERNAME
  echo '$USERNAME:$PASSWORD' | sudo chpasswd
  sudo chage -d 0 $USERNAME
done
