# Test-case-generator  
#### Generate test cases for Competitive Coding.  
### Instructions:  
* Download Zip file [here](https://github.com/Tanmay-901/Important-details/raw/master/test_case.zip) and then extract 
the file, open dist folder, and then run test_case.exe(keep all the files at same location)
* For more convinience,
  1. right click on 'test_case.exe' after extraction.
  2. click on `pin to start`.
  3. Now the tool's icon is pinned to your start menu and can be used directly from there which saves the hussle of going 
    inside the `dist` folder everytime you want to run the tool.

## To be kept in mind:
* This is a **plug'n'play** tool i.e. no installation is required
* There could be a case when your web browser or windows defender shows a warning regarding security issue or virus
detected and in that case, you would either have to pause your antivirus and/or windows defender for the time being before downloading(can be resumed
right after downloading completes).
* If the pc shows a warning similar to this "Operation did not complete because the file contains a virus or unwanted file", it is 
probably due to an issue with **py2exe** and **pyinstaller** which are used to convert the python program into an executable file. It can be overcome by 
allowing "insatallation from unknown sources" and setting it up as "Ask always" under the privacy settings.  

------------------------
## About Project  
* This project is a combined application of **Object Oriented Programming, Competitive coding and Tkinter toolkit**.  
* I got the motivation to develop this project after I begun my competitive programming journey(not a great one yet though but working my way up gradually), 
there were many times when I saw people(including me and my friends) stuck on trying to struggle in thinking test cases when their program 
fails the submission, especially the case with beginners and that is the main reason this project is developed.
* However, it is not advised to directly use this tool everytime without trying and thinking test cases on your own, but 
treat it like a hint to a problem, you should try to solve the problem first before looking up the hint and if you're unable to get ahead 
then it is advisable to go for the hint instead of just wasting more time. Treat this tool similarly.  
  
## Home Page: 
> Click on the desired type of Test Case.  
  
![Home Page](https://github.com/Tanmay-901/test-case-generator/blob/master/Images/Home.png)
## Input Screen  
> Enter the constraints here  
Make sure that none of the constraints is having **values more than 10<sup>7</sup> and T*maximum_value_of_n/m/k <=10<sup>7</sup>**   
> This limit is applied because Outputs are in the form of arrays, and any array having size more than that would completely use up memory of
> a standard PC and would cause it to hang. This issue is under consideration and would be soon dealt with.  
  
![Input Screen](https://github.com/Tanmay-901/test-case-generator/blob/master/Images/Input_screen.png)  
## Output Screen  
> Finally Output is shown.  
  
![Output Screen](https://github.com/Tanmay-901/test-case-generator/blob/master/Images/Output_screen.png)  
  
On the output screen you can use multiple handy features as well like **_copy, regenerate new test case, change constraints_**
on single click.

------------------------
## Pre-requisites:  
* To use codes apart from first release, 'tkinter' must be installed.  
------------------------
## Challenges faced:  
| S.N. | Issue | Solution/proposed Solution |Resolved or not |
|:-----| :----- | :--------------- | :------------- |
| 1.   | Application window appeared different on windows and Linux based system  | Manually designed the GUI similar to the Linux one| :heavy_check_mark: |
| 2.   | PC freezed when input constraints were too big | Set lower and upper limit for constraints | :heavy_check_mark: |
| 3.   | Working on big input values | split the test case in two or more parts and then concatenate them as strings to generate on large constraints | :x: |
| 4.   | Windows defender/Antivirus/Chrome virus check treated the file as malicious and blocked download | Used py2exe instead of pyinstaller and uploaded zip of multiple files instead of `--onefile` | :heavy_check_mark: |
| 5.   | Code became Surprisingly long| Converted whole program from simple functions and methods to OOPs | :heavy_check_mark: |

------------------------
## Journey of Development of this project:  
* I learned Tkinter a whole lot better while building this project compared to when I just learned and copy pasted code from tutorial.
* Before this project, All I knew about OOPs was its definition, types and example and used them only for exam and interview purpose but with 
this project I have used them a lot thoroghly now and now undderstand every bit of what I earlier used to mug up. while developing this 
project I faced an unforeseen issue of working on a very very long code. In the starting phase when the program was all
commands, functions and methods, **the code was more than 1500 lines for just 5 types of test cases** and that too without other additional features 
(like copy, regenerate, change constraints and others).
* It started to be really inconvinient for me to traverse in that program from top to bottom every 5 minutes and it took a lot of time just
to find what i was searching for to work upon. Then I thought of trying OOPs- Inheritance and Abstraction, because there were things which 
seemed like a little bit common for most of the test cases although it cost me a few more days just to get it done (change whole code in 
classes and methods), the code started to **optimise and its length reduced drastically and within a week the program was less than 
half(600 lines approx) of what it was** and that too with those additional buttons and features which currently are present.  


------------------------
## Updates:
* Support for Test cases for larger constraint values is being worked upon.
* New test case types are being added continuously.
