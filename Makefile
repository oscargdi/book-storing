.PHONY: start
start:
	@echo "Starting the server..."
	PIPENV_DOTENV_LOCATION=.env.local pipenv run python src/main.py
