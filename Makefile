all:
	make clean
	make exec

clean:
	rm -R *.pyc

exec:
	python main.py

extract:
	@if [[ -z "$(EXP)" ]]; then \
		cd oracle; ./extract.sh; \
	else \
		cd oracle; ./extract.sh "${EXP}"; \
	fi
