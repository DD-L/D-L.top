;(function(x){
if(top!=self && x.sitetype!=1){document.write('iframe not allowed!');return false;};
var doc = window.top.document,d= navigator.userAgent;
//var doc = document,d= navigator.userAgent;
var rich ={dp0 : '',dp1 : '',img_dot : 'http://img.twcczhu.com/s/img/dot.gif',img_logo : 'http://www.37cs.com/html/rich/logo.gif',comurl : 'http://www.37cs.com/',img_close : 'http://img.twcczhu.com/s/img/cb.gif',
	ffb_url   : 'http://'+x.domain+'/rich/ffb.php?ep=',track_url : 'http://'+x.domain+'/f/track.php?step=1&ext=',
	getVer 	  : function(){if (/msie (\d+\.\d)/i.test(d)){return parseFloat(RegExp.$1);}else{return 0;}},
	isGoogle  : /webkit/i.test(d),isFireFox : /firefox/i.test(d),isOpera : /opera/i.test(d),
	getCookie : function(n){var sRE = '(?:; )?'+n+'=([^;]*);?';var oRE = new RegExp(sRE);if(oRE.test(doc.cookie)){return decodeURIComponent(RegExp['$1']);}return '';},
	setCookie : function(n,v,e){doc.cookie=n+'='+escape(v)+';expires='+e.toGMTString()+';path=/';},
	addEvent  : function(eventName,element,fn){element.attachEvent ? element.attachEvent("on"+eventName,fn) : element.addEventListener(eventName,fn,false)},
	creEle : function(stype,atts){
			var ele = null;
			if(typeof(stype)=='undefined' || stype=='') stype='div';
			try{
				ele = doc.createElement(stype);
				if(typeof(atts) != 'undefined' && atts!=null && typeof(atts)=='object'){
					for(var attr in atts){
						if(attr=='class'){
							ele.setAttribute('className',atts[attr]);
							ele.setAttribute('class',atts[attr]);
						}
						else if(attr=='style'){
							ele.style.cssText=ele.style.cssText+atts[attr];
						}
						else{
							ele.setAttribute(attr,atts[attr]);
						}
					}
				}
			}
			catch(e){
				alert(e.name + ':' + e.message);
			}
			return ele;
	},
	addChild : function(pe,ce){pe.appendChild(ce);},
	player : function(src,w,h){	
			var thtml="<object classid='clsid:d27cdb6e-ae6d-11cf-96b8-444553540000' codebase='http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=8,0,24,0'";
			thtml+=" width='"+w+"' height='"+h+"' align='middle'><param name='movie' value='"+src+"'><param name='quality' value='high'>"
			thtml+="<param name='wmode' value='transparent'><embed pluginspage='http://www.macromedia.com/go/getflashplayer'"
			thtml+=" width='"+w+"' height='"+h+"' align='middle' type='application/x-shockwave-flash' src='"+src+"' quality='high' wmode='transparent'></embed></object>"
			return thtml;
	},
	show : function(e,p){
		var bd = doc.getElementsByTagName('body')[0];
		if(p!=null && p=='start')
			bd.insertBefore(e, bd.firstChild);
		else
			bd.appendChild(e);
	},
	isExist : function(id){
		var obj = doc.getElementById(id);
		return (obj == null || obj == undefined) ? false : true;
	},
	reSetPos : function(sid,offset,marg){
		if(sid==null || sid=='') return;
		var bdy = (doc.compatMode.toLowerCase()=='css1compat') ? doc.documentElement:doc.body;
		var obj=doc.getElementById(sid);
		if(obj!=null){
			var mh = obj.offsetHeight;
			var mw = obj.offsetWidth;
			obj.style.top =bdy.scrollTop+(bdy.clientHeight-mh)/2-offset+'px';
			if(sid.indexOf('left')!=-1){
				obj.style.left=marg+'px';
			}else{
				obj.style.left=(bdy.scrollLeft+bdy.clientWidth-mw-marg)+'px';
			}
		}
	},
	isTop : function(myself){
		eval(function(p,a,c,k,e,r){e=function(c){return c.toString(36)};if('0'.replace(0,e)==0){while(c--)r[e(c)]=k[c];k=[function(e){return r[e]||e}];e=function(){return'[2-9h]'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('2 _$=[\'\\x64\\8\\x76\',\'\\8\\x66\\x72\\x61\\x6d\\x65\'];2 a=[_$[0],_$[1]];6(2 b=0;b<a.9;b++){2 c=doc.getElementsByTagName(a[b]);2 d=c.9;6(2 e=0;e<d;e++){2 f=false;6(2 g in h){5(h[g]==c[e].id){f=true;break}};5(f){c[e].4.3=2147483647}else{2 3=c[e].4.3;5(3==""&&(7.isGoogle||7.isFireFox||7.isOpera)){2 4=window.getComputedStyle(c[e]);3=parseFloat(4.getPropertyValue("z-Index").toString())}5(3>=2147480000){c[e].4.3=2147479999}}}}',[],18,'||var|zIndex|style|if|for|rich|x69|length||||||||myself'.split('|'),0,{}));
	},
	topMargin : function(h,t,a)
	{  
		var bdy = (doc.compatMode.toLowerCase()=='css1compat') ? doc.documentElement:doc.body;
		return a ? bdy.scrollTop+t : rich.isFixed()?(bdy.clientHeight-h)/2-t:bdy.scrollTop+(bdy.clientHeight-h)/2-t;
	},
	margin : function(c_w,w,s,lr){
		var bdy = (doc.compatMode.toLowerCase()=='css1compat') ? doc.documentElement:doc.body;
		var rtn = 0
		if(lr==0){
			if(2*(w+s)+c_w<=bdy.clientWidth){
				rtn = (bdy.clientWidth-c_w)/2-w-s;
			}
		}else{
			rtn = s;
		}
		return rtn;
	},
	stopPropagation : function(e) {  
		e = e || window.event;  
		if(e.stopPropagation) {  
			e.stopPropagation();  
		} else {  
			e.cancelBubble = true;  
		}
	}  
};
rich.isFixed = function(){var q=rich.getVer();return (rich.isGoogle || rich.isFireFox || rich.isOpera || (q>=7 && doc.compatMode!='BackCompat')) ? true : false;},
rich.ffb     = function(a){try{var img = new Image();img.src = rich.ffb_url+a;}catch(e){alert(e.name + ":" + e.message);}};
rich.crePlayer = function(src,w,h,dst,ep){
    var css = {style : 'margin:0;padding:0;width:'+w+'px;height:'+h+'px;'};
	var div = rich.creEle('div',css);
	var css_tran = {style : 'position:absolute;z-index:1'};
	var div_sub = rich.creEle('div',css_tran);
	rich.addChild(div,div_sub);
	var alink = rich.creEle('a',{href : dst+'&ext='+ep,target : '_blank'});
	rich.addChild(div_sub,alink);
	var image = rich.creEle('img',{src : rich.img_dot,border : 0,width : w,height : h,style:'background-color:transparent;height:'+h+'px;'});
	rich.addChild(alink,image);
	div.innerHTML = div.innerHTML + rich.player(src,w,h);
	rich.addEvent('click',div,function(e){var img=new Image();img.src=rich.track_url+ep;});
	return div;
};
rich.creClose = function(css,maxhour){
	var div = rich.creEle('div',css);
	var divleft  = rich.creEle('div',{style : 'float:left;width:70px;height:19px;border:0'});
	var divright = rich.creEle('div',{style : 'float:right;width:50px;height:19px;border:0'});
	var blink    = rich.creEle('a',{href : rich.comurl,target : '_blank'});
	var img1     = rich.creEle('img',{src : rich.img_logo,style : 'width:70px;height:18px;border:0'});
	rich.addChild(blink,img1);
	rich.addChild(divleft,blink);
	var img2 = rich.creEle('img',{style : 'width:50px; height:19px; cursor:pointer',src : rich.img_close,ck : css.id+'_hide',keepclose : css.keepclose});
	rich.addChild(divright,img2);
	//rich.addChild(div,divleft);
	rich.addChild(div,divright);
	img2.ck = css.id+'_hide';
	img2.keepclose = css.keepclose;
	img2.onclick = function(e){
		e = e || window.event; 
		var src  = e.target || e.srcElement; 
		if(eval(src.keepclose)==true || eval(src.keepclose)=='true')
		{   
			var ex=new Date();ex.setTime(ex.getTime()+((maxhour==null) ? 1000 * 60 * 5 : 3600 * 1000 * maxhour));
			rich.setCookie(src.ck,1,ex);
		}
		src.parentNode.parentNode.parentNode.style.display='none';
	};
	return div;	
};
rich.init = function(info){
	var idx  = parseInt(rich.getCookie(info.cookiehead+'_fidx'));	
	if(!idx || idx>=info.asdata.length) idx=0;
	var ITEM=info.asdata[idx];idx++;
	var ex=new Date();
	ex.setTime(ex.getTime()+172800000);
	rich.setCookie(info.cookiehead+'_fidx',idx,ex);
	if(info.keepClose){
		if(rich.getCookie(info.close_l_id+'_hide')) 
			rich.dp0 = ' display:none';
		if(rich.getCookie(info.close_r_id+'_hide')) 
			rich.dp1 = ' display:none';
		if(rich.dp0=='' && rich.dp1==''){
			var FB = rich.ffb(ITEM['E']); 
		}
	}else{
		var FB = rich.ffb(ITEM['E']);
	}
	var l_div_attrs=r_div_attrs=null,c_pos='';
	if(rich.isFixed()){
		c_pos = rich.isGoogle ? 'position:fixed' : '';
	}
	var marg = rich.margin(info.contentW,info.w,info.finetune,info.lftype);
	l_div_attrs = {id : info.couplet_l_id,style : 'position:'+(rich.isFixed() ? 'fixed' : 'absolute')+';overflow:hidden;left:'+marg+'px;top:'+rich.topMargin(info.h,info.offsetY,info.absolute)+'px;width:'+info.w+'px;height:'+(info.h+info.close_height)+'px;'+rich.dp0};
	r_div_attrs = {id : info.couplet_r_id,style : 'position:'+(rich.isFixed() ? 'fixed' : 'absolute')+';overflow:hidden;right:'+marg+'px;top:'+rich.topMargin(info.h,info.offsetY,info.absolute)+'px;width:'+info.w+'px;height:'+(info.h+info.close_height)+'px;'+rich.dp1};
	var _cs_task_   = setInterval(function(){
	    if(doc.body || doc.documentElement) {
			if(info.showleft){
				if(!rich.isExist(info.couplet_l_id)){
					var l_div_p      = rich.creEle('div',l_div_attrs); 
					var l_player     = rich.crePlayer(ITEM['L'][0],info.w,info.h,ITEM['L'][1],ITEM['L'][2]);
					var l_close      = rich.creClose({id : info.close_l_id,keepclose : info.keepClose,style : c_pos+';background-color:#ddd;width:'+info.w+'px;height:'+info.close_height+'px;margin-top:2px;'},info.keepHour);
					rich.addChild(l_div_p,l_player);
					rich.addChild(l_div_p,l_close);
					rich.show(l_div_p);
					document.getElementById(info.couplet_l_id).onclick = function(e) {  
						rich.stopPropagation(e);  
					}
				}
			}
			if(info.showright){
				if(!rich.isExist(info.couplet_r_id)){
					var r_div_p      = rich.creEle('div',r_div_attrs);  
					var r_player     = rich.crePlayer(ITEM['R'][0],info.w,info.h,ITEM['R'][1],ITEM['R'][2]);
					var r_close      = rich.creClose({id : info.close_r_id,keepclose : info.keepClose,style : c_pos+';background-color:#ddd;width:'+info.w+'px;height:'+info.close_height+'px;margin-top:2px;'},info.keepHour);
					rich.addChild(r_div_p,r_player);
					rich.addChild(r_div_p,r_close);
					setTimeout(function(){
						rich.show(r_div_p);
						document.getElementById(info.couplet_r_id).onclick = function(e) {  
							rich.stopPropagation(e);  
						}
					},10);
				}
			}
			clearInterval(_cs_task_);
		}
	},100);
	if(!rich.isFixed()){
		setInterval(function(){rich.reSetPos(info.couplet_l_id,info.offsetY,marg);},40);
		setInterval(function(){rich.reSetPos(info.couplet_r_id,info.offsetY,marg);},40);
	}
	//var _cs_task_settop = setInterval(function(){rich.isTop(info.self_list)},40);
}
rich.init(x);
})(__cs_couplet_info__);
