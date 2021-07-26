 var config = {
		
      '.chosen-select'           : {},
      '.chosen-select-deselect'  : {allow_single_deselect:true},
      '.chosen-select-no-single' : {disable_search_threshold:10},
      '.chosen-select-no-results': {no_results_text:'Oops, nothing found!'},
      '.chosen-select-width'     : {width:"95%"},
	  '.chosen-select-height'     : {height:"700px"},
	  '.chosen-select-height'     : {height:"700px"}
    }
    for (var selector in config) {
      $(selector).chosen(config[selector]);
	  
	  
    }