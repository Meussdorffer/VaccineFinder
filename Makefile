lambda-layer:
	docker run --rm --volume=$(pwd):/lambda-build \
	-w=/lambda-build \
	lambci/lambda:build-python3.8 \
	pip install -r requirements.txt --target python

lambda-function:
	tar -acf lambda-function.zip lambda_function.py vacc.py

build: lambda-layer lambda-function
