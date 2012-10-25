$(function() {
    $('body a').live('click', function(event) {
        link = $(this).attr('href');

        if (link.indexOf('/articles/') == 0) {
            event.preventDefault();
            $.ajax({url: link}).success(function(data) {
                $('section#articles *').remove()
                $('section#articles').append(data);
            });
        };
    });
});
