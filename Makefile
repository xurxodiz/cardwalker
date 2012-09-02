all:
	make clean
	make exec

clean:
	rm *.pyc

exec:
	python main.py
