# Team Pixel -> Pixelated

***Note - I have made this repo opensource but have removed some of my secret weapons to not give the BattleSnake2020 competitors a leg up*** :smiley:

[Here is a write up](https://ntmk.ca/blog/battlesnake2019/) of my journey to BattleSnake 2019.
[Some implementation details / ideas](https://ntmk.ca/blog/battlesnake2019-part-2/) can be found here. 

***Note - I was also in the process of switching to oop so the code is sparatic as its an unfinished process***

A [Battlesnake AI](https://play.battlesnake.io/) written in Python. 

Visit [https://github.com/battlesnakeio/community/blob/master/starter-snakes.md](https://docs.battlesnake.io/) for API documentation and instructions for running your AI.

***WARNING - As of January 2020 python 2.7 is being deprecated. Pixleated was written with 2.7 so an upgrade will be required or bad things could happed.***

#### You will need...

* a working Python 2.7 development environment ([getting started guide](http://hackercodex.com/guide/python-development-environment-on-mac-osx/))
* experience [deploying Python apps to Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
* [pip](https://pip.pypa.io/en/latest/installing.html) to install Python dependencies

## Resources used
[Amits A* Pages](http://theory.stanford.edu/~amitp/GameProgramming/)    
[Noahs BattleSnake](https://github.com/noahspriggs/battlesnake-python)    
[Python A* Ppathfinding (binary heap)](http://code.activestate.com/recipes/578919-python-a-pathfinding-with-binary-heap/)    
[BattleSnake Docs](https://docs.battlesnake.io/)

## Running the Snake Locally

~1) [Fork this repo](https://github.com/battlesnakeio/starter-snake-python/fork).~

~2) Clone repo to your development environment:~
```
~git clone git@github.com:<your github username>/starter-snake-python.git~
```

3) Install dependencies using [pip](https://pip.pypa.io/en/latest/installing.html):
```
pip install -r requirements.txt
```

4) Run local server:
```
python app/main.py
```

5) Test your snake by sending a curl to the running snake
```
curl -XPOST -H 'Content-Type: application/json' -d '{ "hello": "world"}' http://localhost:8080/start
```

## Deploying to Heroku

~1) Create a new Heroku app:~
```
~heroku create [APP_NAME]~
```

2) Deploy code to Heroku servers:
```
git push heroku master
```

3) Open Heroku app in browser:
```
heroku open
```
or visit [http://APP_NAME.herokuapp.com](http://APP_NAME.herokuapp.com).

## Deploying to Heroku

1) View server logs with the `heroku logs` command:
```
heroku logs --tail
heroku logs -n 500 <- can be any value to display logs 
```

2) Output to file and console command:
```
python app/main.py | tee output.txt
```
