function ajax() {
    $('body a').live('click', function(event) {
        link = $(this).attr('href');

        if (link.indexOf('/articles/') == 0 || link.indexOf('/flat/') == 0) {
            event.preventDefault();
            $.ajax({url: link}).success(function(data) {
                $(data).replaceAll('section#articles');
                articles_bottom();
            });
        };
    });
};

feeds = {
    keep_scrolling: function() {
        setTimeout(function() {
            feeds.scroll();
            feeds.keep_scrolling();
        }, 5000);
    },
    scroll: function() {
        var last = $('#feeds article:last');
        last.remove();
        $('#feeds').prepend(last);
        $('#feeds article').each(function(index) {
            if (index < feeds.available) {
                $(this).show();
            } else {
                $(this).hide();
            }});
    },
    get_available: function() {
        var aside = $('aside')
        var available = window.innerHeight - aside.position().top - aside.height();
        var feed_height = aside.find('#feeds article').first().height();
        var available = parseInt(available / feed_height) - 1;
        var available = (available > 0) ? available : 0;
        this.available = available;
    }
};


function articles_bottom() {
    var aside_height = $('aside').outerHeight();
    $('section#articles').height(aside_height);
};

function categories_left() {
    $(window).resize(function() {
        var categories = $('#categories');
        var left = categories.width();
        categories.css({left: '-{left}px'.replace('{left}', left)});
    });
    $(window).resize()
};

$(function() {
    categories_left();
    articles_bottom();
    feeds.get_available();
    feeds.scroll();
    feeds.keep_scrolling();
    ajax();
});
