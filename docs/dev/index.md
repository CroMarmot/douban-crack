# Developer

## Dev

```sh
pip3 install -e .
```

## test

```sh
hatch run tests:test
hatch run tests:test -VV tests/unit/test_crack_html.py
```

## Lint

hatch + ruff + mypy + black

```sh
hatch run lint:all
hatch run lint:fmt
```

## Docs

```sh
hatch run docs:serve
hatch run docs:build
```

## Build and Publish

```sh
hatch build
tar -tvf dist/douban_crack-*.tar.gz

# to testpypi
twine upload --repository testpypi dist/*
# to pypi
twine upload dist/*
```
