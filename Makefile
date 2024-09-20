# Makefile for firebase_cart package

# Python interpreter
PYTHON := python3

# Poetry command
POETRY := poetry

# Source directory
SRC_DIR := src

# Test directory
TEST_DIR := tests

# Default target
.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  install    : Install dependencies"
	@echo "  test       : Run tests"
	@echo "  lint       : Run linter"
	@echo "  format     : Format code"
	@echo "  clean      : Remove build artifacts"
	@echo "  build      : Build the package"
	@echo "  all        : Run lint, format, test, and build"

.PHONY: install
install:
	$(POETRY) install

.PHONY: test
test:
	$(POETRY) run pytest $(TEST_DIR)

.PHONY: lint
lint:
	$(POETRY) run flake8 $(SRC_DIR) $(TEST_DIR)

.PHONY: format
format:
	$(POETRY) run black $(SRC_DIR) $(TEST_DIR)

.PHONY: clean
clean:
	rm -rf dist
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +

.PHONY: build
build: clean
	$(POETRY) build

.PHONY: all
all: lint format test build