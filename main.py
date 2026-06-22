[tool.poetry]
name = "icfes-analytics"
version = "0.1.0"
description = "Análisis ICFES con clustering, series temporales y API"
authors = ["Tu Nombre <tu@email.com>"]
packages = [{include = "icfes_analytics", from = "src"}]

[tool.poetry.dependencies]
python = "^3.11"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"