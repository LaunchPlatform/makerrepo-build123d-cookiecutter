# {{ cookiecutter.project_slug }}

Hi there! 😄👋

Thank you for using MakerRepo, and congratulations on creating this sample MakerRepo repository. There are many things you can do with MakerRepo—feel free to explore, customize, and use this project as a starting point.

This project includes:

- **Artifacts** — fixed CAD models (see `{{ cookiecutter.project_slug }}/tutorial_bracket.py`).
- **Generators** — parametric models users can customize (see `{{ cookiecutter.project_slug }}/desk_organizer.py`).

## Quick start

### 1. Install dependencies

From this directory (project root):

```bash
uv sync
```

This installs `build123d`, `makerrepo`, `makerrepo-cli`, and `pydantic` into the project environment.

### 2. Run workflows locally with MakerRepo CLI

All commands below are run from the **project root** (where `pyproject.toml` lives). The CLI discovers artifacts and generators by scanning your Python packages.

**List artifacts and generators:**

```bash
uv run mr artifacts list
uv run mr generators list
```

**View an artifact in the OCP viewer:**

Install and run the [OCP viewer](https://github.com/OpenCadCode/OCP-viewer) first; the commands below open models in it.

```bash
uv run mr artifacts view
# Or specify by name, e.g.:
uv run mr artifacts view tutorial_bracket.tutorial_bracket
```

**Export an artifact to a file (STEP, STL, 3MF, etc.):**

```bash
uv run mr artifacts export -o ./output
# Or to a specific file:
uv run mr artifacts export tutorial_bracket.tutorial_bracket -o bracket.step
```

**Run a generator with custom parameters and view the result:**

```bash
uv run mr generators view desk_organizer/desk_organizer -p '{"length": 150, "width": 90, "height": 40, "n_length": 4, "n_width": 2}'
```

**Export generator output:**

```bash
uv run mr generators export desk_organizer/desk_organizer -p '{"length": 120, "width": 80, "height": 35}' -o organizer.step
```

**Snapshot (screenshot) an artifact or generator:**

```bash
uv run mr artifacts snapshot -o artifact.png
uv run mr generators snapshot desk_organizer/desk_organizer -p '{}' -o generator.png
```

You can use the short alias `mr` instead of `makerrepo-cli`. For full CLI options:

```bash
uv run mr --help
uv run mr artifacts --help
uv run mr generators --help
```

### 3. Clone, edit, and push to MakerRepo.com

This repository was created for MakerRepo.com. To work with it locally:

1. **Create an access token** with Git permissions on the [access token management page](https://makerrepo.com/access-tokens/).
2. **Clone your repository** (when prompted for password, use your [access token](https://makerrepo.com/access-tokens/) secret):

   ```bash
   git clone https://makerrepo.com/{{ cookiecutter.username }}/{{ cookiecutter.project_slug }}.git
   cd {{ cookiecutter.project_slug }}
   ```

3. **Make local changes** — edit CAD modules, add artifacts or generators, then commit and push:

   ```bash
   git add .
   git commit -m "Your commit message"
   git push
   ```

4. After you push, MakerRepo CI will build your artifacts and generators and publish them to the web UI. Refresh your repository page on MakerRepo.com to view and share models in the embedded OCP viewer.

If you generated this project with the cookiecutter template and have not created a MakerRepo repository yet, [create one](https://makerrepo.com/repositories/create), then add it as the remote and push:

   ```bash
   git remote add origin https://makerrepo.com/{{ cookiecutter.username }}/{{ cookiecutter.project_slug }}.git
   git push -u origin main
   ```

## Documentation

- **MakerRepo docs** — [docs.makerrepo.com](https://docs.makerrepo.com/)
- **Getting started** — [docs.makerrepo.com/getting-started/](https://docs.makerrepo.com/getting-started/)
- **Artifacts** — [docs.makerrepo.com/artifacts/](https://docs.makerrepo.com/artifacts/) (decorator options, export formats)
- **Generators** — [docs.makerrepo.com/generators/](https://docs.makerrepo.com/generators/) (parameters, validation, performance)
- **MakerRepo CLI** — [docs.makerrepo.com/makerrepo-cli/](https://docs.makerrepo.com/makerrepo-cli/) (artifacts and generators subcommands)
- **Build123D** — [github.com/gumyr/build123d](https://github.com/gumyr/build123d)

## Project layout

```
{{ cookiecutter.project_slug }}/
├── pyproject.toml
├── README.md
└── {{ cookiecutter.project_slug }}/
    ├── __init__.py
    ├── tutorial_bracket.py   # @artifact — fixed model from build123d tutorial
    └── desk_organizer.py     # @customizable — parametric model
```

- Add more modules and decorate functions with `@artifact` or `@customizable`; MakerRepo (and `mr`) will discover them automatically.
- Use `desc` and `short_desc` on decorators to improve how models appear on MakerRepo.com.
