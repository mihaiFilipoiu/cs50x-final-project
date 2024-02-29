# WORKOUT JOURNAL
#### Video Demo:  <https://www.youtube.com/watch?v=pLy1VccLulk&ab_channel=MihaiF>
#### Description:


The Workout Journal App is my go-to digital fitness companion, designed to make tracking my workouts a breeze and helping me stay on top of my fitness goals. It's like having a personal trainer in my pocket!

When I set out to create this app, my main goal was to make it super easy for anyone to log their workouts and see their progress over time. I wanted to create something that would be intuitive to use, even for people who aren't tech-savvy.

With the Workout Journal App, I can create my own account in just a few clicks. Once I'm logged in, I can start logging my workouts right away. I've made it super simple to record all the important details of my workout, like which muscles I worked, what exercises I did, and how many sets and reps I completed.

One of the coolest features of the app is that it's really flexible. Whether I'm into weightlifting, running, yoga, or anything in between, I can easily customize the app to fit my workout routine. I can even add notes and comments to my workouts to help me remember how I felt or any insights I had during my session.

As I keep logging my workouts, the app will automatically track my progress over time. I'll be able to see how my strength and endurance improve, which exercises I'm getting better at, and where I might need to push myself a little harder.

I've also made sure that the app is super easy to navigate. Whether I'm using it on my computer, tablet, or phone, I'll find that everything is laid out in a way that makes sense and is easy to understand.

Overall, the Workout Journal App is all about making it easier for me to stay consistent with my workouts and reach my fitness goals. It's like having a personal trainer cheering me on every step of the way!

#### Files:

app.py: This is the main Python file that contains the backend logic of the web application. It is built using the Flask framework and handles routing, user authentication, database interactions, and rendering HTML templates.

helpers.py: This is the secundary Python file that contains helpful functions that i used in 'app.py', such as: login_required()(decorated function).

templates/: This directory contains all the HTML templates used to render different pages of the web application. Each template corresponds to a specific page or component of the app, such as the login page, registration page, homepage, workout logging page, etc.

static/: This directory contains static files such as CSS stylesheets, JavaScript files, and images used in the web application. These files are served to the client-side and are responsible for the styling and functionality of the app's frontend.

workouts.db: This is the SQLite database file used to store user data, workout logs, and other relevant information. The database schema is defined in the app.py file and is used to interact with the database using SQL queries.

#### Files explained:

app.py: This file contains the Flask application setup, including route definitions for different pages, user authentication logic, and database interactions. It handles user registration, login, logout, and session management. Additionally, it defines routes for displaying the homepage, adding a new workout log, viewing workout details, and other functionalities.

HTML Templates: Each HTML template in the templates directory corresponds to a specific page or component of the web application. For example:

- layout: This template renders the navbar of the app with specific buttons for when the user is logged in or not.

- login.html: This template renders the login page, allowing users to enter their credentials and log in to their accounts.

- register.html: This template renders the registration page, allowing new users to create an account.

- index.html: This template renders the homepage, displaying logged workouts and providing options to add a new workout or view workout details.

- add_log.html: This template renders the form for adding a new workout log, allowing users to specify details such as muscle group, exercises, sets, reps, and weights.

- log.html: This template renders the detailed view of a workout log, displaying information about the muscle group, date, and exercises performed.

Static Files: The static directory contains CSS stylesheets, JavaScript files, and images used to enhance the frontend appearance and functionality of the web application. For example:

- styles.css: This CSS stylesheet defines the styling for various elements of the web application, such as fonts, colors, layout, and responsiveness.

#### Features:

- User authentication: Users can create accounts and log in securely.
- Logging workouts: Users can log their workouts, specifying the muscle groups worked and the exercises performed.
- Viewing workout history: Users can view their workout history, including details of each workout logged.
- Dynamic forms: The app includes dynamic forms for logging workouts, allowing users to add multiple exercises to a single workout session.

#### Technologies Used:

- Python
- Flask
- HTML
- CSS
- JavaScript
- Jinja2 templating engine
- SQLite database