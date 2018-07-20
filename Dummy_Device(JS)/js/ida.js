 $(function(){
        csmapi.set_endpoint ('http://test.iottalk.tw:9999');
        var profile = {
		    'dm_name': 'Dummy_Device',          
			'idf_list':[Dummy_Sensor],
			'odf_list':[Dummy_Control],			
        };
		
        function Dummy_Sensor(){
            return Math.random();
        }
		
        function Dummy_Control(data){
            $('.ODF_value')[0].innerText=data[0];
        }
      
/*******************************************************************/                
        function ida_init(){}
        var ida = {
            'ida_init': ida_init,
        }; 
        dai(profile,ida);     
});
