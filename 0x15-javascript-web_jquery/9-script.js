// Script that fetches from https://fourtonfish.com/hellosalut/?lang=fr
// and displays the value of hello from that fetch in the HTML’s tag DIV#hello.
// Must work when it is imported from the HEAD tag

const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$(document).ready(function () {
    $.get(url, function (data) {
        $('DIV#hello').text(data.hello);
    });
});
