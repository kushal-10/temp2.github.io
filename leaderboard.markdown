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
<!-- 
<div id="leaderboard">
  <table>
    <tr>
      {% for header in site.data.leaderboard[0] %}
        <th>{{ header[0] }}</th>
      {% endfor %}
    </tr>
    {% for row in site.data.leaderboard %}
      <tr>
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
</div> -->

<div id="leaderboard">
  <table>
    <tr>
      {% for header in site.data.leaderboard[0] %}
        <th>{{ header[0] }}</th>
      {% endfor %}
    </tr>
    {% assign tooltips = "Tooltip 1,Tooltip 2,Tooltip 3,Tooltip 4,Tooltip 5" | split: "," %}
    {% for row in site.data.leaderboard %}
      <tr>
        {% assign row_index = forloop.index0 | modulo: 2 %}
        {% for cell in row %}
          {% if forloop.first and row_index != 0 %}
            <td data-toggle="tooltip" title="{{ tooltips[forloop.index0] }}"></td>
          {% else %}
            <td data-toggle="tooltip" title="Tooltip text here">{{ cell[1] }}</td>
          {% endif %}
        {% endfor %}
      </tr>
    {% endfor %}
  </table>
</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    var tooltips = document.querySelectorAll('[data-toggle="tooltip"]');
    tooltips.forEach(function (el) {
      new bootstrap.Tooltip(el);
    });
  });
</script>
