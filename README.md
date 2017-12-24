# website

The file only includes plain text without pictures
The original file should refer to: README.pdf
---------------------------------------------------------------------------------------------------------------------------------------
Based on the description of the Code Test, I needed to build a website for a fictitious government and chose promoting traveling in Melbourne as the topic of the government website. As a result of that it is my first year in Melbourne, I think that there are a lot of things to explore in the city.

The major techniques used to implement the website are Python and Django. This combination is the most popular way to implement a website. The major feature of Django is that it implements the MVC, or we should say MTV, so that the website is easily to scale up and maintain. On the other hand, taking the other two requirements into account: ChatBot and Data visualization, I think the variety of libraries of Python and techniques compatible to it would be very helpful. For example, I built the website from the base of Bootstrap. Even though I can build it from the scratch, this way may be time-efficient under the time-limited situation for me. All works were running in the python virtual environment to make sure that the work is independent from others. That is why I chose Python and Django to implement the website.

The website met all requirements listed in the description. It includes standard routine of about, FAQ, contact etc as shown in Figure 1, 2 and 3:


 
Figure 1. The standard routine: About (presented by multimedias)
 
Figure 2. The standard routine: FAQ (with ipsum text)


 
Figure 3. The standard routine: Contact

But not limited to them; according to the essence of the website: promote traveling, the website also shows some famous tourist spots via JQuery as shown in Figure 4:
 
Figure 4. More features beyond the requirement

As for the multi-step webform, it was implemented in the form of anonymous discussion board. In the discussion board, guests can post their subject which includes the topic of the subject, their name, and the content, and then others can reply the subject to share information or discuss. The link to the Discussion Board can be found on the navigation bar on the homepage as well, and redirect to the homepage of Discussion Board as Figure 5:

 
Figure 5. The homepage of The Discussion board

Replying to a topic and reading all replies to a topic are shown in Figure 6 and 7:
 
Figure 6. Reply to one topic

 
Figure 7. Read all replies to a topic

For another requirement:Chatbot, it can be activated by the link “ONLINE SERVICES” at the homepage. Clicking the link will redirect to a new page and start a chat with Chatbot. The Chatbot was implemented by ChatterBot which is one of Python Libraries and trained to reply most basic conversations and questions relating to traveling, such as “What is the most famous spot in Melbourne?” or “Which restaurant is the best?” etc. The response to these questions is shown in Figure 8.

 
Figure 8. Chatting with Chatbot about traveling

The last requirement, Data visualization, was implemented by D3.js. I utilized D3.js to visualize the number of tourists from all over the world to Melbourne into circles with different size based on the number of tourists from that country. That is, that more tourists coming from that country will lead to a larger circle. On the other hand, for the more concise and indicative result, only the country with the number of tourists greater than 60,000 will show its name on the circle. The visualized data is like the Figure 9:

 
Figure 9. Visualized number of tourists from different countries 

To sum up, this work used the following techniques: HTML, CSS, Javascript, JQuery, Python, Django, Bootstrap, ChatterBot and D3.js. It might not a perfect outcome, but I really have learnt a lot from this project and thank to the opportunity. After I completed the project, I know I still has a lot to learn and am excited about it!

