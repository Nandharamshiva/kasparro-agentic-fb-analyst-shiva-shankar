setup:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

run:
	python src/run.py "Analyze ROAS drop"

test:
	pytest -q

clean:
	rm -rf .venv __pycache__
