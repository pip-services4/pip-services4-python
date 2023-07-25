init:
	pip install -r requirements.txt
    
clean:
	rm -rf .cache
	rm -rf build
	rm -rf pip_services_container.egg-info
	rm -f pip_services_container/*.pyc
	rm -f pip_services_container/**/*.pyc
	rm -rf test/__pycache__
	rm -rf test/**/__pycache__
	
install:
	pip install -e .

.PHONY: test
test:
	py.test test -s

run:
	python -m examples.DummyProcess

docgen:
	rm -rf build/doc
	sphinx-apidoc -f -e -o build/doc pip_services4_container
	mv build/doc/modules.rst build/doc/index.rst
	rm -rf doc/api
	sphinx-build -b html build/doc doc/api -c .
