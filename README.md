# Some python scripts for [Notepad++](https://notepad-plus-plus.org/).

* [Full-width ⇔ Half-width](#zen-han)
* [Sort json or yaml file by keys](#sortjsonyaml)
* [Copy Files](#copyfiles)

## Before using these scripts

Install the plugin of [Python Script](https://github.com/bruderstein/PythonScript) in [Notepad++](https://npp-user-manual.org/docs/plugins/).

## zen-han

### Full-width ⇔ Half-width  

This is a python script to convert Japanese characters for [Notepad++](https://notepad-plus-plus.org/).  

### Main features

* Convert full-width characters to half-width
* Convert half-width characters to full-width
* Convert full-width katakana characters to hiragana
* Convert hiragana characters to full-width katakana

### Installation

Just copy `zen-han` folder to the scripts' folder. For example:  
  `C:\notepad++\plugins\Config\PythonScript\scripts`

### Usage

1. Select the characters you want to do the convertion.
2. Click the convertion's menu in `Plugins -> Python Script -> Scripts -> zen-han`  
![Plugins Menu](./menu.png)

### Description of scripts

* \_\_init\_\_  
  `The file which make the directory to a python package`
* Han2Zen  
  `Convert all half-width characters in selection to full-width`
* Han2ZenAns  
  `Convert half-width characters of alphabet, number, sign in selection to full-width`
* Han2ZenKana  
  `Convert half-width characters of katakana in selection to full-width`
* Hira2Kana  
  `Convert hiragana characters in selection to full-width katakana`
* Kana2Hira  
  `Convert full-width katakana characters in selection to hiragana`
* Zen2Han  
  `Convert all full-width characters in selection to half-width`
* Zen2HanAns  
  `Convert full-width characters of alphabet, number, sign in selection to half-width`
* Zen2HanKana  
  `Convert full-width characters of katakana in selection to half-width`
* ZenkakuHankaku  
  `The main library`

## sortjsonyaml

### Sort json or yaml file by keys

This is a python script to sort json or yaml file by keys

### Installation

1. Download souce code of [PyYAML 5.4.1](https://pypi.org/project/PyYAML/5.4.1/#files)
  (Target file: PyYAML-5.4.1.tar.gz).
2. Extract folder `PyYAML-5.4.1\lib\yaml` from the downloaded file into the lib folder of notepad++. For example:
  `C:\notepad++\plugins\PythonScript\lib`
3. Copy `SortJsonYaml.py` file to the scripts' folder. For example:  
  `C:\notepad++\plugins\Config\PythonScript\scripts`

### Usage

1. Open the target file
2. Click the menu `Plugins -> Python Script -> Scripts -> SortJsonYaml`

## copyfiles

### Copy Files

This is a python script to copy files from a directory to another directory for [Notepad++](https://notepad-plus-plus.org/).  

### Installation

Just copy `CopyFiles.py` file to the scripts' folder. For example:  
  `C:\notepad++\plugins\Config\PythonScript\scripts`

### Usage

1. List up all the target files in the editor
2. Click the menu `Plugins -> Python Script -> Scripts -> CopyFiles`

## License

This script is available under the
[MIT license](https://opensource.org/licenses/MIT).
