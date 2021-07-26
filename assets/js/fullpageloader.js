
var myFullpage = new fullpage('#fullpage', {
        anchors: ['temaAgua', 'dadosInteressantes', 'introobjectivosAgua', 'objectivosAgua', 'formularioSugestoes'],
        sectionsColor: ['#4545f3', 'white', 'white', 'white', 'white'],
    slideSelector: '.slide2',
    /*scrollOverflow: true,*/

        navigation: true,
     autoScrolling: false,
            navigationPosition: 'right',
        navigationTooltips: ['Introdução ao tema Água', 'Consulta de Dados interessantes', 'Guia para perguntas', 'Objectivos e perguntas', 'Sugestões!'],
        responsiveWidth: 1100,
    responsiveHeight: 600,
   fitToSection: false,
    /*resetSliders:true,*/
licenseKey: '6D5A2159-B20143E0-8CE02F7F-AF19A3C4',
        afterResponsive: function(isResponsive){

        },
    

			});
/*$(document).on('click', '.accordion', function(){
setTimeout(function(){
  fullpage_api.reBuild(); 
}, 0);
});*/



