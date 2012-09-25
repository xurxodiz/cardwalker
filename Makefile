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
		cd util; ./extract.sh; \
	else \
		cd util; ./extract.sh "${EXP}"; \
	fi
