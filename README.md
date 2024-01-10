# ads-retrieval-task

## Task description

This repository contains code for two annotation tasks. <br>

Task 1 is a multiple choice scenario where you will be presented with one ad and one question, and you are requested to choose your aswer among three given options. The samples to annotate are 10. <br>

Task 2, on the other hand, requires you to rate the appropriateness of a statement with respect to an ad. You should express your rating as a percentage, with 0 indicating the lowest appropriateness and 100 the highest. The samples to annotate are 10 ads, but each of them can be associated with 3 different statements so, in practice, you will give 30 ratings and will see the same ad 3 times. 

## Instructions to run the code

To run the annotation interface on your local machine, please first clone this repository and install the necessary depencencies with the command
```
    pip install -r requirements.txt
```

Then, run ```python app.py``` if you would like to start Task1, or ```python app_range.py``` if you prefer to do Task2. In both, cases, you will see an output like the following on your terminal: 
``` 
    * Serving Flask app 'app_range'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 694-371-605
```
Now copy the given URL (in this case, ```http://127.0.0.1:5000``) on your preferred browser and you will be able to see the annotation intrface. <br>

All answers are automatically saved whenever you press the "submit" button, so feel free to pause and resume the task whenever you want. The interface will resume from the last annotated example, so you will not have to redo everything from the beginning if you kill the interface.<br>

When you are finished with the task and wish to close the interface, please do so from the terminal, by pressing ```ctrl+C```. Simply closing your browser window will **not** close the running application. <br>

When you have completed both tasks, please forward to me **both** files present in the ```annotations``` directory. Thank you for your help!





 
