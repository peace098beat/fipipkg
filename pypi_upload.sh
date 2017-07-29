python setup.py sdist
python setup.py bdist_wheel

twine register dist/*.whl
twine upload dist/*