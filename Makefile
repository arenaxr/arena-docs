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
		--ignore-status-codes "0,301,307,403,429,500,522,999" \
		--ignore-missing-alt \
		--ignore-empty-alt \
		--allow-missing-href \
		--no-check-external-hash \
		--no-enforce-https \
		_site

install: $(PROJECT_DEPS)
	@if [ -f .ruby-version ]; then \
		expected=$$(cat .ruby-version | tr -d '[:space:]'); \
		actual=$$(ruby -e 'puts RUBY_VERSION'); \
		major_expected=$$(echo $$expected | cut -d. -f1,2); \
		major_actual=$$(echo $$actual | cut -d. -f1,2); \
		if [ "$$major_expected" != "$$major_actual" ]; then \
			echo "WARNING: Ruby $$actual does not match .ruby-version ($$expected)."; \
			echo "  Install Ruby $$expected via rbenv: rbenv install $$expected"; \
			echo "  Then prepend to PATH: export PATH=\"$$HOME/.rbenv/versions/$$expected/bin:$$PATH\""; \
			exit 1; \
		fi; \
	fi
	$(BUNDLE) config set --local path '_vendor/bundle'
	$(BUNDLE) install

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
