$(function() {
  function signalWrong(target) {
    $(target).addClass('wrong').focus();
    $('input[type="submit"]')
      .attr('disabled', 'disabled')
      .css({'color': '#C4C7C8'});
  }

  function signalRight(target) {
    $(target).removeClass('wrong');
    $('input[type="submit"]')
      .removeAttr('disabled')
      .css({'color': '#000', 'cursor': 'auto'});
  }

  $('form').on('keyup', 'input[name="number"]', function() {
    if (isNaN($(this).val()) || parseInt($(this).val()) <= 0 || parseInt($(this).val()) > 2000) {
      signalWrong($(this));
    } else {
      signalRight($(this));
    }
  }).on('keyup', 'input[name*="n0"]', function() {
    if (isNaN($(this).val()) || parseInt($(this).val()) <= 00 || parseInt($(this).val()) > 60) {
      signalWrong($(this));
    } else {
      signalRight($(this));
    }
  });

  $('input[type="text"]').autotab_magic().autotab_filter('numeric');
});
