# Test output dir (must match default project_slug in cookiecutter.json)
TEST_OUTPUT := _test_output
TEST_PROJECT := $(TEST_OUTPUT)/my_makerrepo_cad

.PHONY: generate verify
# Generate the template into _test_output using default cookiecutter values (no prompt).
generate:
	cookiecutter . --no-input -o $(TEST_OUTPUT)

# Generate, sync deps in the generated project, and list artifacts/generators to verify discovery.
verify: generate
	cd $(TEST_PROJECT) && uv sync && uv run mr artifacts list && uv run mr generators list
