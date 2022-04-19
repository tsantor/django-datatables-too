python_version=3.9.11
venv=djangopermfilter_env

env:
	pyenv virtualenv ${python_version} ${venv} && pyenv local ${venv}

reqs:
	python -m pip install -U pip && python -m pip install -r requirements.txt

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

serve:
	python manage.py runserver 0.0.0.0:8080


scratch: env reqs migrate createsuperuser serve


clean:
	# Remove build artifacts
	rm -rf {build,dist,*.egg-info}

build:
	python setup.py sdist bdist_wheel

upload_test:
	python setup.py sdist bdist_wheel && twine upload dist/* -r pypitest

upload:
	python setup.py sdist bdist_wheel && twine upload dist/* -r pypi
