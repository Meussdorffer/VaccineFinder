@REM Delete old.
del *.zip

@REM Build layer.
docker run --rm --volume=$(pwd):/lambda-build -w=/lambda-build lambci/lambda:build-python3.8 pip install -r requirements.txt --target python


@REM Build function.
tar -acf lambda.zip lambda_function.py vacc.py
tar -acf layer.zip python
