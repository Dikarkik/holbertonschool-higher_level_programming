// Script that toggles the class of the HTML tag HEADER
// when the user clicks on the tag DIV#toggle_header.

$("div#toggle_header").on("click", function () {
  if ($('header').attr('class') === 'green')
    $('header').removeClass('green').addClass('red');
  else
    $('header').removeClass('red').addClass('green');
});
