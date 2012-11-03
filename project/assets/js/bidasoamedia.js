function ajax() {
    $('body a').live('click', function(event) {
        link = $(this).attr('href');

        if (link.indexOf('/articles/') == 0) {
            event.preventDefault();
            $.ajax({url: link}).success(function(data) {
                $(data).replaceAll('section#articles');
                articles_bottom();
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

function articles_bottom() {
    var aside_height = $('aside').outerHeight();
    $('section#articles').height(aside_height);
};

$(function() {
    ajax();
    scroll_feeds();
    articles_bottom();
});
