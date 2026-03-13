import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium")


@app.cell
def _():

    import marimo as mo
    slider = mo.ui.slider(1, 100, value=50)
    slider

    return (slider,)


@app.cell
def _(slider):
    number = slider.value
    print(f"The number is: {number}")
    return


if __name__ == "__main__":
    app.run()
