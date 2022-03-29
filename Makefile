run:
	echo {} > dataFiles/authlib.json
	echo {} > dataFiles/wunder_profiles_store.json
	python test.py

teardown:
	echo {} > dataFiles/authlib.json
	echo {} > dataFiles/wunder_profiles_store.json