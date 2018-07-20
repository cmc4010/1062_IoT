 $(function(){
        set_endpoint('http://140.113.199.198:9992');
		set_PUSH_INTERVAL(500);

        var profile = {
		    'dm_name': 'Dum_0316092',
			'idf_list':[[Dummy_Sensor,['None']]],
			'odf_list':[[Face_Detect,['None']]],
        };

        function Dummy_Sensor(){
            return Math.random();
        }

        function Face_Detect(data){
            $('.ODF_value')[0].innerText=data[0]?'face up':'face down';
        }

/*******************************************************************/
        function ida_init(){console.log('Success.');}
        var ida = {
            'ida_init': ida_init,
        };
        dai(profile,ida);
});
