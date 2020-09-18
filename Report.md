Final Report

Task 0

The message on the server terminal was “IoT simulator connected to ('::1', 53936, 0, 0)”, and the message on the client terminal was “ECE Senior Capstone IoT simulator”. 

Task 1

I added three lines of code which have the following effects: open file, write to it, and close the file. 

Task 2

I collected 715 lines of data. Of the 715 lines, we have: 

2.1 The median of temperature in lab 1 is 21.02 degrees, and variance is 6.39.

2.2 The median of occupancy in the office is 2.0, and variance is 1.68. 

2.4 The mean of time interval is 1.02 seconds, and variance is 1.14.

2.3&2.4The pictures are as follows: 

![picture](https://github.com/zhjunyu/2020-sensor-miniproject/blob/main/TEMPERATURE.png)

![picture](https://github.com/zhjunyu/2020-sensor-miniproject/blob/main/OCCUPANCY.png)

![picture](https://github.com/zhjunyu/2020-sensor-miniproject/blob/main/CO2.png)

![picture](https://github.com/zhjunyu/2020-sensor-miniproject/blob/main/TIME.png)



The mean, median, variance, and the plots are also shown in “analyze.py”. The probability distribution function has the shape of gaussian distribution, though it is skewed a little bit. 




Task 3

3.1 The algorithm is easy to understand: to detect anomalies in temperature sensor data, I simply choose to use 2 standard deviations (95%) as the scale of defining good sensors. Any data lying out of the 95% range will be identified as an anomaly. I wrote the script in "analyze.py" to make use of data easier. After finding and removing the anomalies, I used the updated data to calculate the standard deviation again to get more precise data. 

The bad data points in the office are:
4.337112754258847
26.07735631886634
15.769898972748134
27.675028186195725
28.2208093150452
19.630205214598462

The bad data points in Lab1 are:
26.851183790200356
41.203402518058766
-8.664839352290723
14.947083674477813

The bad data points in class1 are:
-160.53405196325397

The updated mean of temperature in the office is:
23.00937899032705

The updated std of temperature in the office is:
0.6160601485635125

The updated mean of temperature in lab 1 is:
21.008370408045018

The updated std of temperature in the lab1 is:
0.4944908191414018

The updated mean of temperature in class1 is:
27.218955730214198

The updated std of temperature in class1 is:
2.5670526480730573

3.2 A persistent change in temperature doesn’t always indicate a failed sensor; it may be caused by change in environment (for example, season changes or changes caused by AC). Data points which has a large difference from the mean indicates a failed sensor; for example, I detected -160 and 41 degrees, and this data indicate a failed sensor. 

3.3 The possible bounds on temperature for each room type in degrees are:

Office: 21.78 to 24.24

Lab1: 20.02 to 22.00

Class1: 22.08 to 32.35


Task 4

4.1 The data above conforms to real life to some extent. For example, the temperature in the lab changes in a smaller range because when doing experiments, variables such as temperature should be strictly controlled. The classroom experiences larger temperature change because it is relatively more open and contains more people than labs and offices. 

4.2 The simulation may fail to deal with some situations in reality. For example, it doesn’t have a stopping criteria which stops receiving data from failed sensors, which may cause anomalies in data. Moreover, if the sensors send data to the server at the same time, it may not be able to deal with it. 

4.3 Using Python websockets provides a better experience than other websockets such as C++, probably because of its simpler language style. Though I haven’t learned Python before, I could learn to use its websockets in a short period of time. 

4.4 Personally, I think it would be better to have the server poll the sensors rather than letting the sensors reach out to the server when they have data. Suppose all sensors collect data at the same time, and if they send the data to the server at the same time, the server will probably not be able to handle so much data. So it would be better for the server to tell sensors to transport data one at a time. 

