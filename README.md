# QA Team Solvemed - Plotting

QA Team Solvemed - Plotting is a Python library for dealing with plotting graphs for data visualization.

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

# Introduction
Plotting is used to explore data, and is one of the most important tasks that engineers and scientists use computers for. 
Plots are used to:

- present and understand data; and
- to check computed results visually.

We will use the tools presented in this notebook to visualise results in subsequent files.

# Objectives
- Introduction to a programmatic approach to plotting 
- Create line plots and bar charts from discrete data sets
- Create line plots of mathematical functions
- Create histograms for distribution-like data 
- Develop interactive plots
- Create contour plots of functions of two variables

# Visuals

## Seaborn library
Seaborn is a Python visualization library built on matplotlib. It comes equipped with preset styles and color palettes to create complex, aesthetically pleasing charts with a few lines of code.  

Due to its integration with matplotlib, Seaborn allows to use it across the many environments that matplotlib supports. Moreover, users coming from matplotlib will find that much of their knowledge transfers. Seaborn makes it easy to switch between different visual representations by using a consistent dataset-oriented API. 

Seaborn features: 

- API abstraction across visualizations  

- Statistical estimation and error bars 

- Informative distributional summaries 

- Specialized plots for categorical data 

- Composite views onto multivariate datasets 

- Classes and functions for making complex graphics 

## Bokeh library

Bokeh and Plotnine libraries are based on The Grammar of Graphics concepts, but Bokeh is native to Python, unlike Plotnine which is ported over from R.  

Bokeh allows to create interactive and web-ready plots. Moreover, Bokeh supports streaming and real-time data analysis. 

This library has a wide spectrum of applications, with three main interfaces with varying levels of control to accommodate different user types: 

 - a level for creating charts quickly - it includes methods for creating common charts such as bar plots, box plots, and histograms,

- a level allowing to control the basic building blocks of each chart (the dots in a scatter plot, for example), 

- a level geared toward developers and software engineers. It has no pre-set defaults and requires you to define every element of the chart. 

