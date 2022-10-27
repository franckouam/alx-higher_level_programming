const ulList = $('.my_list');
alert("Le js a charge");
$('#add_item').click(function () {
    alert('on a clique add_item');
    ulList.append('<li>Item</li>');
  });

$('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

$('#clear_list').click(function () {
    ulList.empty();
  });