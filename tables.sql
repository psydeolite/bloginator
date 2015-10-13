CREATE TABLE User(
       User_ID INT	 NOT NULL,
       Name VARCHAR(20)	 NOT NULL,
       PRIMARY KEY (User_ID)
);

CREATE TABLE Blog(
       Blog_ID INT	NOT NULL,
       User_ID INT	NOT NULL,
       Blog_Name CHAR(30)	NOT NULL,
       Post_Time DATE		NOT NULL,
       PRIMARY KEY (Blog_ID)
);

CREATE TABLE Post(
       Post_ID INT	NOT NULL,
       Blog_ID INT	NOT NULL,
       User_ID INT	NOT NULL,
       Post_Time DATE	NOT NULL,
       Text CHAR(500)	NOT NULL,
       PRIMARY KEY (Post_ID)
);

CREATE TABLE Comment(
       Comment_ID INT	NOT NULL,
        Post_ID INT	NOT NULL,
       Blog_ID INT	NOT NULL,
       User_ID INT	NOT NULL,
       Post_Time DATE	NOT NULL,
       Text CHAR(500)	NOT NULL,
       PRIMARY KEY (Comment_ID)
);