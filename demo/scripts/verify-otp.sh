read -p "Enter OTP: " OTP
curl --request POST \
	--url http://$DEMO_URL/register/verify \
	--header 'content-type: application/json' \
	--data "{\"email\": \"${DEMO_USER_MAIL}\", \"otp\": \"${OTP}\"}"