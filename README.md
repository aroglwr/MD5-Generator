# MD5 Generator
<p align="center">
  <img src="./icon.png" />
</p>

## What is this?
This is a simple command line program that generates and outputs a file containing MD5 hashes for a supplied file. It supports single files or folders containing files using `-f`. It will not search subfolders.

## Usage
Run `md5-generator.exe FILENAME` where `FILENAME` contains the directory path.

### Optional Parameters
* `-o` - Output folder
* `-n` - Output filename
* `-f` - Is a folder (no argument)
* `-j` - Outputs as json file (no argument)

## Building
Built using [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) and does not contain any external packages.

## License
This program is licensed under the MIT License.
