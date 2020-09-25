// Script that adds a LI element to a list
// when the user clicks on the tag DIV#add_item:
// The new element must be: <li>Item</li>
// The new element must be added to UL.my_list

$("div#add_item").on("click", function () {
  $("UL.my_list").append('<li>Item</li>');
});
