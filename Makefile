ENV=env
PIP=$(ENV)/bin/pip
RUFF=$(ENV)/bin/ruff
PYINSTALLER=$(ENV)/bin/pyinstaller
BUILD_NAME=asteroids
TARGET=/usr/local/bin

.PHONY: all env install lintfix fmt build clean

default: all

all: env install lintfix fmt build clean

env:
	$(info 🌍 ACTIVATING ENVIRONMENT...)
	python -m venv $(ENV)

install:
	$(info 📥 DOWNLOADING DEPENDENCIES...)
	$(PIP) install -r requirements.txt

fmt:
	$(info ✨ CHECKING CODE FORMATTING...)
	$(RUFF) format

lintfix:
	$(info 🔍 RUNNING LINT TOOLS...)
	$(RUFF) check --select I --fix

build: install
	$(info 🏗️ BUILDING THE PROJECT...)
	$(PYINSTALLER) --onefile --noconsole --name $(BUILD_NAME) main.py
	mv dist/$(BUILD_NAME) $(TARGET)

clean:
	$(info 🧹 CLEANING UP...)
	rm -rf build/ dist/
	rm asteroids.spec
