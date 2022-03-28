# FileAutomation
## This is the file automation GUI project written in python
<h3>Purpose:</h3> The main purpose of this app is to search for the required files and merge their contents into a single file.<br><br>

![image](https://user-images.githubusercontent.com/50429258/160341639-817b0ec1-393a-4118-af62-02009adb561c.png)

## Once all the details are filled, just press enter, and let the program search for all the files which matches your search.

![image](https://user-images.githubusercontent.com/50429258/160341946-5451cfbb-7aec-448a-aa71-84482da0be24.png)

Once you press Enter, it will look in the F:\ drive for all the .txt files having abc in them...<br><br>
### Once the search is completed, it will prompt the results window:
![image](https://user-images.githubusercontent.com/50429258/160342536-c330988f-defa-43f9-97a2-cc07a704eb44.png)

As you can see, it could found 2 .txt files in F:\ having abc in them.

- Now, you can click the merge all butoon on the top to merge these files content into a single file.
- As soon as you click the merge all button, a new window pops up:
![image](https://user-images.githubusercontent.com/50429258/160343252-77b56a69-8e0e-4731-b24f-8fb88c6fa68d.png)
- This window asks you for the file extension by which you want to save the file
- And the name of the file.
- Once you filled both, just press enter, and you get the following output:
![image](https://user-images.githubusercontent.com/50429258/160343538-15fab078-c988-4078-96f8-3313f69d0200.png)

- You get the option to open the file right away by just clicking the open button.
- After clicking the Open button, merged.txt will open:
![image](https://user-images.githubusercontent.com/50429258/160343840-ea59c245-5b27-4db9-933c-820bf4be926a.png)

- We can see that abc.txt was empty, that's why no content is shown.
- abcd.txt had some content, which you can see in the abcd.txt portion of merged.txt file. 

### NOTE: The application generates the log files in the folder in  which the application is placed. You can see those log files to check for any rejected files or any other events if you think something unexpected has happened!
### For each instance, the application generates a new log file in a dedicated folder, which the application takes care of by itself.
