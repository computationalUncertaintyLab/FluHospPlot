#mcandrew;

PYTHON:=python3 -W ignore

COMMITprefix:= Flu Hosp data generated on 
COMMITsuffix:=$(shell date +"%Y-%m-%d")

COMMIT:=$(COMMITprefix) $(COMMITsuffix)

runall: preprocess build git

preprocess:
	$(PYTHON) preprocess.py

build:
	$(PYTHON) build.py
	$(PYTHON) produce_data-latest.py

git:
	git add . && git commit -m "$(COMMIT)" && git push
