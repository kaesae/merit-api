# Project Merit Overview


## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Planning and Approval | Incomplete
|Day 1| Set up backend with Python/Django| Incomplete
|Day 1.5| Test backend | Incomplete
|Day 2| Set up frontend with React then test | Incomplete
|Day 2.5| Test frontend | Incomplete
|Day 3| Minimal CSS, then JavaScript functions | Incomplete
|Day 4| JavaScript functions, merit score cumulative function | Incomplete
|Day 5| MVP & Bug Fixes & Adding Seed Data | Incomplete
|Day 6| Debugging| Incomplete
|Day 7| Full Styling with Animations | Incomplete
|Day 8| Present | Incomplete


## Project Description

Merit is a transparent social media application where good samaritans can rate their network and give specific positive praise for their good qualities. At Merit, our philosophy is to shine light onto everyday people with altruism, holistic mindsets, and a sense of community.

Merit's backend will be built with Python and Django, while our frontend will be powered by React and JavaScript.



## User Stories

Everyday people will log into Merit and when they see their rating go up due to a recent social interaction, they will find out that they are Good Samaritans. A specific positive praise will come up alongside that rating 

## Wireframes   

- [Mobile](https://drive.google.com/file/d/1jIgVx7uq7n9RXkQt2_8qWYOOqMhkl-RX/view?usp=sharing)



## Time/Priority Matrix 

[Link](https://drive.google.com/file/d/1-x2qCgwxylPw7JvXJfaKhdjDh9BK0syg/view?usp=sharing)


### MVP/PostMVP  

#### MVP

- 3 models for our data (User, Comment, Rating)
- CRUD functionality (Create Posts for other users, Read previous posts, Update posts, Delete posts)
- Have 4 Routes and components on frontend (Home, Daily Tracker, My Health Page, About Team)
- Fetch data from backend API
- Animations (Posts slightly slides up and transitions from transparent on page load)
- Animations (Arrow slides up or down depending on rating given)
- Fully Deployed frontend and backend

#### PostMVP 

- Graph function for longitudinal ratings
- Graph function for recent ratings
- Graph function since beginning
- Posts are marked as a broad and specific quality (i.e. Broad, Specific; Community, Altruism; Social, Mediator; Characteristic, Genuine)
- Badges page for specific qualities

## Routing Table

| **URL**     | **HTTP Verb** | **Action** | **Description**             |
| ----------- | ------------- | -------------- | ---------------------- |
| /            | GET          |    show        | shows merit display page  |
| /sign-up     | POST         |    create      | creates  |
| /sign-in     | POST         |    show        | checks if existing user   |
| /sign-out    | DELETE       |    delete      | deletes token  |
| /home        | READ         |    show        | populates user data and recent post   |
| /overview    | GET          |    show        | show graphs over time of posts and ratings  |
| /posts/:id   | UPDATE       |    update      | updates a post |
| /posts/:id   | DELETE       |    delete      | deletes a post |
| /about       | READ         |    show        | displays company info   |


## Functional Components

| Component | Description | 
| --- | :---: | 
| Display Page | Landing Page with Add New User Button |
| Sign Up | Form to add new user| 
| Sign In | Form to check if existing user |
| Header | Logo and Menu | 
| About Merit | Photos and team description | 
| Longitudinal Graph | Graph function for longitudinal ratings | 
| Recent Ratings Graph| Graph function for recent ratings | 
| Overview Graph| Graph function since beginning | 
| Footer | My info |

#### MVP
| Component | Priority | Estimated Time | Actual Time |
| --- | :---: |  :---: | :---: | 
| Installing and Setup for backend            | H | 2hr | hr |
| Models and Views                            | H | 8hr | hr |
| CRUD Routes and debugging, test on Postman | H | 5hr | hr |  
| Deploying backend                           | H | 3hr|  hr | 
| Creating React App                          | H | 1hr | hr|
| About page                                  | H | 1hr | hr|
| Add Routes                                  | H | 1hr |  hr |
| Login Authentication                        | H | 3hr | hr |
| Create Components                           | H | 20hrs|  hr |
| Star Rating                                 | H | 3hr | hr|
| Fetch and test data on frontend             | H | 3hr |  hr |
| Animations                                  | H | 3hr | hr |
| CSS                                        | H | 3hr |  hr |
| Deploy frontend                            | H | 1hr |  hr |
| Total                                      | H | 53hrs| hr |

#### PostMVP
| Component | Priority | Estimated Time | Actual Time |
| --- | :---: |  :---: | :---: | 
| Longitudinal Graph | L | 5hr | hr |
| Recent Ratings Graph | L | 3hr | hr |
| Overview Graph | L | 2hr | hr |
| Posts tagged with qualities | L | 5hr | hr |
| Badges Page | M | 4hr | hr |
| Total | H | 19hrs| hrs |

## Additional Libraries
 Use this section to list all supporting libraries and thier role in the project. 

- [Animations:] (tobiasahlin.com)
- [Fonts:] (googlefonts)

## Code Snippet

Use this section to include a brief code snippet of functionality that you are proud of an a brief description  

```
TBD

```

## Issues and Resolutions
