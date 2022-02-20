all:

LINT_TARGETS := src/

.PHONY: format
format:
	poetry run autoflake -i --remove-all-unused-imports --remove-unused-variables -r ${LINT_TARGETS}
	poetry run isort ${LINT_TARGETS}
	poetry run black ${LINT_TARGETS}
