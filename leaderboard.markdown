---
layout: default
title: Leaderboard
---

<style>
    table {
        margin-left: auto;
        margin-right: auto;
    }
</style>

# Leaderboard

<div id="leaderboard">
  <table>
    <tr>
      {% for header in site.data.leaderboard[0] %}
        <th>{{ header[0] }}</th>
      {% endfor %}
    </tr>
    {% for row in site.data.leaderboard %}
      <tr>
      <!-- Remove odd numbered rows -->
      <!-- Display model--model only once -->
        {% assign row_index = forloop.index0 | modulo: 2 %}
        {% for cell in row %}
          {% if forloop.first and row_index != 0 %}
            <td></td>
          {% else %}
            <td>{{ cell[1] }}</td>
          {% endif %}
        {% endfor %}
      </tr>
    {% endfor %}
  </table>
</div>

