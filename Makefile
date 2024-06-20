SHELL := /bin/bash
BUNDLE := bundle
JEKYLL := $(BUNDLE) exec jekyll
HTMLPROOF := $(BUNDLE) exec htmlproofer
PROJECT_DEPS := Gemfile

.PHONY: all check install update build serve

all: install serve

check:
	$(JEKYLL) doctor
	$(HTMLPROOF) \
		--ignore-status-codes "0,301,307,403,429,999" \
		--ignore-missing-alt \
		--ignore-empty-alt \
		--allow-missing-href \
 		--no-check-external-hash \
 		--no-enforce-https \
		_site

install: $(PROJECT_DEPS)
	$(BUNDLE) install --path _vendor/bundle

update: $(PROJECT_DEPS)
	$(BUNDLE) update

build:
	$(JEKYLL) build

serve:
	$(JEKYLL) serve

watch:
	$(JEKYLL) serve --watch

clean:
	$(JEKYLL) clean
