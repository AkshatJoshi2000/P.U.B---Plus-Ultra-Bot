<h1 align="left">P.U.B - PLUS ULTRA BOT</h1>

<div align="center">
  
  <h3 align="center">
    <img src="Assets/Plus Ultra Bot.png" alt="PLUS ULTRA" width = 400px, height = 250px></a><br>
    <br>
   <p align="center" ><ins><strong>P.U.B</strong> <em>- A modern day multi-purpose discord bot.</em></ins></p>
  </h3>

 
  ![GitHub repo size](https://img.shields.io/github/repo-size/AkshatJoshi2000/P.U.B---Plus-Ultra-Bot)
  ![GitHub](https://img.shields.io/github/license/AkshatJoshi2000/P.U.B---Plus-Ultra-Bot)
  ![PyPI](https://img.shields.io/pypi/v/selenium?color=%09&label=selenium&style=flat-square)
  ![GitHub top language](https://img.shields.io/github/languages/top/AkshatJoshi2000/P.U.B---Plus-Ultra-Bot)
  ![GitHub last commit](https://img.shields.io/github/last-commit/AkshatJoshi2000/P.U.B---Plus-Ultra-Bot)
  ![GitHub contributors](https://img.shields.io/github/contributors/AkshatJoshi2000/P.U.B---Plus-Ultra-Bot)
  

  <h5 align = "left">Plus Ultra Bot (P.U.B) is a next-generation fully featured multi-purpose discord bot which aims to cover the small aspects, thus making hanging out with friends and family more convenient and fun.
</h5>
</div>

## Features
<strong>P.U.B</strong> builds on the well established usability  of `discord.py`, and gives you:

* An inbuilt music bot, which gets your favourite music to you.

  <img src="Assets/local train song play.png" alt="PLUS ULTRA"></a><br>
   

  | Flag          | Description                         | Usage                      |
  |---------------|-------------------------------------|----------------------------|
  | /join         | Adds the bot to the voice channel   | pub/join                   |
  | /play         | Plays and add new songs to the queue| pub/play <name of the song>|
  | /queu         | Shows the queue                     | pub/queue                  |
  |/song-info     | Returns info regarding the song     | pub/song-info              |
  
* A reaction reply gif, `pub/g  <gif action> <member>` (member is optional)
* Random anime nickname - a random anime nickname will be assigned to every new member when they will join the server. 

## Endpoints

```sh
pub/help
```

This will display help for the tool. Here are all the endpoints it supports.

| Flag                    | Description                                             | Usage                                              |
|-------------------------|---------------------------------------------------------|----------------------------------------------------|
| /help                   | Gives a bot endpoints                                   | pub/help                                           |
| /news                   | Returns headlines regarding the input subject          | pub/news <subject>                                 |
| /weather                | Returns weather info of the input city                  | pub/weather <city> <country>                       |
| /roll                   | Rolls a dice                                            | pub/roll                                           |
| /toss                   | Tosses a coin                                           | puebab/toss                                        |
| /remmin                 | Sets a reminder (in mins)                               | pub/remmin <time in mins> <text>                   |
| /remhr                  | Sets a reminder (in hrs)                                | pub/remhr <time in hr> <text>                      |
| /cprice                 | Prints info regarding the input cryptocurrency          | pub/cprice <cryptocurrency>                        |
| /g                      | Retuns a gif based on the input action                  | pub/g <gif action> <member> (member is optional)   |
| /meaning                | Gives the mening of the input word                      | pub/meaning <word>                                 |
| /words                  | Gives a random quote                                    | pub/words                                          |
| /movie                  | Returns general info regarding the movie                | pub/movie <movie's name>                           |
| /delete                 | Deletes the last test                                   | pub/delete                                         |
| /wiki                   | Gives wiki summary of the input subject                 | pub/wiki <subject>                                 |
| /fb                     | Returns soccer updates                                  | pub/fb <team 1> <team 2>                           |
| /cric                   | Return cricket updates                                  | pub/cric <team 1> <team 2> (optional)              |
| /creepy                 | Fetched you a random creepy story                       | pub/creepy                                         |
| /animetoday             | Returns a random anime with synopsis                    | pub/animetoday                                     |

<div>
  
## Examples

#### Weather
```sh
   pub/weather shibuya japan
 ```
<img src="Assets/Shibuya_weather.png" alt="PLUS ULTRA" width = 250px, height = 220px></a>


```sh
   pub/weather "san isidro" peru  #City name consisting of more than one word must me written in-between ""             
 ```
<img src="Assets/san_isidro.png" alt="PLUS ULTRA" width = 205px, height = 200px></a>

#### GIF
```sh
   pub/g slap @member  #Can also be used without providing the the member argument           
 ```
 <img src="Assets/gif.png" alt="PLUS ULTRA" width = 270px, height = 240px></a>
</div>

#### Cricket Score
```sh
   pub/cric csk mi           
 ```
 <p>When the name of both the teams are passed as a parameter, the match summary of their previous match and the date of their next match is displayed</p>
 <img src="Assets/csk vs mi (parameter).png" alt="PLUS ULTRA"></a>
 
 
 ```sh
   pub/cric           
 ```
 <p>When nothing is passed as a parameter, the bot will return the latest score feed regarding cricket</p>
 <img src="Assets/no parameter cric.png" alt="PLUS ULTRA"></a>
 
#### Dictionary
 ```sh
   pub/meaning anemoia          
 ```
 <img src="Assets/meaning.png" alt="PLUS ULTRA"></a>


## Contributing to P.U.B

* Report bugs, mising best practices.
* Help fixing in bugs.
* Follow the code structure.
* Make sure that your changes do not conflict with the core files.
* Submit pull requests.

## Licence
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
