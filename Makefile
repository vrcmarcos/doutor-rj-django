install:
	@pip install -r requirements.txt
run:
	@python ./doctor_rj/manage.py runserver 0.0.0.0:8000