read -p "Enter PASSWORD: " PWD
curl --request POST \
	--url http://$DEMO_URL/login \
	--header 'content-type: application/json' \
	--data "{\"email\": \"${DEMO_USER_MAIL}\", \"password\": \"${PWD}\"}"