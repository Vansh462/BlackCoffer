# BlackCoffer
 a task assignment given to me


The Problem
(Detailed Task is in "Objective" MS word file inside Problem Details folder)
A table with headings and links was given , i had to scrap heading wise data from the link and store it in files named heading wise , for eg if there are 10 headings then 10 files for each heading.
Further i had to calculate 13 Sentiment analysis Variables like positive score, negative score, word count, Fog index, Percentage Complex words , etc

definitions of all is provided in Problem Details folder as named "text Analysis" ms word file.



HOW I APPROACHED THE SOLUTION

Understanding the Problem: I carefully reviewed and understood the requirements of the assignment. This helped me identify the specific tasks I needed to perform, such as extracting articles from URLs and computing text analysis variables.

Research and Planning: I researched relevant libraries, tools, and techniques that could help me achieve the tasks outlined in the assignment. Based on my research, I planned my approach, including how to extract articles from URLs and what text analysis techniques to use.

Choosing Tools and Libraries: After researching and planning, I chose the appropriate tools and libraries for the task. For example, I decided to use Python with libraries like BeautifulSoup for web scraping and NLTK for text analysis.

Implementing Article Extraction: I wrote code to extract textual data articles from the given URLs. This involved using web scraping techniques with BeautifulSoup and handling different HTML structures and errors gracefully.

Performing Text Analysis: Once I extracted the articles, I performed text analysis to compute the required variables. This included tasks such as tokenization, stop word removal, sentiment analysis, and word frequency analysis.

Computing Variables: I computed the variables required for the assignment, such as word count, sentence count, average word length, and sentiment scores. I ensured that these variables were accurately calculated based on the text analysis results.

Testing and Validation: I tested my implementation with different URLs and articles to ensure it worked correctly. I also validated the computed variables to ensure their accuracy and consistency.

Documenting and Presenting Results: I documented my code, including comments and documentation strings, to make it easy to understand and maintain. I presented the results of my text analysis, including computed variables and any insights gained, in a clear and understandable format.

Iterating and Improving: Finally, I iterated on my implementation based on feedback and additional requirements. I looked for opportunities to improve efficiency, accuracy, or functionality to ensure the best possible outcome.




HOW TO RUN PY FILE
1) make sure you are in the same directory as BlackCoffee drive folder provided by BlackCoffee company in assignment.
2)executing py file will automatically scrap articles from the links in excel file and store them on "data/"
3)output of file will automatically show the output.xlsx files starting rows and also save the output file in the same directory.

the BlackCoffer.py file is in Solution Folder


REQUIREMENTS

libraries:
1)pandas
2)bs4
3)requests
4)os
5)nltk