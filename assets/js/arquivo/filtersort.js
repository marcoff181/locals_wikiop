$(function() {

    var $container = $('#container'),
        $select = $('#filters select');

    $container.isotope({
        itemSelector: '.item'
    });

    $select.change(function() {
        var filters = $(this).val();
;
        $container.isotope({
            filter: filters
        });
    });

});