---
layout: default
title: My Blog
---

<h1>최신 포스트 5개</h1>
<ul>
  {% for post in site.posts limit:5 %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <span>{{ post.date | date: "%Y-%m-%d %H:%M" }}</span>
    </li>
  {% endfor %}
</ul>
