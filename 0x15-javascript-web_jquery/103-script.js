const url = 'https://fourtonfish.com/hellosalut/?lang=';
$(document).ready(function () {
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      const lan = $('INPUT#language_code').val();
      $.getJSON(url + lan, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });

  $('INPUT#btn_translate').on('click', function () {
    const lan = $('INPUT#language_code').val();
    $.getJSON(url + lan, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
