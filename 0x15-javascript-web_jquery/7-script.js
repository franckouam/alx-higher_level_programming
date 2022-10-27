const characterDiv = $('#character');
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: function (character) {
    characterDiv.text(character.name);
  }
});
