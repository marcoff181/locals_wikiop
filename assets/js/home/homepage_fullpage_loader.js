
var myFullpage = new fullpage('#fullpage', {
        anchors: ['introHomepage', 'botoesMenu'],
        sectionsColor: ['#125582', '#125582'],
    slideSelector: '.slide2',
    /*scrollOverflow: true,*/

        navigation: true,
     autoScrolling: false,
            navigationPosition: 'right',
        navigationTooltips: ['Introdução do site', 'Escolhe um tema'],
        responsiveWidth: 1100,
    responsiveHeight: 600,
   fitToSection: false,
    /*resetSliders:true,*/
licenseKey: '6D5A2159-B20143E0-8CE02F7F-AF19A3C4',
        afterResponsive: function(isResponsive){

        },
    

			});



