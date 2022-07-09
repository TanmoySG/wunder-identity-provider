curl --request POST \
	--url http://${DEMO_URL}/register/generate \
	--header 'content-type: application/json' \
	--data "{\"email\": \"${DEMO_USER_MAIL}\", \"name\": \"${DEMO_USER_NAME}\",\"password\": \"${DEMO_USER_PWD}\"}"