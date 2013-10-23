$(function() {
  var raffled = $('.raffled'),
      all = $('.bet');

  var concourses = new Array();

  raffled.each(function() {
    var concourse = parseInt($(this).text());
    concourses.push(concourse);
  });

  all.each(function() {
    var bet = parseInt($(this).text());
    for (var i = 0; i < concourses.length; i++) {
      if (bet === concourses[i]) {
        $(this).css({'color': '#1632C2'}).parent().addClass('found-same-concourse');
        
      }
    }
  });

  $('.bets').each(function() {
    if ($(this).find('.found-same-concourse').length > 3) {
      $(this).find('.check-status').addClass('match').removeClass('dont-match');
    }
  });
});
