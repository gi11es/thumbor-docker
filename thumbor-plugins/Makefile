PYTHON = python3

coverage:
	@nosetests -sv --with-coverage --cover-package=wikimedia_thumbor

test:
	@nosetests -sv

offline-test:
	@nosetests -s tests/ --ignore-files='test_proxy_loader.py|test_huge_video.py|test_https_loader.py|test_vips_https_loader.py|test_3d.py'

setup:
	@$(PYTHON) -m pip install -e .[tests]
