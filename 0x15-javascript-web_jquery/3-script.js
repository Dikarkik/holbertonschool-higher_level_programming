// Script that adds the class red to the HTML tag HEADER
// when the user clicks on the tag DIV#red_header.

$("div#red_header").on("click", function (event) {
  $("header").addClass("red");
});
