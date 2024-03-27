
# Python Package Exercise
[![Upload Python Package](https://github.com/software-students-spring2024/3-python-package-exercise-team-mskv/actions/workflows/python-publish.yml/badge.svg?branch=main&event=release)](https://github.com/software-students-spring2024/3-python-package-exercise-team-mskv/actions/workflows/python-publish.yml)

[Link to package](https://pypi.org/project/mksv-miniGame)

## Team Members

[Linkun Wan](https://github.com/KKun117)
[Marcus Du](https://github.com/Quadram13)
[Vanessa Viglucci](https://github.com/VanessaViglucci)
[Sara Gizabi](https://github.com/saragizabi)



## Package Info

This package is a set of 4 minigames that can be run from the main function or included individually in whatever code you choose.

The following code can be used by replacing the placeholder with the specific game of your choosing. The four functions are run_space_game(), run_count_game(), run_rps_game(), run_tic_tac_toe()

```
from . import space_invaders as spacegame
        spacegame.run_space_game()
```

Otherwise, the game hub can be run from the command line by running the __main__.py file.


## Working with the package
Please feel free to clone this repository from github or install this package from Pypi. All links are at the top of the page. 

We recommened using a virtual environment when handling this package, whether you are contributing or simply making use of the minigames.

First ensure that pipenv is installed, then create a virtual environment by entering `pipenv shell`

To install the package, enter `pipenv install -i https://pypi.org/project/mksv-miniGame==0.1.7`

Then you can run the package from the command line: python3 -m minigame. This will run the code in the __main__.py file.
