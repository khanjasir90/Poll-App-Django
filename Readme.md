# Django-Poll-App

Django poll app is a full featured polling app. You have to register in this app to show the polls and to vote. If you already voted you can not vote again. Only the owner of a poll can add poll , end poll. If a poll is ended it can not be voted. Once the owner has ended a poll a mail is send to the users regarding the result of the poll and also Analyze feature is also available which provides the result in a visual manner.Also a user can share a poll across devices using QR-Code.

<h1>Getting Started</h1>
<p>These instructions will get you a copy of the project up and running on your local machine for development .</p>

<h2>Prerequisites</h2>
<code>python== 3.5 or up and django==2.0 or up</code>

<h2>Installing</h2>
<pre>open terminal and type</pre>
<code>git clone https://github.com/khanjasir90/Poll-App-Django.git</code><br><br>

<h4>or simply download using the url below</h4>
<code>https://github.com/khanjasir90/Poll-App-Django.git</code><br>

<h2>To migrate the database open terminal in project directory and type</h2>
<code>python manage.py makemigrations</code><br>
<code>python manage.py migrate</code>

<h2>To use admin panel you need to create superuser using this command </h2>
<code>python manage.py createsuperuser</code>

<h2> To run the program in local server use the following command </h2>
<code>python manage.py runserver</code>

<p>Then go to http://127.0.0.1:8000 in your browser</p>

<h2>Run Django-Poll-App using Docker</h2>

<code>docker build . -t djangopollapp</code><br>
<code>docker run -p 8001:8000 -it --rm djangopollapp</code><br>
<p>Then go to http://127.0.0.1:8000 in your browser</p>

<h2>Project snapshot</h2>

<h4>Register Page</h4>
<div>
<img src="https://github.com/khanjasir90/Poll-App-Django/blob/main/screenshot/signup.JPG" width = 80% height= 70%><br>
</div><br>

<h4>Login Page</h4>
<div>
<img src="https://github.com/khanjasir90/Poll-App-Django/blob/main/screenshot/signin.JPG" width = 80% height= 70%><br>
</div><br>

<h4>Home Page</h4>
<div>
<img src="https://github.com/khanjasir90/Poll-App-Django/blob/main/screenshot/home.JPG" width = 80% height= 70%><br>
</div><br>

<h4>Profile Page</h4>
<div>
<img src="https://github.com/khanjasir90/Poll-App-Django/blob/main/screenshot/profile.JPG" width = 80% height= 70%><br>
</div><br>

<h4>Add Poll Page</h4>
<div>
<img src="https://github.com/khanjasir90/Poll-App-Django/blob/main/screenshot/addpoll.JPG" width = 80% height= 70%><br>
</div><br>

<h4>Vote Page</h4>
<div>
<img src="https://github.com/khanjasir90/Poll-App-Django/blob/main/screenshot/vote.JPG" width = 80% height= 70%><br>
</div><br>

<h2>Author</h2>
<blockquote>
  Mohd Jasir Khan<br>
  Email: khanmohdjasir@gmail.com
</blockquote>

<div align="center">
    <h3>========Thank You !!!=========</h3>
</div>