$(function() {
  var raffled = $('.raffled'),
      all = $('.bet');

  var numbers = new Array();

  raffled.each(function() {
    var number = parseInt($(this).text());
    numbers.push(number);
  });

  all.each(function() {
    var bet = parseInt($(this).text());
    for (var i = 0; i < numbers.length; i++) {
      if (bet === numbers[i]) {
        $(this).css({'color': '#1632C2'}).parent().addClass('found-same-number');
        
      }
    }
  });

  $('.bets').each(function() {
    if ($(this).find('.found-same-number').length > 3) {
      $(this).find('.check-status').addClass('match').removeClass('dont-match');
    }
  });
});
