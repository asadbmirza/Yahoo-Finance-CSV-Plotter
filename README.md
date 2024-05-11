# Yahoo-Finance-CSV-Plotter
Yahoo Finance Plotter takes in CSV data from Yahoo finance and provides a variety of functions such as share volume plotting, daily volume rate of change, and open/closing price comparisons! OOP project created utilizing matplotlib/Pandas on Python.

Install:
- Clone the repository to your system
- Download any csv data you want from Yahoo CSV
- Place it in the same folder as the cloned repository
- In a main.py file, create an instance of the class by importing Yahoo_CSV_Finance_Plotter, then initiating an object by setting a variable equal to Yahoo_CSV_Finance_Plotter.CSV_Finance_Plotter('csvName.csv')
- You can now call all the available functions and ranges on that object! Any inaccassible ranges will showcase a graph that will stop at the last available range, or if the starting range is less than the end range, will just display all available dates of the graph.

Need to implement/improve on
- Learning more about finance from learning resources to get a better idea of what new functions can be implemented
- **Update 1:**
  - Added high_low comparision function
  - Added optional functionality to plot only given ranges of the csv data to every function, e.g volume_plotter(start = 2, end = 10)
  - Added private helper function increase_decrease_plotter(), used for making the increasing sections of plot graphs green, decreasing sections red, and stagnant sections blue: Currently only used by volume_plotter()
- Adding in functions that use machine learning which can predict future volume fluctuations, open/closing prices etc
- Adding in a GUI to better enhance casual user experience
