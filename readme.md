# Android Layout Analyser

---

## ➡️ Description

This Python script will provide following insights for an Android project.

- Which ViewGroups and Views are used for creating layout files.
- How many times each ViewGroup or View is used. For example, it will tell you that you have used ConstraintLayout 120 times in whole project.

## ➡️ Requirements

1. Python3
2. BeautifulTable (To print data in result file) ([https://github.com/pri22296/beautifultable](https://github.com/pri22296/beautifultable))

## ➡️ How to use?

1. Install required dependencies.
2. Open terminal and execute `python3 layout_analyser.py`
3. When asked for project path, enter full path of an Android project
Example: `/Users/sample_user/Desktop/projects/android_workspace/first_app` 
4. It will print the result in terminal and create `result.txt`