deps:
	@python3 -m venv .venv && \
	  . .venv/bin/activate && \
		pip3 install -r requirements.txt

deps-windows:
	@python3 -m venv .venv && \
	  .\.venv\Scripts\activate && \
		pip3 install -r requirements.txt

run:
	@. .venv/bin/activate && \
	  uvicorn main:app --reload

run-windows:
	@.\.venv\Scripts\activate && \
	  python3 -m uvicorn main:app --reload