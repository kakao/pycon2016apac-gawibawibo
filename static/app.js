$(function () {
    var hands = [$('#gawi'), $('#bawi'), $('#bo')];
    var cur_hand = 0;
    setInterval(function () {
        hands[cur_hand].hide();
        cur_hand = (cur_hand + 1) % hands.length;
        hands[cur_hand].show();
    }, 500);

    $('#play').click(function () {
        $('#audio')[0].play();
    });

    //
    // by outsider
    //

    var audio = new Audio('/static/gawibawibo-bo-bo-bo.mp3');
    var $left = $('.hand.left');
    var $right = $('.hand.right');
    var changeHand = function (left, right) {
        $left.attr('src', '/static/' + left + '.png');
        $right.attr('src', '/static/' + right + '.png');
    };

    $('#open').click(function () {
        $('#popup').show();
        audio.play();
        $('.hand').addClass('start');
        setTimeout(function () {
            changeHand('bo', 'gawi');
        }, 2100);
        setTimeout(function () {
            changeHand('gawi', 'bawi');
        }, 3000);
        setTimeout(function () {
            changeHand('bo', 'bo');
        }, 3900);
        setTimeout(function () {
            changeHand('bawi', 'gawi');
        }, 4700);
    });
    $('#close').click(function () {
        $('#popup').hide();
    });
});
