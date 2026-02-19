Assignment 3 - Replicating a Classic Experiment  
===
02/20/2026

Link to gh-pages: [https://danlm8.github.io/a3-experiment/]

Finding the Mean: Are horizontal barcharts, vertical barcharts, or pie charts easier for humans to find the median data point?
Written By: Skyler Dooley & Daniel Mastrobuono
--

HYPOTHESIS
Our hypothesis is that people will prefer horizontal bar charts when attempting to determine the median value. 

Note: To run experiment webpage locally, use the command ```node server.js ``` (make sure to run dataGen.py to generate charts first)

![experiment bar](/img/experimentbar.PNG)
![experiment pie](/img/experimentpie.PNG)
![experimentbar2](/img/experimentbar2.PNG)


# Description of Experiment
We wanted to test if horizontal barcharts, vertical barcharts, or pie charts are easier for humans to find the median data point. Our hypothesis is that people will prefer horizontal bar charts when attempting to determine the median value simply because horizontal barcharts are one of the more common ways to relay information. This experiment consisted of 3 graph types, 20 randomly generated versions of each graph (60 graphs total), and 10 participants. Each participant was asked the question "Select the bar/slice you believe to be the median" for each of the 60 charts, and each participant were given the same 60 charts. After each participant completed all 60 trials, a csv file was automatically downloaded onto the local computer which we were then able to add back into the source folder. From there we were able to gather all the outputs from the trials into one master csv file and calculate the error. 

Rankings: 
1. Horizontal Bar Chart with a 2.55 avg error
2. Pie Chart with a 2.69 avg error
3. Vertical Bar Chart with a 2.73 avg error

We calculated the error value using Cleveland and McGill's log2 function. From this, we can see some interesting results. Our hypothesis was correct, the horizontal bar charts are easier to find the median on. However, we were incredibly surprised to see that the vertical bar chart had the most error, while the pie chart was slightly better. Vertical bar charts are probably the most common type of chart used in most industries, so it's shocking to see that it isn't all that great at displaying the values in between the highest and the lowest. It would seem that when one is trying to display any data where seeing the median may be important, they should use a horizontal bar chart. 

<img width="1299" height="820" alt="image" src="https://github.com/user-attachments/assets/1a31a305-c270-45e0-b748-eac48c5f288a" />

# Technical Achievements
To run this experiment, we choose to host the webpage where the experiments were done on a local server to allow for us to be able to run the trials quickly and without the need of a database. This was not a requirement by the project guidelines but it allowed for us to spend less time coding a complex webpage/database and more time running the experiment and gathering data. 

To generate the 60 charts, we wrote python code, ``` dataGen.py ```, that outputs a json file containing chart id, chart type, color of the chart (which was lightgray for all), data points, and the median value (or true-percent). Then in ```index.html```, we used d3 to read from the json file and created the charts, along with the other elements of the webpage itself (title, automatic save to csv function, mouseclicks). 

To combine all the csv files from the trials, we wrote two more python files, ```combine_csvs.py``` and ```get_error.py```, which combine the csvs into a master file and then calculates the error values for each row. We found that this was the quickest and easiest way to combine the files and get the error values without having to manually copy/paste the contents of each file into a new spreadsheet.
