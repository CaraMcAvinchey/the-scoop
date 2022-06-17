# THE SCOOP

The Scoop is a Python terminal application which runs in the Code Institute mock terminal on Heroku.

<img width="980" alt="image" src="https://user-images.githubusercontent.com/97494262/173846607-830a7f65-fe86-43fb-a168-2d639c01cafb.png">

## Author
Cara McAvinchey

## Project Overview
*  The Scoop is an app built for an ice cream truck so that customers can easily place an order and collect their items with an order number. The business owner will be able to see how many orders were made for each scoop type and customers can see how much their order will be at the end of the process.

You can view the deployed website [here](https://the-scoop-icecream.herokuapp.com/)

## Table of Contents
XX

## The Scoop: Steps to Use
* First the customer is welcomed to the app and asked for their name. If valid, the customer and make their first order.
![1](https://user-images.githubusercontent.com/97494262/173981166-5e0f66ea-ce4a-4cb9-983e-1e950403529e.gif)

* If their name input is not valid, the customer will get a hint about what is wrong.
![2](https://user-images.githubusercontent.com/97494262/173981316-be2beec0-a8cd-4a7d-9639-2c121b27751a.gif)

* The menu displayed will ask for the number of scoops.
<img width="757" alt="image" src="https://user-images.githubusercontent.com/97494262/173981509-7183c6fb-a425-475b-b6f3-b47175c92636.png">

* The menu will display again if the input is not valid.
![3](https://user-images.githubusercontent.com/97494262/173982886-cc4916bb-15af-434a-8a21-00b400b99904.gif)

* The app will then ask the customer if they'd like to order another ice cream.
<img width="760" alt="image" src="https://user-images.githubusercontent.com/97494262/173982983-d69fb162-3eeb-4d37-b081-725adcbb6fc2.png">

* If no, the customer will receive notice that their order is complete and the price of the order is displayed.
<img width="757" alt="image" src="https://user-images.githubusercontent.com/97494262/174240674-48f7159f-46f2-4182-9fa2-e4c9af4e1010.png">

* The customer can proceed to the collection point to pay and pick up their order according to the number.

## Features

### Implemented Features

* Welcome Function
    - An introduction to the company and the service offered with a friendly hello and welcome. There is no terminal interaction at this point.
 <img width="446" alt="image" src="https://user-images.githubusercontent.com/97494262/174312293-45d3400d-79d3-4e47-9229-db3cdd9f1e0c.png">

* User Information
    - The customer is requested their name and the input will be validated for numbers, characters or single letters.
    - The validate_name function is triggered according to the following if statements:
 <img width="390" alt="image" src="https://user-images.githubusercontent.com/97494262/174313354-704e5151-e354-4d1c-a3f9-288a5e1dc277.png">
 
* Ordering Function
    - The customer will then input their order using numbers. The function will repeat the order again if anything other than the numbers are input.
    
* Reorder Function
    - After each ice cream is ordered, the customer is given the option to order another or continue to the next step.
    <img width="450" alt="image" src="https://user-images.githubusercontent.com/97494262/174314151-96c78add-8570-44ad-b0d7-40b6baf9ac08.png">

* Order Successful
    - The function will add the numbers to an external spreadsheet for the business owner to get total sales orders.

* Print Receipt
    - The customer will see a summary of their order and the final price. The fuction calculates the number of each scoop ordered and outputs the cost.
    <img width="557" alt="image" src="https://user-images.githubusercontent.com/97494262/174318752-b436b7d3-6555-4df6-9b56-ba4ef1edf5d6.png">

* Order Complete
    - The function will generate a random number from 1-100 for the customer to take to the counter and pay/pick up their order when ready.

### Future Features

* For future development, the app could allow for a login/sign up function to collect basic info about The Scoop customer for a possible rewards program e.g for every 5 double scoops, get a single scoop free. (the registration function can be found in the flow chart [here](#design-documents)
* The Scoop is a growing business, as the product offering increases (such as toppings, cone/cup, flavours) these options could be added to the app.
* If the customer makes a mistake, adding the ability to remove an order would improve the user experience.

## Design Documents

The below flowchart maps out the user experience from beginning to end. The registration process is marked off as a future feature and explained in detail [here](#future-features). Due to time constraints and my limited knowledge, I was not able to code this part of the project. 

![icecream-two-three](https://user-images.githubusercontent.com/97494262/174000156-c863418a-35f2-4e94-9420-a844a3d243d8.jpg)

## Data Model/ Classes
In this section write our your data model(s) or classes. 

You might want to include subsections that include how the data in the model is initialized and then the methods that you created to update it through the program.


You can create a table and take a screenshot, or you can write up subsections in markdown:

![image](https://user-images.githubusercontent.com/23039742/130148204-b56406bf-0fff-48f3-9dee-2f3cdbe67cc5.png)

### Class X
To better group the game as an object, I wrote a class representing its properties and had method functions to update those properties: 

**Properties**
- property 1: is a {string} it represents {something} 
- property 2: is a {string} it represents {something} 

**Methods**
- **\_\_init\_\_**: Initialize method, it starts the class off with default parameters as if a user just started to play a game.
- **\_\_str\_\_**: Returns a string representation of the class/object

## Libraries used
* cachetools
    - Python module which provides various memoizing collections and decorators.
    
* google-auth
     - This library simplifies using Google’s various server-to-server authentication mechanisms to access Google APIs.
     
* google-auth-oauthlib
    - This library provides oauthlib integration with google-auth.
    
* gspread
     - Interface for working with Google Sheets.
     
* oauthlib
    - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python 3.6+.
    
* pyasn1
    - Pure-Python implementation of ASN.1 types and DER/BER/CER codecs (X.208)
    
* pyasn1-modules
    - A collection of ASN.1 modules expressed in form of pyasn1 classes. Includes protocols PDUs definition (SNMP, LDAP etc.) and various data structures (X.509, PKCS etc.).
    
* requests-oauthlib
    - Provides first-class OAuth library support for Requests.

* rsa
    - It supports encryption and decryption, signing and verifying signatures, and key generation according to PKCS#1 version 1.5.

## Testing

### Validation Testing
You should try to ensure you code is valid and follows proper indentation.  In this section you should write up any websites you used to validate your code. As your projects becomes more complex these tools may change.

For each python file in your project, run it through the pep8online validator

- [PEP8 Validator](http://pep8online.com/) include a screenshot of results

Note any errors or warnings you are ignoring and why. 

If the line is too long just add 
```$python 
# noqa
```
There is a space before the # and after it to skip the quality assurance for that line.

### Manual Testing
* You can view manual testing of the website [here](https://docs.google.com/spreadsheets/d/1tB4dZcZOXlaUn-47L1OZD27e5xZdzZz8Y1MKFU8m00U/edit?usp=sharing)

### Defects of Note
Some defects are more pesky than others. Highlight 3-5 of the bugs that drove you the most nuts and link to them directly here.

### Outstanding Defects
It's ok to not resolve all the defects you found as long as:
- it does not impacting a user from completing a vital function on the website
- it only affects a very small subset of users
- is an extreme edge case that very few users would try

If you know of something that isn't quite right, create an issue and  link to it here and explain why you chose not to resolve it. 

Sometimes it's as simple, word wrapping issue that makes the site look odd at a certain screensize that you just didn't have time to fix due to the impending deadline and lack of skills. It's best to mention it but note why you allowed it to go live than let asccessors think you didn't notice it.

## Deployment

### Gitpod
Before deploying, the Gitpod workspace needs the following setup steps for Heroku to build the project:

1. Install the dependencies for Heroku using the following instruction to the terminal:
```$python
pip3 freeze > requirements.txt
```
<img width="291" alt="image" src="https://user-images.githubusercontent.com/97494262/174004074-ad7dcaae-25cd-471c-b25a-4f8f0a7fbbbd.png">

2. The project creds.json file from the Google Drive and Google Sheets API access used when adding Config Var, see example below:
<img width="624" alt="Screenshot 2022-06-16 at 14 06 35" src="https://user-images.githubusercontent.com/97494262/174003352-fba526ae-1358-4580-8628-1831d7817df2.png">

### Heroku
This application will be deployed via [Heroku](https://heroku.com)

1. Log into Heroku.

2. Navigate to Dashboard. 

3. Click "New" and select "Create New app" from the drop-down menu. Name the application something unique and select your region.

<img width="1438" alt="3" src="https://user-images.githubusercontent.com/97494262/173860257-49e66c65-cea9-4ff4-9cad-702574c414ea.png">

4. Click "Create App".

5.	Navigate to "Settings" and scroll down to "config vars".

6. Click "Reveal Config Var", in the field key enter CREDS and in the value field copy and paste the contents of creds.json file.

<img width="1438" alt="6" src="https://user-images.githubusercontent.com/97494262/173860589-3fc0684d-c724-43ff-b693-ec757f4035f1.png">

7. Scroll down to "build packs", click "build packs" and then click both "python" and "node.js" ensuring python is first on the list.

<img width="1437" alt="7" src="https://user-images.githubusercontent.com/97494262/173861135-de973726-7024-4a0a-a7cd-bac610d5f766.png">

8. Navigate to the "Deploy" section.

9. Scroll down to "Deployment Method" and select "GitHub".

<img width="1438" alt="9" src="https://user-images.githubusercontent.com/97494262/173861309-776bc0c9-ac55-482b-99db-1a901b6acad1.png">

10. Authorise the connection of Heroku to GitHub.

11. Search for the GitHub repository name to connect with and select it.

12. For Deployment there are two options, automatic deployment or manual. I chose Automatic Deployment so Heroku will re-build each time code is pushed to GitHub.

13. Ensure the correct branch is selected "master/Main", and select the deployment method that you desire.

<img width="1438" alt="13" src="https://user-images.githubusercontent.com/97494262/173861796-8339a390-f449-4d4d-b203-f5b0d33c4924.png">

14. Force the first deployment by clicking 'deploy branch' and wait for the site to build.
15. Ensure the build was successful by checking the overview tab and the activity log should say 'Build succeeded'

<img width="1271" alt="image" src="https://user-images.githubusercontent.com/97494262/173862726-50da81d4-dcf3-489a-9e8b-3b9b8f1db9d3.png">

16. Open the deployed site and check that the program is running.

## Credits

### Acknowledgments

* Code Institute: Love Sandwiches Project
    - [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.
    - Steps to declare and connect the Google APIs to my worksheet.
    - Function to update the worksheet.
    - Steps to deploy the project to Heroku.

* Dog's in the Hood by Obiageli Onyekpe
    - Deployment section steps in README.
    - Libraries section used and descriptions in README.
* Flowchart created using [diagrams.net](https://www.geeksforgeeks.org/python-randint-function/?ref=gcse)
* This [GeeksforGeeks](https://www.geeksforgeeks.org/python-randint-function/?ref=gcse) article assisted with generating a random number for my order function
* Thanks to my mentor, Malia Havlicek for reviewing and giving suggestions on how to improve my project.
* The tutors at Code Institute for their patience and support.
* The Code Institute Slack community for tips and guidance.
