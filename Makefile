test:
	python3 -m unittest tests.test_html
	python3 -m unittest tests.test_dom
	python3 -m unittest tests.test_style
	python3 -m unittest tests.test_JSON
	python3 -m unittest tests.test_svg
	# python3 -m unittest tests.test_x3d
	# python3 -m unittest tests.test_geom
	python3 -m unittest tests.test_sitemap

build:
	rm -rf dist/
	python3 setup.py sdist bdist_wheel
	rm -r build/

deploy:
	rm -r dist/
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
	rm -r build/
