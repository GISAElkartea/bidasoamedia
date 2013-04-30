function ajax() {
    $('body a[href^="/articles"]').live('click', function(event) {
        event.preventDefault();
        link = $(this).attr('href');
        $.ajax({url: link}).success(function(data) {
            $(data).replaceAll('section#articles');
            var title = $('div#title');
            title.remove();
            $('head title').text(title.text());
            articles_bottom();
        });
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
        var available = parseInt(available / feed_height) - 2;
        var available = (available > 0) ? available : 0;
        this.available = available;
    }
};


function articles_bottom() {
    var articles = $('section#articles')
    var height = window.innerHeight - articles.position().top;
    if (articles.height() < height) {
        articles.height(height);
    };
};

$(function() {
    articles_bottom();
    feeds.get_available();
    feeds.scroll();
    feeds.keep_scrolling();
    ajax();
});
