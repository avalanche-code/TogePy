<h1 align="center">TogePy: A Pokemon Team Builder</h1>
<br/>

TogePy is a Pokemon team builder written in Python, and works by querying the [PokeAPI](https://pokeapi.co/) for getting specific information about the Pokemon you want to add to your team.

## Features

- Terminal User Interface made with Textual
- Searching Pokemon via PokeAPI
- Create Teams
- Add searched Pokemon to team
- Delete Teams

## Planned Features

- Delete Pokemon from Teams
- Change Move Set of Pokemon
- Change Ability of Pokemon
- Change Position in Team
- Share/Save Teams
- Give Items to Pokemon, Item Search
- Statistics Overview
- Moveset recommendations based on Pikalytics

## Develop locally

### 0. Install uv

[Get uv by astral here](https://docs.astral.sh/uv/getting-started/installation/)

### 1. Clone Project

```bash
git clone git@github.com:avalanche-code/TogePy.git
```

### 2. cd into directory

```bash
cd TogePy
```

### 3. Sync dependencies

```bash
uv sync
```

### 4. Configure git to use Hooks

```bash
git config core.hooksPath .githooks
```

### 5. Run the program

```bash
uv run -m togepy
```

### Now you're ready to go!

## Tools

Testing with Pytest (pytest-cov, pytest-xdist and pytest-mock)

```bash
uv run pytest --cov -n auto
```

Linting with Ruff (use --fix for autofix)

```bash
uv run ruff check 
```

Security Checks with Bandit


```bash
uv run bandit togepy
```

## Automation

There is a github action in place called ```metronome.yml```. Checks every Push with Linting, Testing and Security Checks. If everything is successful and commit was pushed with a tag, the action tries to build a release. Automatically gets published in the release section of this GitHub page.

There is a git hook in place called ```pre-commit```. If configured correctly, it only lets you commit changes that fulfill Linting, Testing **with 80% coverage**, and Security check. This is meant as an additional security measure or "booster" for coding quality.

There are also 2 shell scripts in the project root folder. 

```uv_verify``` emulates ```mvn verify```, checks everything that the pre-commit hook also checks, but **without coverage**, and then builds locally with ```uv build```. 

```uv_check``` does the same, but **gives test coverage** and doesn't build. It's only meant for manually checking your code quality before ```pre-commit``` hooks in, and as a self-check tool. 
It also generates a local html report.

```metronome.yml```: Install dependencies -> pytest -> lint -> bandit ---if successful and tag--> uv build

<br/>
<p align="center">
<img width="500" height="500" alt="mascot" src="https://github.com/user-attachments/assets/29d128c2-659c-4244-9a42-8fce98d0bc91" display=block />
</p>
<br/>

> This project is being developed as part of the "Automated Software Development (PRI-ASE)" lecture at University of Applied Sciences in Saarbrücken, Germany (htw saar)
