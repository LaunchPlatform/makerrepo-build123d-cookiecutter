# makerrepo-build123d-cookiecutter

A [Cookiecutter](https://cookiecutter.readthedocs.io/) template for generating a **Build123D** repository ready for [MakerRepo.com](https://makerrepo.com/) — a GitHub-like platform for manufacturing as code.

## What you get

- A Python project managed with **uv** (no Poetry).
- Dependencies: `build123d`, `makerrepo`, `makerrepo-cli`, and `pydantic`.
- Sample **artifact** (fixed CAD model) and **generator** (parametric model) to learn from.
- A README with next steps, docs links, and local CLI workflow.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) installed (`curl -LsSf https://astral.sh/uv/install.sh | sh` or via your package manager).
- [Cookiecutter](https://cookiecutter.readthedocs.io/) (`pip install cookiecutter` or `uv tool install cookiecutter`).

## Usage

From the directory where you want to create the new project:

```bash
cookiecutter gh:LaunchPlatform/makerrepo-build123d-cookiecutter
```

Or clone this repo and run from the template directory:

```bash
git clone https://github.com/LaunchPlatform/makerrepo-build123d-cookiecutter.git
cd makerrepo-build123d-cookiecutter
cookiecutter . --no-input   # use defaults
# or
cookiecutter .              # prompt for project_name, project_slug, author
```

You will be prompted for:

- **project_name** — Human-readable name (e.g. "My MakerRepo CAD Project").
- **project_slug** — Python-friendly package name (e.g. `my_makerrepo_cad`).
- **author** — Your name or team.

A new directory named after `project_slug` will be created. `cd` into it, then follow the generated project’s **README.md** for:

1. Creating a repo on MakerRepo.com and pushing your code.
2. Using `makerrepo-cli` (`mr`) to list, view, export, and snapshot artifacts and generators locally.
3. Links to [MakerRepo docs](https://docs.makerrepo.com/).

## License

MIT. See [LICENSE](LICENSE).
