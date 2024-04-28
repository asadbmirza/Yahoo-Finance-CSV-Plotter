# Yahoo-Finance-CSV-Plotter
Yahoo Finance Plotter takes in CSV data from Yahoo finance and provides a variety of functions such as share volume plotting, daily volume rate of change, and open/closing price comparisons! OOP project created utilizing matplotlib/Pandas on Python.

Need to implement/improve on
- Learning more about finance from learning resources to get a better idea of what new functions can be implemented
- **Update 1:**
  - Added high_low comparision function
  - Added optional functionality to plot only given ranges of the csv data to every function, e.g volume_plotter(start = 2, end = 10)
  - Added private helper function increase_decrease_plotter(), used for making the increasing sections of plot graphs green, decreasing sections red, and stagnant sections blue: Currently only used by volume_plotter()
- Adding in functions that use machine learning which can predict future volume fluctuations, open/closing prices etc
- Adding in a GUI to better enhance casual user experience
