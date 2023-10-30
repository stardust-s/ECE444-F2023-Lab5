# ECE444(2023 Fall) - Lab 5

Assignment Submitted by: Sage Jiang


# Info
this repo is a replay of
https://github.com/mjhea0/flaskr-tdd.



# discussion
## pros and cons of TDD
pros: 
- the tests are basically your requirements, thus you will **always know if you meet the requirement**
- since you write code to fulfill the test, all code will be covered by tests (i.e. **high coverage**), and if something break you will know easily
- it forces you to **write code in a modular way**, where code interact with each other using the functions that unit tests run on. If you write spaghetti code, you can not easily expose interface for unit test to run. thus it **increase code clearity** and avoid intertwined code
- if you are only doing one test and then one section of code a time, you will **know when your code break** (it is always the last thing you add), instead of wasting hours trying to find bug in some hidden corner cases

cons:
- **high maintenance cost**, since you will need to write test for everything you're planning to add, instead of only the high-level interfaces
- it becomes a requirement for **everyone in your group**
- the cost propogated to later stage if a requirement is changed will be much higher. the chart shown in class shows that each step adds cost to a magnitude higher. with test driven development there is essentially **another step in between** which will further multiply all the cost