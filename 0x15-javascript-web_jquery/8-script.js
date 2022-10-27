const moviesUl = $('#list_movies');
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function (response) {
    $.each(response.results, function (i, movie) {
      moviesUl.append('<li>' + movie.title + '</li>');
    });
  }
});
