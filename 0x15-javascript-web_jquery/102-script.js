const url = 'https://fourtonfish.com/hellosalut/?lang=';
$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const lan = $('INPUT#language_code').val();
    $.getJSON(url + lan, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
