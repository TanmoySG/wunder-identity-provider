run-demo:
	@make -s teardown
	@echo ------------------------
	@echo Running Complete Demo...
	@echo ------------------------
	@python demo.py complete

run-login-demo:
	@echo ---------------------
	@echo Running Login Demo...
	@echo ---------------------
	@python demo.py login

run-registration-demo:
	@make -s teardown
	@echo ----------------------------
	@echo Running Registration Demo...
	@echo ----------------------------
	@python demo.py registration

build:
	@pip install -r requirements.txt

load-user:
	@export sampleuser=$(cat demo/demo_user.json)

teardown:
	@echo {} > dataFiles/authlib.json
	@echo {} > dataFiles/wunder_profiles_store.json
	@echo Resources Torn Down