init:
	pip install -r requirements.txt
    
clean:
	rm -rf .cache
	rm -rf build
	rm -rf pip_services4_mqtt.egg-info
	rm -f pip_services4_mqtt/*.pyc
	rm -f pip_services4_mqtt/**/*.pyc
	rm -rf test/__pycache__
	rm -rf test/**/__pycache__
	
install:
	pip install -e .

.PHONY: test
test:
	py.test test -s

docgen:
	sphinx-apidoc -f -e -o build pip_services4_mqtt
	cp conf.py ./build/
	cp index.rst ./build/
	sphinx-build -b html build docs -c .
	rm -rf build
