function ajax() {
    $('body a').live('click', function(event) {
        link = $(this).attr('href');

        if (link.indexOf('/articles/') == 0) {
            event.preventDefault();
            $.ajax({url: link}).success(function(data) {
                $(data).replaceAll('section#articles');
            });
        };
    });
};

function scroll_feeds() {
    setTimeout(function() {
        var first = $('#feeds article:first');
        first.remove();
        $('#feeds').append(first);
        scroll_feeds();
    }, 5000);
};

$(function() {
    ajax();
    scroll_feeds();
});
