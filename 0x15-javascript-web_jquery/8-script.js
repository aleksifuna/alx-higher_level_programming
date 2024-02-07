$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data) {
    const movies = data.results;
    $.each(movies, function (i, movie) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
