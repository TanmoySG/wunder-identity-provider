build:
	@pip install -r requirements.txt


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


load-user-and-run-demo:
	@make -s teardown
	@echo ----------------------------------
	@echo Load User and Run Complete Demo...
	@echo ----------------------------------
	@python demo.py complete demo/demo_user.json 


load-user-and-run-registration:
	@make -s teardown
	@echo ----------------------------------
	@echo Load User and Run Complete Demo...
	@echo ----------------------------------
	@python demo.py registration demo/demo_user.json 


load-user-and-run-login:
	@make -s teardown
	@echo ----------------------------------
	@echo Load User and Run Complete Demo...
	@echo ----------------------------------
	@python demo.py login demo/demo_user.json 


teardown:
	@echo {} > dataFiles/authlib.json
	@echo {} > dataFiles/wunder_profiles_store.json
	@echo Resources Torn Down