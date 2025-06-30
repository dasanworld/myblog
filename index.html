---
layout: default
title: My Blog
---

<h2>오늘 포스트</h2>

{% assign today = "now" | date: "%Y-%m-%d" %}
<p>오늘 날짜: {{ today }}</p>

<ul>
  {% assign today = "now" | date: "%Y-%m-%d" %}
  <p>오늘 날짜(today 변수 값): {{ today }}</p>
  {% assign today_posts = site.posts | where_exp: "post", "post.date | date: '%Y-%m-%d' == today" %}
  {% if today_posts.size > 0 %}
    {% for post in today_posts %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span>{{ post.date | date: "%Y-%m-%d %H:%M" }}</span>
      </li>
    {% endfor %}
  {% else %}
    <li>오늘 포스트가 없습니다.</li>
  {% endif %}
</ul>

<h2>이전 포스트</h2>
<ul>
  {% for post in site.posts %}
    {% unless post.date | date: "%Y-%m-%d" == today %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span>{{ post.date | date: "%Y-%m-%d %H:%M" }}</span>
      </li>
    {% endunless %}
  {% endfor %}
</ul>
