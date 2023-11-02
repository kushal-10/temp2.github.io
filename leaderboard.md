---
layout: default
title: Leaderboard
---

# center table
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
      {% for cell in row %}
        <td>{{ cell[1] }}</td>
      {% endfor %}
    </tr>
    {% endfor %}
  </table>
</div>
