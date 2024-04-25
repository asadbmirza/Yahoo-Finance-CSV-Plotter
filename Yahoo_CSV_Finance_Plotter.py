import pandas as pd
import matplotlib.pyplot as plt

class CSV_Finance_Plotter:
    def __init__(self, csv_file):
        ##Name of Corresponding CSV goes here
        self.__data = pd.read_csv(csv_file)
        self.__dateSeries = pd.to_datetime(self.__data['Date'])

    ##Private helper function that plots green when increasing, blue when stagnant, and red when decreasing
    def _increase_decrease_plotter(self, start, end, dates, data, dataType):
        streak = 1
        track = {"inc": False, "dec": False, "same": True}
        plot = False
        colour = 'blue'
        for i in range(start + 1, end):
            if data['Volume'][i] > data['Volume'][i-1]:
                if track['inc'] == True:
                    streak += 1
                else:
                    plot = True
                    if (track['dec'] == True):
                        colour = 'red'
                        track['dec'] = False
                    else:
                        colour = 'blue'
                        track['same'] = False
                    track['inc'] = True

            elif data['Volume'][i] < data['Volume'][i-1]:
                if track['dec'] == True:
                    streak += 1
                else:
                    plot = True
                    if (track['inc'] == True):
                        colour = 'green'
                        track['inc'] = False
                    else:
                        colour = 'blue'
                        track['same'] = False
                    track['dec'] = True
            else:
                if track['same'] == True:
                    streak += 1
                else:
                    plot = True
                    if (track['dec'] == True):
                        colour = 'red'
                        track['dec'] = False
                    else:
                        colour = 'green'
                        track['inc'] = False
                    track['same'] = True

            if plot == True:
                plt.plot(dates[i-streak:i], data[dataType][i-streak:i], color = colour)
                plot = False
                streak = 2
        
        if track['dec']:
            colour = 'red'
        elif track['inc']:
            colour = 'green'
        else:
            colour = 'blue'
        plt.plot(dates[end-streak:end], data[dataType][end-streak:end], color = colour)

    ##Contains optional parameters that recieve starting and ending positions of data, as well as closing/adj close parameters
    def open_close_plotter(self, start = -1, end = -1, closeType = "Close"):
        if (start < 0):
            start = 0
        if (end < start or end > len(self.__dateSeries)):
            end = len(self.__dateSeries)
        if closeType != "Adj Close" and closeType != "Close":
            closeType = "Close"
        ##opening, and closing prices over time
        plt.figure(figsize=(15, 20))
        plt.plot(self.__dateSeries[start:end], self.__data[closeType][start:end], label = closeType, marker = '.', linestyle='-')
        plt.plot(self.__dateSeries[start:end], self.__data['Open'][start:end], label = "Open", marker = '.', linestyle='-')
        plt.legend()
        plt.title(closeType + '/Open Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Stock Price')
        plt.grid(True, which = 'both')
        plt.show()

    ##Contains optional parameters that recieve starting and ending positions of data
    def high_low_plotter(self, start = -1, end = -1):
        if (start < 0):
            start = 0
        if (end < start or end > len(self.__dateSeries)):
            end = len(self.__dateSeries)
        plt.figure(figsize=(15,20))
        plt.bar(self.__dateSeries[start:end], self.__data["High"][start:end], label = "High", linestyle= '-')
        plt.bar(self.__dateSeries[start:end], self.__data["Low"][start:end], label = "Low", linestyle= '-')
        ##Make min of y scale be the largest number between 0, and the least price from the data - 0.5.
        plt.ylim(max(0, min(self.__data['Low'][start:end]) - 0.5), max(self.__data['High'][start:end]))
        plt.legend()
        plt.title('High/Low Closing Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Stock Price')
        plt.grid(True, which = 'both')
        plt.show()

    ##Contains optional parameters that recieve starting and ending positions of data
    def volume_plotter(self, start = -1, end = -1 ):
        if (start < 0):
            start = 0
        if (end < start or end > len(self.__dateSeries)):
            end = len(self.__dateSeries)
        ##volume plotting
        plt.figure(figsize=(15,20))
        self._increase_decrease_plotter(start, end, self.__dateSeries, self.__data, 'Volume')
        plt.title('Volume Per Day Over Time')
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.grid(True, which= 'both')
        plt.show()

    ##Contains optional parameters that recieve starting and ending positions of data
    def daily_volume_roc(self, start = -1, end = -1):
        if (start < 0):
            start = 0
        if (end < start or end > len(self.__dateSeries)):
            end = len(self.__dateSeries)
        #find daily rate of change
        rocPosDict = {}
        rocNegDict = {}
        length = len(self.__data['Volume'])
        for i in range(start + 1, end):
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
        plt.bar(self.__dateSeries[start + 1:end], rocPosSeries, color = 'green')
        plt.bar(self.__dateSeries[start + 1:end], rocNegSeries, color = 'red')
        plt.title('Daily Volume Rate of Change')
        plt.xlabel('Date')
        plt.ylabel('Volume Rate of Change in Percentage')
        plt.grid(True, which= 'both')
        plt.tight_layout()
        plt.show()


