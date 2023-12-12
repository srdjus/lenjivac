install:
	python -m venv venv; \
	source ./venv/bin/activate; \
	pip install -r requirements.txt

test:
	pytest

run: install
	python main.py

clean: 
	rm -rf venv

