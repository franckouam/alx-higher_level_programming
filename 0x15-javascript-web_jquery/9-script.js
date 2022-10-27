const helloDiv = $('#hello');
$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  headers: {
    'access-control-allow-credentials':true,
    'access-control-allow-headers':'Origin, X-Requested-With, Content-Type, Accept',
    'access-control-allow-origin':'*'
},
  success: function (response) {
    helloDiv.text(response.hello);
  }
});
