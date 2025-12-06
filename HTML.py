#!/usr/bin/env python
# coding: utf-8

# In[ ]:


<!DOCTYPE html>
<html>
<head>
<title>My Blog</title>
</head>
<body>
<h1>My Blog</h1>
<hr>


{% with messages = get_flashed_messages() %}
{% if messages %}
<ul>
{% for msg in messages %}
<li>{{ msg }}</li>
{% endfor %}
</ul>
{% endif %}
{% endwith %}


{% block content %}{% endblock %}
</body>
</html>


# In[ ]:


{% extends 'base.html' %}
{% block content %}
<h2>Recent Posts</h2>


{% for post in posts %}
<h3><a href="/post/{{ post.id }}">{{ post.title }}</a></h3>
<small>By {{ post.author }} on {{ post.date_posted }}</small>
<hr>
{% endfor %}


{% endblock %}


# In[ ]:


{% extends 'base.html' %}
{% block content %}
<h2>Login</h2>
<form method="POST">
<label>Username:</label>
<input type="text" name="username" required><br>


<label>Password:</label>
<input type="password" name="password" required><br>


<button type="submit">Login</button>
</form>
{% endblock %}


# In[ ]:


{% extends 'base.html' %}
{% block content %}
<h2>Your Posts</h2>
<a href="/new">Create New Post</a>
<br><br>


<table border="1" cellpadding="5">
<tr>
<th>Title</th>
<th>Edit</th>
<th>Delete</th>
</tr>


{% for post in posts %}
<tr>
<td>{{ post.title }}</td>
<td><a href="/edit/{{ post.id }}">Edit</a></td>
<td><a href="/delete/{{ post.id }}">Delete</a></td>
</tr>
{% endfor %}
</table>
{% endblock %}


# In[ ]:


{% extends 'base.html' %}
{% block content %}
<h2>Your Posts</h2>
<a href="/new">Create New Post</a>
<br><br>


<table border="1" cellpadding="5">
<tr>
<th>Title</th>
<th>Edit</th>
<th>Delete</th>
</tr>


{% for post in posts %}
<tr>
<td>{{ post.title }}</td>
<td><a href="/edit/{{ post.id }}">Edit</a></td>
<td><a href="/delete/{{ post.id }}">Delete</a></td>
</tr>
{% endfor %}
</table>
{% endblock %}


# In[ ]:


{% extends 'base.html' %}
{% block content %}
<h2>Edit Post</h2>
<form method="POST">
<label>Title:</label>
<input type="text" name="title" value="{{ post.title }}" required><br><br>


<label>Content:</label><br>
<textarea name="content" rows="10" cols="40" required>{{ post.content }}</textarea><br><br>


<button type="submit">Update</button>
</form>
{% endblock %}


# In[ ]:


{% extends 'base.html' %}
{% block content %}
<h2>{{ post.title }}</h2>
<small>By {{ post.author }} on {{ post.date_posted }}</small>
<hr>
<p>{{ post.content }}</p>
{% endblock %}

