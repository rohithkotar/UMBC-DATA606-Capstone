1. **Title and Author**
   - **Project Title**: Real-Time Reddit Chatbot on Data Science Subreddit
   - **Prepared for UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang**
   - **Author Name**: Rohith Kotar
   - **Link to the author's GitHub profile**: https://github.com/KotarRohith
   - **Link to the author's LinkedIn profile**: https://www.linkedin.com/in/rohith-kotar/
   - **Link to your PowerPoint presentation file**: 
   - **Link to your YouTube video**: 

2. **Background**
   - **What is it about?**: This project focuses on developing a real-time chatbot that operates on Reddit data from the data science subreddit.
   - **Why does it matter?**: With the increasing interest in data science and related topics, having a chatbot that can provide real-time insights and engage users on data science discussions can be valuable.
   - **What are your research questions?**: 
     - How can we leverage Reddit data to create a chatbot that responds to user queries on data science topics?
     - How accurate and responsive can the chatbot be in real-time interactions with users?

3. **Data**
   - **Data sources**: Reddit PRAW API
   - **Data size**: 1 GB
   - **Data shape**: Depends on API query results
   - **Time period**: Jan 2023 to Dec 2023
   - **What does each row represent?**: Each row represents a post on the data science subreddit.
   - **Data dictionary**: 
     - *Columns name*: title, selftext, author, num_of_comments, score, created_utc (as of now)
     - *Data type*: String, timestamp
     - *Definition*:
       - Title: The title of a Reddit submission (post), which is typically a brief summary or description of the content being shared or discussed.
       - Selftext: The main body of text accompanying a Reddit submission. It provides additional context, information, or details related to the content of the post. Not all posts have selftext, as some may be link posts with no accompanying text.
       - Author: The username of the Reddit user who created the submission. This attribute indicates the original poster (OP) of the content.
       - Num_of_comments: The number of comments that the Reddit submission has received. Comments are responses or reactions from other Reddit users to the original post.
       - Score: The score of the Reddit submission, which represents the net number of upvotes minus downvotes received by the post. It is a measure of the post's popularity and perceived quality within the Reddit community.
       - Created_utc: The timestamp indicating the date and time when the Reddit submission was created, represented in Coordinated Universal Time (UTC). It provides information about when the post was originally posted to the platform.
   - **Target/label**: Not applicable. 
   - **Features/predictors**: Text content of posts and metadata such as author, timestamp, number of upvotes etc.

4. **Exploratory Data Analysis (EDA)**

5. **Model Training**
   - **Predictive analytics models**: Natural Language Processing (NLP) models for text analysis and understanding.
   - **Model training**: Python packages like NLTK for training NLP models.
   - **Train vs test split**: N/A
   - **Performance measurement**: Metrics such as accuracy, precision, recall, and F1-score for evaluating model performance.

6. **Application of the Trained Models**
   - Develop a web app using Flask for users to interact with the trained chatbot models.
   - Users can query the chatbot for real-time insights and engage in data science discussions based on Reddit data.

7. **Conclusion**

8. **References**
