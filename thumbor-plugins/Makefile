PYTHON = python3

coverage:
	@nosetests -sv --with-coverage --cover-package=wikimedia_thumbor

test:
	@ASYNC_TEST_TIMEOUT=60 pytest tests/

single-test:
	@ASYNC_TEST_TIMEOUT=60 pytest tests/integration/test_3d.py

offline-test:
	@ASYNC_TEST_TIMEOUT=60 pytest tests/ --ignore 'tests/integration/test_proxy_loader.py' --ignore 'tests/integration/test_huge_video.py' --ignore 'tests/integration/test_https_loader.py' --ignore 'tests/integration/test_vips_https_loader.py' --ignore 'tests/integration/test_3d.py'

online-test:
	@ASYNC_TEST_TIMEOUT=60 pytest tests/integration/test_proxy_loader.py tests/integration/test_huge_video.py tests/integration/test_https_loader.py tests/integration/test_vips_https_loader.py tests/integration/test_3d.py

setup:
	@$(PYTHON) -m pip install -e .[tests]
