[](#expresso)
# Expresso

![I Am Resposive Screenshot](pointofsale/static/img/amiresponsive.png)

Say hello to Expresso, a card based point of sale system designed to run from your smartphone. Users can create, edit and delete the Menu, Sub-menu and Item categories to build an app that best suits their needs. Build and edit an order, confirm payment and save the day's transaction data for export via email at the end of the day as a .csv file.

## Table Of Contents

- [Introduction](#introduction)
- [The Initial Idea](#the-initial-idea)
- [Technologies](#technologies)
- [Building And Testing ](#testing)
- [Bugs And Fixes](#bugs-and-fixes)

-




## Introduction

Expresso is a mobile friendly way to track your sales throughout the day. Featuring a responsive design that looks great on phone, tablet or desktop. Fully customisable to match the needs of the user.

## The Initial Idea

The idea for Expresso cam from several areas. First and foremost from my experience of being front of house in a small independent
cafe in a nearby town and using a point of sale system. Secondly from browsing the market stalls that appear every weekend just opposite my place of work, and talking to stall owners. Lastly from chatting with my work colleagues and listening to their views and opinions about interacting with a till.

I have a banking app that allows me to take payments via Apple or Google Pay using my phone as the terminal. This is enabled by Stripe and removes the need for any integrated payment software. By combining this payment functionality with a flexible point of sale system you can effectively manage a small shop, a market stall, a popup stall or even a carboot sale. The data from the app can be exported as a .csv file meaning that you could upload the data into a suitable accounting app and manage your whole business with nothing more than a smartphone.

[View the deployed app here](https://mp3-pointofsale-4872260bbf57.herokuapp.com/)

[Back to the top](#expresso)

## Technologies

Here are the main technolgies used for the project.

- [HTML5](https://html.com/)
- [Bootstrap5.3.2 - CSS and Javascript library.](https://getbootstrap.com/)
- [FontAwesome5.15.3 - Icons.](https://fontawesome.com/?utm_source=font_awesome_homepage&utm_medium=display&utm_campaign=fa5_released&utm_content=auto_modal)
- [Heroku - Platform used for deployment.](https://www.heroku.com/home)
- [Flask - Python web framework.](https://flask.palletsprojects.com/en/3.0.x/)
- [Jinja2 - Template engine.](https://jinja.palletsprojects.com/en/3.0.x/templates/)
- [A more complete list can be  found here, requirements.txt](requirements.txt)


[Back to the top](#expresso)

## Testing

Manual testing was selected as the best way to check the app as a modular approach to the build meant that each part
could be tested as the code was assembled and many of the bugs fixed before final testing.

### Test 1: base.html renders the startscreen and navbar shows correct links.

- Expected:   That base.html template renders the startscreen with a header, footer and placeholder text. Navbar displays 
            the correct links.
- Testing:    App was launched with run.py.
- Result:     The startscreen rendered correctly with all elements displaying correctly. Decided to change navbar link names.
- Fix:        Change names of navbar links to better reflect the app. Test passed.

### Test 2: addition of Menu options incl. add, edit and delete and mainscreen.html displays all menus.

- Expected:   That a menu could be added and displayed, edit, delete and sub-menu buttons would display correctly.
- Testing:    The app was launched with run.py
- Result:     A menu was added and displayed correctly. edit, delete and sub-menu buttons displayed correctly.
- Fix:        No fix required. Test passed.

Once these two initial tests had been successfully completed the 'Menu' code was repurposed for the sub menus and added to the build

### Test 3: addition of Submenu options incl. add, edit and delete and view_submenus.html displays all submenus.

- Expected:   That a submenu could be added and displayed, edit, delete and item buttons would display correctly.
- Testing:    The app was launched with run.py
- Result:     A submenu was added and displayed correctly. edit, delete and item buttons displayed correctly.
- Fix:        No fix required. Test passed.

With the code now allowing menus and submenus to be added correctly the 'Sub-Menu' code was repurposed for items and added to the build.

### Test 4: addition of Item options incl. add, edit and delete and view_items.html displays all items.

- Expected:   That an item could be added and displayed, edit, delete and add to order buttons would display correctly.
- Testing:    The app was launched with run.py
- Result:     An item was added and displayed correctly. edit, delete and add to order buttons displayed correctly.
- Fix:        No fix required. Test passed.

At this point the basic card structure was in place and the testing continued with the addition of edit and delete functionality.

### Test 5: checking the routing and adding in edit and delete functions.

- Expected:   That edit/delete works as expected
- Testing:    The app was launched with run.py. The PostgreSQL database was monitored using SQL shell in Windows 11 submenus and 
              items were added, edited and deleted
- Result:     Issues with passing of variables to identify which menu/sumenu/item needed editing/deleting. Some styling issues when presenting 
              Bootstrap cards.
- Fix:        Routing issues were fixed by passing the relevant identifiers into the necessary app routes in routes.py file. Bootstrap classes adjusted to improve
              consistency of look across different screens. Test passed.

With the app now up and running the 'Order' screen was coded allowing items to be added to the current order. A 'paid' button, displaying the current order total, moves details about this order to the transactions list and clears the screen ready for the next order.

### Test6: adding to an order and then posting this to transactions.

- Expected:   That an order can be created by adding items to the order and then viewed in the 'Order' tab of the navbar. That the paid option button displays and shows
              the correct order total in the correct format and moves the order to transactions.               
- Testing:    The app was launched with run.py. The PostgreSQL database was monitored using SQL shell in Windows 11. An order was created and then the 'paid' option clicked. The
              PostgreSQL database was checked to verify that the correct actions had happened as expected.
- Result:     Issues with passing of variables to identify which menu/sumenu/item needed editing/deleting. Some styling issues when presenting 
              Bootstrap cards.
- Fix:        Routing issues were fixed by passing the relevant identifiers into the necessary app routes in routes.py file. A global variable used in calculating the total order price
              was removed by making the total price calculation a function. PostgreSQL was confirmed to have updated correctly. Bootstrap classes adjusted to improve consistency of look across different screens. Test passed.

The final part of the build was to add in the ability to email a.csv file containing the days transactions to a nominated email address.

### Test7: email a .csv file to an email address.

- Expected:   That when selected an email address could be input and a .csv file containing data about the day's sales could be sent to the email address. That the transactions list would
              clear after the email was sent.                    
- Testing:    The app was launched with run.py. The PostgreSQL database was monitored using SQL shell in Windows 11. An order was created and then the 'paid' option clicked. The
              PostgreSQL database was checked to verify that the correct actions had happened as expected. Then from the 'Sales' screen the 'send email; option was selected. An email address 
              was input and 'send' selected.
- Result:     Email address defaulted to 'gavin.brown@4uxdesign.com' which was a placeholder address needed for the routing. The input email address was ignored.
- Fix:        The issue was identified as a form issue. When inputting an email address the form value had been set to the placeholder email address. Once this was removed the email correctly 
              sent. 

With the basic design and functionality now in place testing could begin for browser, device and Google Lighthouse.

### Browser Tests: the browsers used.

The app was tested on Google Chrome Version 122.0.6261.112 (Official Build) (64-bit), Mozilla Firefox 123.0.1 (64-bit), Microsoft Edge Version 122.0.2365.80 (Official build) (64-bit), Safari, mobile Safari on Apple iPhone 14 running iOS 17.4 and Safari on Apple iPad running iOS 17.4. Google Chrome developer tools were also used to try various different devices/screen resolutions. The app proved to be responsive, scaling correctly across different resolutions with no apparent display issues. All functionality was maintained and the test was considered successful.

[Back to the top of testing](#testing)

[Back to the top](#expresso)



