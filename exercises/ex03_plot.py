# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.22.0",
#     "plotly[express]>=6.6.0",
#     "polars>=1.39.3",
#     "statsmodels>=0.14.6",
# ]
# ///

import marimo

__generated_with = "0.22.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""
    # Exercise 3: Plotting Visualizations 📊

    **Plot Visuals!**

    **What you'll do:**

    - Create visualizations

    **Instructions:**

    - Complete each TODO section
    - Run cells to see your results
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Added Step 1 Like the practice in example notebooks to load data and set up
    """)
    return


@app.cell
def _():
    import polars as pl
    import plotly.express as px
    import plotly.graph_objects as go

    # Load datasets
    try:
        weather = pl.read_parquet("../data/raw/weather.parquet")
    except:
        weather = pl.read_csv("../data/raw/weather.csv")

    sales = pl.read_json("../data/raw/sales.json")
    students = pl.read_csv("../data/raw/students.csv")

    print("✓ Data loaded successfully!")
    return go, pl, px, sales, students


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 1: Your First Plot - Bar Chart
    """)
    return


@app.cell
def _(pl, px, sales):
    # TODO: Create a bar chart showing sales by category
    # Use plotly express (px.bar)
    # - x-axis: product_category
    # - y-axis: total sales
    # - Add a title
    # - Color the bars

    # Hint: Make sure category_sales is a valid dataframe first!
    category_sales = sales.group_by("product_category").agg([
        pl.col("total_amount").sum().alias("total_sales")
    ])

    ex_fig1 = px.bar(
        data_frame=category_sales,
        x="product_category",
        y="total_sales",
        title="Sales by Category",
        color="product_category"
    )
      # Create your plot here

    # Uncomment when ready:
    ex_fig1.show()
    return (category_sales,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2: Line Chart - Sales Over Time
    """)
    return


@app.cell
def _(pl, px, sales):
    # TODO: Create a line chart showing sales trends by month
    # Use px.line
    # - x-axis: month
    # - y-axis: total revenue
    # - Add markers to the line
    # - Add a title

    sales_with_month = sales.with_columns(
        pl.col("date").str.to_date().dt.month().alias("month")
    )

    monthly_sales = sales_with_month.group_by("month").agg([
        pl.col("total_amount").sum().alias("total_revenue")
    ]).sort("month")


    ex_fig2 =px.line(
        data_frame=monthly_sales,
        x="month",
        y="total_revenue",
        title="Sales Trend by Month",
        markers=True
    )

    # Uncomment when ready:
    ex_fig2.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 3: Scatter Plot - Exploring Relationships
    """)
    return


@app.cell
def _(px, students):
    # TODO: Create a scatter plot showing the relationship between
    # attendance_rate (x-axis) and test_score (y-axis)
    # - Color points by grade_level
    # - Add a trendline (trendline="ols")
    # - Add appropriate title and labels

    ex_fig3 = px.scatter(
        data_frame=students,
        x="attendance_rate",
        y="test_score",
        color="grade_level",
        trendline="ols",
        title="Relationship Between Attendance and Test Score",
        labels={
            "attendance_rate": "Attendance Rate (%)",
            "test_score": "Test Score",
            "grade_level": "Grade Level"
        }
    )

    # Uncomment when ready:
    ex_fig3.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 4: Histogram - Distribution Analysis
    """)
    return


@app.cell
def _(px, sales):
    # TODO: Create a histogram of transaction amounts (total_amount)
    # - Use 30 bins
    # - Add a title
    # - Label the axes
    # - Try adding nbins=30 parameter

    ex_fig4 = px.histogram(
        data_frame=sales,
        x="total_amount",
        nbins=30,
        color="region",
        title="Distribution of Transaction Amounts",
        labels={
            "total_amount": "Transaction Amount",
            "count": "Frequency"
        }
    )

    # Uncomment when ready:
    ex_fig4.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 5: Advanced - Multiple Subplots
    """)
    return


@app.cell
def _(category_sales, go, pl, sales):
    # TODO: Create a dashboard with 2 subplots:
    # 1. Top plot: Bar chart of sales by category (reuse category_sales)
    # 2. Bottom plot: Bar chart of sales by region (reuse region_summary)

    # NEED TO RUN CELL TWO TO USE CATEGORY CELLS VARIABLE FOR THIS TO WORK.

    from plotly.subplots import make_subplots



    region_summary = sales.group_by("region").agg([
        pl.col("total_amount").sum().alias("total_sales")
    ])

    # Hint: Use go.Figure() with make_subplots or add multiple traces
    # This is challenging - check the solution if you get stuck!

    ex_fig5 = make_subplots(
        rows=2,
        cols=1,
        subplot_titles=("Sales by Category", "Sales by Region")
    )

    ex_fig5.add_trace(
        go.Bar(
            x=category_sales["product_category"],
            y=category_sales["total_sales"],
            name="Category Sales"
        ),
        row=1,
        col=1
    )

    ex_fig5.add_trace(
        go.Bar(
            x=region_summary["region"],
            y=region_summary["total_sales"],
            name="Region Sales"
        ),
        row=2,
        col=1
    )

    ex_fig5.update_layout(
        title="Sales Dashboard",
        height=700,
        showlegend=False
    )

    # Uncomment when ready:
    ex_fig5.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🎉 Excellent Work!

    You've completed the plotting exercises!

    **What you practiced:**

    - ✅ Bar charts
    - ✅ Line charts
    - ✅ Scatter plots
    - ✅ Histograms
    - ✅ Advanced: Subplots
    - ✅ Multiple chart types (bar, line, scatter, histogram)
    - ✅ Combining data analysis with visualization

    **What's next?**

    - Try creating your own visualizations with the data!

    **Pro Tips:**

    - Plotly charts are interactive - hover, zoom, pan!
    - Always explore your data before plotting
    """)
    return


if __name__ == "__main__":
    app.run()
