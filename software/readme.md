# Updating your Raspi OS

Install the most recent version of Raspi OS. Update it with the following commands:

```
sudo apt update -y
```

```
sudo apt full-upgrade -y
```

Install required libralies with the following commands:

```
sudo apt install libgraphicsmagick++-dev -y
```
```
sudo apt install libwebp-dev -y
```
```
sudo apt install python3-dev -y
```
```
sudo apt install python3-pillow -y
```

# Installing rpi-rgb-led-matrix

Install [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) with the following commands:

```
cd
```
```
git clone https://github.com/hzeller/rpi-rgb-led-matrix/
```

```
cd rpi-rgb-led-matrix
```
```
make
```

# Testing your LED Matrix board

Test your LED board with the following command:

```
sudo ./examples-api-use/demo -D 0 --led-no-hardware-pulse --led-cols 64 --led-rows 64
```

Replace "--led-rows 64" with "--led-rows 32" if you are using a 64x32 LED board.

You can see a colorful square revolve on your LED board if everything goes well. Do "Ctrl-C" to stop it.

<p align="center">
  <img src="../images/demo0.jpg" width="350" />
</p>


# Making and Running Python Apps
