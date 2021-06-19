# Simple starter kit - Flask, Flask-frozen, and Tailwind

A starter kit to help you create a static website builder using Flask and Tailwind CSS.

The `requirements.txt` and `package-lock.json` files are there just for reference. I would suggest deleting these and starting with a fresh and up-to-date set of libraries.

## Table of contents

- [Tech stack](#tech-stack)
- [Requirements](#requirements)
- [Initial setup](#initial-setup)
- [Development](#development)
  - [The manual way](#the-manual-way)
  - [The scripted way](#the-scripted-way)
- [Useful commands for beginners](#useful-commands-for-beginners)

## Tech stack

If you don't like some of these choices that's no problem, you can swap them
out for something else on your own.

### Back-end

- [Flask](https://pypi.org/project/Flask/)
- [Frozen-Flask](https://pypi.org/project/Frozen-Flask/)
- [Flask-Assets](https://pypi.org/project/Flask-Assets/)

### Front-end

- [TailwindCSS](https://tailwindcss.com/)
- [postcss and postcss-cli](https://github.com/postcss/postcss-cli)
- [autoprefixer](https://github.com/postcss/autoprefixer)
- [@fullhuman/postcss-purgecss](https://github.com/FullHuman/purgecss/tree/master/packages/postcss-purgecss)

## Requirements

As long as you already have [Python](https://www.python.org/), [Node](https://nodejs.org/), and [npm](https://www.npmjs.com/get-npm) installed, you should be good to go.

## Initial setup

Clone this repo anywhere you want and move into the directory:

```shell
git clone https://github.com/nickjj/docker-django-example flask-frozen-tailwind
cd flask-frozen-tailwind
```

Setup your virtual environment in your prefered way, for example:

```shell
python3.9 -m venv venv
source venv/bin/activate
```

Install the necessary Python libraries:

```shell
pip3 install Flask Frozen-Flask Flask-Assets
```

Install the necessary Node libraries:

```shell
npm install tailwindcss postcss postcss-cli autoprefixer @fullhuman/postcss-purgecss
```

## Development

### The manual way

Run the application in development mode in the usual way:

```shell
python3 app.py
```

Generate the Build the static files (for testing):

This will generate a huge CSS file containing the entire Tailwind CSS content.

```shell
python3 app.py build
```

Generate the Build the static files (for production):

This will generate a much smaller CSS file containing only the CSS content that you are actually using.

```shell
export ENVIRONMENT="production"
python3 app.py build
```

Note: You may need to delete the `project/static/.webassets-cache` and `project/static/dist` directories. The scripted commands described below will handleall this for you.


### The scripted way

You may need to run the following in order tomake the bash scripts executable:

```shell
chmod +x scripts/*
```

Run the application in development mode in the usual way:

```shell
scripts/run-dev.sh
```

Generate the Build the static files (for testing):

This will generate a huge CSS file containing the entire Tailwind CSS content.

```shell
scripts/build-dev.sh
```

Generate the Build the static files (for production):

This will generate a much smaller CSS file containing only the CSS content that you are actually using.

```shell
scripts/build.sh
```

## Useful commands for beginners

To install Python libraries from an existing requirements.txt file:

```shell
pip3 install -r requirements.txt
```

To save all required Python libraries into a new or existing requirements.txt file:

```shell
pip3 freeze > requirements.txt
```
