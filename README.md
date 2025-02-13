# py-asteroids

A Python version of the classic arcade game [Asteroids](https://www.youtube.com/watch?v=cZfsnA7dAHI), originally developed and published by Atari in 1979. The game was designed by Lyle Rains and Ed Logg.
This Python implementation is inspired by [Boot.dev](https://github.com/bootdotdev).

## Requirements

Ensure that Python is installed on your system. You can check your installed version with:

```
python --version
```

If you need to install Python, [download the latest version](https://www.python.org/downloads/).

Additionally, make sure `/usr/local/bin` is included in your system’s `$PATH`. Check by running:

```
echo $PATH | grep /usr/local/bin
```

If it’s missing, add it to your shell configuration:

- For Linux (Bash):

```
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

- For macOS (Zsh):

```
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

# Installation

Clone the repository and build the project using make:

```
git clone https://github.com/alnah/py-asteroids.git
cd py-asteroids
sudo make
```

# Usage

Run the game with:

```
asteroids
```

# Control

Use the following controls to play the game:

- Space: Shoot
- Up: Move Up
- Down: Move Down
- Left: Rotate Left
- Right: Rotate Right
