install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

format:
	black *.py

lint: 
	ruff check *.py 

test:
	python -m pytest -vv --cov=main test_main.py
	
all: install format lint test
