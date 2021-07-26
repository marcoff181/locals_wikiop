$(document).ready(function () {

    var $container2 = $('#containerisotope');
    $items = $('.itemiso');

    $container2.isotope({
        itemSelector: '.itemiso',
        masonry: {
            columnWidth: 5
        },
        getSortData: {
            selected: function ($item) {
                return ($items.hasClass('selected selected1') ? -1000 : 0) + $items.index();
            }
        },
        sortBy: 'selected selected1'
    });
          /*$container.isotope('shuffle');*/
        $container2.isotope('layout');

    $('.itemiso').click(function () {

        if ($(this).hasClass('selected')) {
            $(this).removeClass('selected');
            $(this).children('#maximise').hide();
            $(this).children('.minimise').show();
        } else {
            $(this).addClass('selected');
            $(this).children('.minimise').hide();
            $(this).children('#maximise').show();
        }

        /*$container.isotope('shuffle');*/
        $container2.isotope('layout');
    });

});

$(function() {
    var $container1 = $('#containerisotope'),
        $select = $('div#filterGroup select');
    filters = {};

    $container1.isotope({
        itemSelector: '.itemiso'

    });
        $select.change(function() {
        var $this = $(this);

        var $optionSet = $this;
        var group = $optionSet.attr('data-filter-group');
    filters[group] = $this.find('option:selected').attr('data-filter-value');

        var isoFilters = [];
        for (var prop in filters) {
            isoFilters.push(filters[prop])
        }
        var selector = isoFilters.join('');

        $container1.isotope({
            filter: selector
        });

        return false;
    });

});