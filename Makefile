init:
	@echo "checking to see if you have the python library dependicies..."
	@pip install -r requirements.txt
	@echo "...done :)"

test:
	@./bin/OE -i ./tests/input_test_bed.bed -k ./tests/db/ -o ~/
clean:
	@find . -name './src/*.pyc' -exec rm --force {} +
	@find . -name './src/*.pyo' -exec rm --force {} +
	@find . -name './src/*~' -exec rm --force  {} +
