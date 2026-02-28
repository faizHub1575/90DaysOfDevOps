#!/bin/bash



read -p "enter the service do want to check " service

read -p " do you want to check the status of $service Yes/no" Choice

if [[ "$Choice" == "yes" ]]; then
        systemctl status "$service" | grep -q "active"

        if [ $? -eq 0 ]; then
                echo "services is active"

        else
                echo "services is not active"

        fi

else
        echo "Skipped"
fi

:Wq
