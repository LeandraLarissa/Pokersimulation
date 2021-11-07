# Pokersimulation
The code provided on this site is a Poker simulation. Two poker strategies are compared with each other in a model of Poker.

## Description

The 4 simulations provided differ in some settings but they share the same rough structure. It is especially recomended to have a look into the first and fourth simulation since there are the most differences.
Further, there is code provided on which the final simulations are based on. The other codes sort to say document the steps made until the simulation was ready to be used.
And finally there is some data provided which was produced with these simulations.
Briefly this site includes:
* The simulations 1 to 4
* Codes which were the steps made to finally have the simulation
* Data produced with the simulations
## Getting Started

### Dependencies
There are no further extentions used. So, the code can be copied and directy be used.
The code was written on the application Visual Studio codes but other applications can for sure be used too.

### Orientation
The code of the simulations is structured in:
* Defining the starting hand categories and further lists
* The main loop repeats how often the players start with a new stack
* In the loop the strategies of the players are defined and how the blinds are raised
* Then there are three while loops: The first is while both have enough chips to pay the blinds. The second and third is while one of the players has enough money to pay the blinds. This was initially intended to be made more elegantly but there was no method to make a list of variables sufficient for these pruposes. Otherwise it would probably be possible in one while loop and it would be easy to spot more than two players.
* After these while loops there are two lists (completedround, completedround2) which collect the number of rounds the players achieved.

## Getting Data
There are several ways to receive data: probably the most elegant way would be to plot the data received directly in the code. 
But in this code the data is finally ploted in an other application. Therefore, there were ways used to convert the data in the most handy way.
### Histogram
If it is intended to make a high number of repetitions it makes sense to convert the data in a compact way:

The following code is to be inserted after the main loop. This code uses the list of the rounds the players made and counts how often a specific number of rounds was achieved.
The range [1,50] is taken because it is assumed that it is impossible to achieve more than 50 rounds.
```
for i in range (1,51):
    print(completedround.count(i),completedround2.count(i))

```
The values received can then be ploted into a bar-diagram

### Boxplot
For a Boxplot the raw data is necessary. Therefore the rounds of the players are simply printed into the console.
One value after the other is printed since this is the most handy form to be converted into graphs.
```
for i in range (1000):
    print (completedround[i], completedround2[i])
```
The range corresponds to the repetitions made in the main loop. If there are uncertainties len(completedround) can be used as a range too.

## Author

ex. Leandra

## Acknowledgments

For the structure of the 'readMe'
* [Dominique Pizzie](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
