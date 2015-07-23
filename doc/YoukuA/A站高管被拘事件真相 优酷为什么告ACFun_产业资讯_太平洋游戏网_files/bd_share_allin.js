/*@update 20120427 增加pos参数选择浮窗左右位置*/
(function(){
	if(!document.getElementById('bdshare_warp')){return;}
	var bd_warp = document.getElementById('bdshare_warp');
	var titleReg=/([^_]*)_?.*/;//匹配第一个空格前的字符
	var shareTitle=document.title.replace(titleReg,"$1");
	//shareTitle=encodeURI(shareTitle);
	var pos = bd_warp.getAttribute('pos') || 'right';
	window.bds_config = {
		'bdText': shareTitle,
		"wbUid" : "1661969105",
		"snsKey" : {
		"tsina" : "736770245"
		}
	};
	
	var shareContent='<div id="bdshare" class="bdshare_t bds_tools get-codes-bdshare">'+
						'<i style="float:left;padding-top:6px;" class="iTxt">分享到：</i>'+
						'<a class="bds_qzone" href="javascript:;">QQ空间</a>'+
						'<a class="bds_tsina" href="javascript:;">新浪微博</a>'+
						'<a class="bds_tqq" href="javascript:;">腾讯微博</a>'+
						'<span class="bds_more">更多</span>'+
					'</div>';
	
	switch (document.getElementById('bdshare_warp').getAttribute('shareType')){
		case 'tools':
			document.write(shareContent);
			document.write('<script type="text/javascript" id="bdshare_js" data="type=tools&amp;img=2&amp;uid=487901&amp;pos='+pos+'" ><\/scr'+'ipt>');
			break;
			
		case 'slide':
			document.write('<script type="text/javascript" id="bdshare_js" data="type=slide&amp;img=2&amp;uid=487901&amp;pos='+pos+'" ><\/scr'+'ipt>');
			break;
			
		case 'slideTools':
			document.write(shareContent);
			document.write('<script type="text/javascript" id="bdshare_js" data="type=slide&amp;img=2&amp;uid=487901&amp;pos='+pos+'" ><\/scr'+'ipt>');
			break;
	}
	
	
	var js = document.createElement("script");
	js.src = "http://bdimg.share.baidu.com/static/js/shell_v2.js?t=" + new Date().getHours();
	document.body.insertBefore(js,document.body.firstChild);
})();
