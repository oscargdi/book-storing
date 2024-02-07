.PHONY: start
start:
	@echo "Starting the server..."
	PIPENV_DOTENV_LOCATION=.env.local pipenv run python src/main.py

.PHONY: pre-commit
pre-commit:
	@echo "Running pre-commit checks..."
	pipenv run pre-commit run --all-files
