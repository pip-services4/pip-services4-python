init:
	pip install -r requirements.txt
    
clean:
	rm -rf .cache
	rm -rf build
	rm -rf pip_services_swagger.egg-info
	rm -f pip_services_swagger/*.pyc
	rm -f pip_services_swagger/**/*.pyc
	rm -rf test/__pycache__
	rm -rf test/**/__pycache__
	
install:
	pip install -e .

.PHONY: test
test:
	py.test test -s

docgen:
	rm -rf build/doc
	sphinx-apidoc -f -e -o build pip_services4_swagger
	mv build/modules.rst build/index.rst
	sphinx-build -b html build/doc doc/api -c .
	rm -rf build
	
