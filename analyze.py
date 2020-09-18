#!/usr/bin/env python3
"""
This example assumes the JSON data is saved one line per timestamp (message from server).

It shows how to read and process a text file line-by-line in Python, converting JSON fragments
to per-sensor dictionaries indexed by time.
These dictionaries are immediately put into Pandas DataFrames for easier processing.

Feel free to save your data in a better format--I was just showing what one might do quickly.
"""
import pandas
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import matplotlib.pyplot as plt
import numpy as np


def load_data(file: Path) -> T.Dict[str, pandas.DataFrame]:

    temperature = {}
    occupancy = {}
    co2 = {}
    timedata = {}

    with open("data.txt", "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])

            temperature[time] = {room: r[room]["temperature"][0]}
            occupancy[time] = {room: r[room]["occupancy"][0]}
            co2[time] = {room: r[room]["co2"][0]}
            timedata[time] = datetime.fromisoformat(r[room]["time"])

    data = {
        "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
        "timedata": pandas.DataFrame.from_dict(timedata, "index").sort_index(),
    }

    return data



if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    data = load_data(file)


#2.1
    print("----------2.1----------")
    print("The median of temperature in lab 1 is: ")
    print(data['temperature']['lab1'].median())
    print()
    print("The variance of temperature in lab 1 is: ")
    print(data['temperature']['lab1'].var())
    print()

#2.2
    print("----------2.2----------")
    print("The median of occupancy in the office is: ")
    print(data['occupancy']['office'].median())
    print()
    print("The variance of occupancy in the office is: ")
    print(data['occupancy']['office'].var())
    print()

#2.3
    print("----------2.3----------")
    plt.figure(1)
    s1 = pandas.Series(data['temperature']['lab1'])
    ax1 = s1.plot.kde()
    plt.xlabel("Temperature")
    plt.title("Temperature in Lab1")

    plt.figure(2)
    s2 = pandas.Series(data['occupancy']['lab1'])
    ax2 = s2.plot.kde()
    plt.xlabel("Occupancy")
    plt.title("Occupancy in lab1")

    plt.figure(3)
    s3 = pandas.Series(data['co2']['lab1'])
    ax3 = s3.plot.kde()
    plt.xlabel("CO2")
    plt.title("CO2 in lab1")

    print()

#2.4
    print("----------2.4----------")
    tp = data['timedata'].diff()
    tp = tp.iloc[1:]
    tp = tp[:][0] / np.timedelta64(1, 's')
    print("The mean of time interval in seconds is: ")
    print(tp.mean())
    print("The variance of time interval in seconds^2 is: ")
    print(tp.var())

    plt.figure(4)
    s4 = pandas.Series(tp)
    ax4 = s4.plot.kde()
    plt.xlabel("Time")
    plt.title("Time distribution")
    plt.show()
    print()

#   Part 3
#   To detect anomalies in temperature sensor data, I simply choose to 
#   use 2 standard deviations (95%) as the scale of defining good sensors. 
#   Any data lying out of the 95% range will be identified as an anomaly. 
#   I wrote the script in "analyze.py" to make use of data easier. 
    
    print("----------Part 3----------")


#   3.1
#   Office Temperature

    print("The mean of temperature in the office is: ")
    office_mean = data['temperature']['office'].mean()
    print(office_mean)
    print("The standard deviation of temperature in the office is: ")
    office_std = data['temperature']['office'].std()
    print(office_std)

    print("The bad data points in the office are:")
    for k in range(len(data['temperature']['office'])):
        if data['temperature']['office'][k] >= office_mean + 2 * office_std:
            print(data['temperature']['office'][k])
            data['temperature']['office'][k] = "NaN"
        elif data['temperature']['office'][k] <= office_mean - 2 * office_std:
            print(data['temperature']['office'][k])
            data['temperature']['office'][k] = "NaN"

#   Lab1 Temperature
    print()
    print("The mean of temperature in lab 1 is: ")
    lab1_mean = data['temperature']['lab1'].mean()
    print(lab1_mean)
    print("The standard deviation of temperature in the lab1 is: ")
    lab1_std = data['temperature']['lab1'].std()
    print(lab1_std)

    print("The bad data points in Lab1 are:")
    for k in range(len(data['temperature']['lab1'])):
        if data['temperature']['lab1'][k] >= lab1_mean + 2 * lab1_std:
            print(data['temperature']['lab1'][k])
            data['temperature']['lab1'][k] = "NaN"
        elif data['temperature']['lab1'][k] <= lab1_mean - 2 * lab1_std:
            print(data['temperature']['lab1'][k])
            data['temperature']['lab1'][k] = "NaN"

#   Classroom Temperature

    print("The mean of temperature in class1 is: ")
    class1_mean = data['temperature']['class1'].mean()
    print(class1_mean)
    print("The standard deviation of temperature in class1 is: ")
    class1_std = data['temperature']['class1'].std()
    print(class1_std)

    print("The bad data points in class1 are:")
    for k in range(len(data['temperature']['class1'])):
        if data['temperature']['class1'][k] >= class1_mean + 2 * class1_std:
            print(data['temperature']['class1'][k])
            data['temperature']['class1'][k] = "NaN"
        elif data['temperature']['class1'][k] <= class1_mean - 2 * class1_std:
            print(data['temperature']['class1'][k])
            data['temperature']['class1'][k] = "NaN"

#   Calculate the new mean and std: 
#   Office
    print()
    print("The updated mean of temperature in the office is: ")
    office_mean = data['temperature']['office'].mean()
    print(office_mean)
    print("The updated std of temperature in the office is: ")
    office_std = data['temperature']['office'].std()
    print(office_std)

#   Lab1
    print()
    print("The updated mean of temperature in lab 1 is: ")
    lab1_mean = data['temperature']['lab1'].mean()
    print(lab1_mean)
    print("The updated std of temperature in the lab1 is: ")
    lab1_std = data['temperature']['lab1'].std()
    print(lab1_std)

#   Class1
    print()
    print("The updated mean of temperature in class1 is: ")
    class1_mean = data['temperature']['class1'].mean()
    print(class1_mean)
    print("The updated std of temperature in class1 is: ")
    class1_std = data['temperature']['class1'].std()
    print(class1_std)
    print()
#3.3
    st1 = 'The temperature bound of the office is ' + repr(office_mean - 2 * office_std) + ' to ' + repr(office_mean + 2 * office_std) + ' degrees. '
    print(st1)
    st2 = 'The temperature bound of lab1 is ' + repr(lab1_mean - 2 * lab1_std) + ' to ' + repr(lab1_mean + 2 * lab1_std) + ' degrees. '
    print(st2)
    st3 = 'The temperature bound of class1 is ' + repr(class1_mean - 2 * class1_std) + ' to ' + repr(class1_mean + 2 * class1_std) + ' degrees. '
    print(st3)
