URL:="localhost:5000"

setup:
	@pip install -r requirements.txt
	@read -p "Enter Port: " port; \
	read -p "Enter Mail-Server: " server; \
	read -p "Enter Password: " password; \
	read -p "Enter Sender: " sender; \
	server_config={\"port\":\"$$port\",\"mail-server\":\"$$server\",\"password\":\"$$password\",\"sender\":\"$$sender\"} ;\
	echo $$server_config | jq '.' ;\
	echo "Appyling Mailer Configurations..." ;\
	echo $$server_config | jq '.' > configs/server_config.json

slim-setup:
	@read -p "Enter Port: " port; \
	read -p "Enter Mail-Server: " server; \
	read -p "Enter Password: " password; \
	read -p "Enter Sender: " sender; \
	server_config={\"port\":\"$$port\",\"mail-server\":\"$$server\",\"password\":\"$$password\",\"sender\":\"$$sender\"} ;\
	echo $$server_config | jq '.' ;\
	echo "Appyling Mailer Configurations..." ;\
	echo $$server_config | jq '.' > configs/server_config.json

# run-demo:
# 	@make -s teardown
# 	@echo ------------------------
# 	@echo Running Complete Demo...
# 	@echo ------------------------
# 	@python demo.py complete


# run-login-demo:
# 	@echo ---------------------
# 	@echo Running Login Demo...
# 	@echo ---------------------
# 	@python demo.py login


# run-registration-demo:
# 	@make -s teardown
# 	@echo ----------------------------
# 	@echo Running Registration Demo...
# 	@echo ----------------------------
# 	@python demo.py registration


# load-user-and-run-demo:
# 	@make -s teardown
# 	@echo ----------------------------------
# 	@echo Load User and Run Complete Demo...
# 	@echo ----------------------------------
# 	@python demo.py complete demo/demo_user.json 


# load-user-and-run-registration:
# 	@make -s teardown
# 	@echo ----------------------------------
# 	@echo Load User and Run Complete Demo...
# 	@echo ----------------------------------
# 	@python demo.py registration demo/demo_user.json 


# load-user-and-run-login:
# 	@make -s teardown
# 	@echo ----------------------------------
# 	@echo Load User and Run Complete Demo...
# 	@echo ----------------------------------
# 	@python demo.py login demo/demo_user.json 


teardown:
	@echo {} > dataFiles/authlib.json
	@echo {} > dataFiles/wunder_profiles_store.json
	@echo Resources Torn Down


run-register:
	@curl --request POST \
		--url http://$(URL)/register/generate \
		--header 'content-type: application/json' \
		--data '{"email": "$(DEMO_USER_MAIL)", "name": "$(DEMO_USER_NAME)","password": "$(DEMO_USER_PWD)"}'

run-verify-otp:
	@read -p "Enter OTP: " OTP
	@curl --request POST \
		--url http://$(URL)/register/verify \
		--header 'content-type: application/json' \
		--data '{"email": "$(DEMO_USER_MAIL)", "otp": "$(OTP)"}'

run-login:
	@read -p "Enter OTP: " OTP
	@curl --request POST \
		--url http://$(URL)/login \
		--header 'content-type: application/json' \
		--data '{"email": "$(DEMO_USER_MAIL)", "password": "$(DEMO_USER_PWD)"}'
