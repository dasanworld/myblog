---
layout: default
title: My Blog
---

<h1>최신 포스트</h1>
<ul>
  {% for post in paginator.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <span>{{ post.date | date: "%Y%m%d %H:%M" }}</span>
    </li>
  {% endfor %}
</ul>

<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path }}">이전</a>
  {% endif %}
  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path }}">다음</a>
  {% endif %}
</div>
