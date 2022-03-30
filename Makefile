run-demo:
	@make -s teardown
	@echo --------------------
	@echo Running Demo...
	@echo --------------------
	@python test.py

teardown:
	@echo {} > dataFiles/authlib.json
	@echo {} > dataFiles/wunder_profiles_store.json
	@echo Resources Torn Down