import pandas as pd
import matplotlib.pyplot as plt

class CSV_Finance_Plotter:
    def __init__(self, csv_file):
        ##Name of Corresponding CSV goes here
        self.__data = pd.read_csv(csv_file)
        self.__dateSeries = pd.to_datetime(self.__data['Date'])

    def open_close_plotter(self):
        ##opening, and closing prices over time
        plt.figure(figsize=(15, 20))
        plt.plot(self.__dateSeries, self.__data['Close'], label = "Closing", marker = '.', linestyle='-')
        plt.plot(self.__dateSeries, self.__data['Open'], label = "Opening", marker = '.', linestyle='-')
        plt.legend()
        plt.title('Closing/Opening Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.grid(True, which = 'both')
        plt.show()

    def open_adjclose_plotter(self):
        ##opening, adjusted closing over time
        plt.figure(figsize=(15, 20))
        plt.plot(self.__dateSeries, self.__data['Adj Close'], label = "Adjusted Closing", marker = '.', linestyle='-')
        plt.plot(self.__dateSeries, self.__data['Open'], label = "Opening", marker = '.', linestyle='-')
        plt.legend()
        plt.title('Opening/Adjusted Closing Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.grid(True, which = 'both')
        plt.show()

    def volume_plotter(self):
        ##volume plotting
        plt.figure(figsize=(15,20))
        plt.plot(self.__dateSeries, self.__data['Volume'], label = "Volume", color = 'blue')
        plt.title('Volume Per Day Over Time')
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.grid(True, which= 'both')
        plt.show()

    def daily_volume_roc(self):
        #find daily rate of change
        rocPosDict = {}
        rocNegDict = {}
        length = len(self.__data['Volume'])
        for i in range(1, length):
            #calculate rate of change
            temp = (int(self.__data['Volume'][i]) - int(self.__data['Volume'][i - 1]))*100/int(self.__data['Volume'][i - 1])
            temp = round(temp,2)
            if temp >= 0:
                rocPosDict[i - 1] = temp
                rocNegDict[i - 1] = 0
            else : 
                rocPosDict[i - 1] = 0
                rocNegDict[i - 1] = temp

        rocPosSeries = pd.Series(rocPosDict)
        rocNegSeries = pd.Series(rocNegDict)
        
        #set up graph
        plt.figure(figsize=(15,20))
        plt.bar(self.__dateSeries[1:], rocPosSeries, color = 'blue')
        plt.bar(self.__dateSeries[1:], rocNegSeries, color = 'red')
        plt.title('Daily Volume Rate of Change')
        plt.xlabel('Date')
        plt.ylabel('Volume Rate of Change in Percentage')
        plt.grid(True, which= 'both')
        plt.tight_layout()
        plt.show()


finObject = CSV_Finance_Plotter('CSV.csv')
finObject.daily_volume_roc()
finObject.volume_plotter()
finObject.open_adjclose_plotter()
finObject.open_close_plotter()