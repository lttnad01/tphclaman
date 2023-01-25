$(document).ready(function() {

    var sloganArea = $('.slogan ul');
    var shown_area = $('.slogan');

    function position_lis(itemHeight) {
        var height = itemHeight;
        $('.slogan ul li').each(function(i) {
            if (i == 0)
                height = 0;
            $(this).css('top', height);
            $(this).removeClass('first');
            height = height + $(this).innerHeight();
        });
    }

    var switch_slogan = function() {
        var itemHeight = $('.slogan ul li').eq(0).innerHeight();
        sloganArea.animate({
            top: itemHeight * -1
        }, {
            duration: 300,
            queue: false,
            complete: function() {
                sloganArea.append($('.slogan ul li').eq(0));
                sloganArea.css('top', 0);
                position_lis(itemHeight);
            }
        });
    };
    var adapt_shown_area = function() {
        shown_area.animate({
            height: $('.slogan ul li').eq(1).find('span').innerHeight(),
        }, {
            duration: 200,
            queue: false,
        });
    };

    var animations = function() {
        switch_slogan();
        adapt_shown_area();
    };
    position_lis($('.slogan ul li').eq(0).innerHeight());
    setInterval(animations, 1800);
});