$(function() {
	var table = $('table');


	table.each(function() {
		var concourses = [];

		$(this).find('.raffled').each(function() {
			var concourse = parseInt($(this).text());
			concourses.push(concourse);
		});

		$(this).find('.bet').each(function() {
			var bet = parseInt($(this).text());
			for (var i = 0; i < concourses.length; i++) {
				if (bet === concourses[i]) {
					$(this).css({'color': '#1632C2'}).parent().addClass('found-same-concourse');
				}
			}
		});

		$(this).find('.bets').each(function() {
			if ($(this).find('.found-same-concourse').length > 3) {
				$(this).find('.check-status').addClass('match').removeClass('dont-match');
			}
		});
	});
});
