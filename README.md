<h1>Key Generator</h1>

<h3># A complex 64-digit key generation script.</h3>

# How to use:

To run it with Python, open the console and type the command :
```sh
$ cd ("file path")
```
 Then we type :
```sh
$ python kwc.py
```
<p>into the console. The script will create a file with .txt extension and write your 64 digit key to it.</p>

<p>Every time you run the script, 1 other key will be written on the other line of the .txt file.</p>

# Another usage:

<p>If you want, you can compile the python file with pyinstaller and use it this way.</p>

<p>First of all, you need to install pyinstaller on the computer you are using.</p>

<p>To install pyinstaller:</p>

```sh
$ pip install pyinstaller
```
<p>then we need to access the location of the file to be compiled via console</p>

<p>To go to the file location:</p>

```sh
$ cd ("file path")
```
<p>Then we enter the following commands in the pyinstaller tool to compile the file to be compiled:</p>

```sh
$ pyinstaller --onefile --noconsole kwc.py
```
<p>After the compilation process is finished, run the .exe file in the folder named "Dist" and your key will be in the resulting .txt file.</p>

# Sample Keys

* [Click to see generated sample keys.](https://github.com/NSIS-arch/KWC/blob/main/Sample_Keys/Sample_Keys.txt)

# Libraries required for use and compiling:

* `string` :
(It comes by default in Python)
#
* `random` :
(It comes by default in Python)
#
