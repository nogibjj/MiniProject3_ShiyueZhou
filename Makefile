install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

format:
	black *.py

lint: 
	ruff check *.py 

test:
	python -m pytest -vv --cov=main test_main.py
	
generate_and_push:
	python main.py
	git config --local user.email "action@github.com";
	git config --local user.name "GitHub Action";
	git add .
	git commit -m "test"
	git push
	
all: install format lint test
