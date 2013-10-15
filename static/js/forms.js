$(function() {
  $('form').on('keyup', 'input[name="number"]', function() {
    if (isNaN($(this).val()) || parseInt($(this).val()) <= 0 || parseInt($(this).val()) > 2000) {
      $(this).addClass('wrong').focus();
    } else {
      $(this).removeClass('wrong');
    }
  });

  $('form').on('keyup', 'input[name^="n0"]', function() {
    if (isNaN($(this).val()) || parseInt($(this).val()) <= 0 || parseInt($(this).val()) > 60) {
      $(this).addClass('wrong').focus();
    } else {
      $(this).removeClass('wrong');
    }
  }).on('focusout', 'input[name^="n0"]', function() {
    if ($(this).val() < 10 && $(this).val().length < 2) {
      $(this).val('0' + $(this).val());
    }
  });

  $('input[type="text"]').autotab_magic().autotab_filter('numeric');
});
