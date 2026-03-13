# Week 1 Summary

Week 1 was mainly about setting up the tools and understanding the basic workflow for data science. Instead of jumping straight into analysis, I focused on learning the tools I’ll be using throughout the course and how they work together.

The main tools were:
- Python for coding
- Polars for working with data
- Plotly for visualizations
- Marimo for notebooks
- Markdown for writing explanations
- Git for version control
- UV for managing packages and environments
- VS Code as my main editor

Overall, this week felt like building the foundation before doing more advanced data work.

---

## What Data Science Means

From this week, I understood that data science is about using data to answer questions and support better decisions.

The general process usually involves:

- collecting data
- cleaning and preparing the data
- exploring patterns and trends
- sometimes building models
- explaining the results clearly

I also realized that data science is not just coding. It also requires critical thinking, problem solving, and communication.

---

## Python Basics

Python is the main language I’ll be using in this course. It’s widely used in data science because it’s readable and beginner friendly.

Some of the basics I reviewed included:

- variables and data types
- lists, dictionaries, tuples, and sets
- conditionals and loops
- functions
- importing libraries

One important thing I learned is that I don’t need to memorize everything. Practice and reading code regularly is more important. Errors are also normal when coding and part of the learning process.

---

## Markdown

Markdown is the format I’ll use for writing notes, documentation, and explanations.

It’s simple and uses symbols to format text, like:

- `#` for headings
- `**bold**` for bold text
- `-` for bullet points
- backticks for code
- `[text](link)` for links

I like Markdown because it’s clean, easy to read, and helps document my work clearly.

---

## VS Code

VS Code will be my main coding environment. It lets me write code, manage files, run the terminal, and use Git all in one place.

Some useful habits I learned were:

- opening the whole project folder
- using the integrated terminal
- using the Command Palette
- installing helpful extensions like Python and Pylance

The main idea is to get comfortable using it as my everyday workspace.

---

## Git and Version Control

Git helps track changes in my projects and keeps a history of my work.

The basic workflow I learned was:

1. `git status` – check changes
2. `git add` – stage changes
3. `git commit -m "message"` – save a snapshot
4. `git push` – send changes to GitHub

Using Git helps keep projects organized and prevents losing work. A good habit is making small commits regularly.

---

## UV Package Management

UV is used to manage project environments and dependencies.

Some useful commands include:

- `uv sync`
- `uv add package-name`
- `uv remove package-name`
- `uv run python script.py`
- `uv run marimo edit notebook.py`

The main goal of UV is to keep project environments consistent so the code runs reliably.

---

## Marimo Notebooks

Marimo is the notebook system used in this course. Unlike traditional notebooks, Marimo notebooks are saved as normal `.py` files and update reactively.

This makes them easier to manage with Git and helps avoid hidden states in notebooks.

A good notebook workflow includes:

- keeping one idea per cell
- explaining steps with Markdown
- using clear variable names

---

## Polars for Data Wrangling

Polars is the library used for working with tabular data. It’s designed to be fast and efficient.

Some common tasks include:

- reading data with `pl.read_csv()`
- selecting columns
- filtering rows
- sorting data
- grouping and aggregating
- joining tables
- handling missing values

---

## Plotly for Visualization

Plotly is the visualization library used in the course. Its charts are interactive, which makes exploring data easier.

Common charts include:

- line charts
- bar charts
- scatter plots
- histograms
- box plots

Plotly Express is useful for quickly creating charts, while Graph Objects allows more customization.

The biggest takeaway for me is that visualization is not just about making charts look good. It’s about understanding the data and clearly communicating insights.
