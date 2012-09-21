all:
	make clean
	make exec

clean:
	rm -R *.pyc

exec:
	python main.py

card:
	python main.py card

extract:
	@if [[ -z "$(EXP)" ]]; then \
		cd oracle; ./extract.sh; \
	else \
		cd oracle; ./extract.sh "${EXP}"; \
	fi
