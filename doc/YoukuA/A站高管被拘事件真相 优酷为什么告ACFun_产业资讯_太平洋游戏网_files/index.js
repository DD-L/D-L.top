var _ivyIDs=window._ivyIDs||"";
var _tmpIvyIDs=window._tmpIvyIDs||"";
var _cntUrl=window._cntUrl||"";
var _state_=0;
var _count_=1;
var __lock__ =0;
var _ivySubmitPage="http://tga.pcgames.com.cn/adpuba/show2?channel=inline&id=";
function _addIvyID(para_loc_ad){
	if(_tmpIvyIDs.indexOf(para_loc_ad+";")>-1){
		return;
	}

	_tmpIvyIDs = _tmpIvyIDs + para_loc_ad + ";";
	_ivyIDs = _ivyIDs + para_loc_ad + ";";
}
function _delIvyID(para_loc_ad){
	if(para_loc_ad != null && para_loc_ad.length>0 && para_loc_ad.indexOf("_")>0){
		if(_tmpIvyIDs.indexOf(para_loc_ad+";")>-1){
			_tmpIvyIDs = _tmpIvyIDs.replace(para_loc_ad+";", "");
		}
		if(_ivyIDs.indexOf(para_loc_ad+";")>-1){
			_ivyIDs = _ivyIDs.replace(para_loc_ad+";", "");
		}
	}
}
function _submitIvyID_impl(){
  __lock__ = 1;
  if (_ivyIDs && _ivyIDs != ""){
    var _ivyIDssend = _ivyIDs;
    _ivyIDs = "";
    try{
       var i2 = document.createElement("script");
       if(i2){
	  var ivydiv = document.getElementById("ivy_div");
	  if(!ivydiv){
	      //var bodys = document.getElementsByTagName("body");
	      //ivydiv = bodys[0];
              ivydiv   =   document.createElement("div");
              ivydiv.id= "ivy_div";
              ivydiv.style.display   =   "none";
              //2009.2.25...apply insertBefore for better compatiable
              //document.body.appendChild(ivydiv);
              document.body.insertBefore(ivydiv, document.body.firstChild);
	  }

	  if (!ivydiv){
    	      try{
                 var i2 = new Image(1,1);
                 i2.src = _ivySubmitPage + _ivyIDssend;
                 i2.onload=function() { _uVoid(); };
              }catch(err0){_addIvyID(_ivyIDssend);}
	  }else{
              //2009.2.25...apply insertBefore for better compatiable
	      //ivydiv.appendChild(i2);
              document.body.insertBefore(i2, document.body.firstChild);
	      var page = _ivySubmitPage + _ivyIDssend + "&state=" + _state_ + "&submitcnt=" + _count_;
	      i2.src = page;
          }
       }
    }catch(err){
        try{
	   var i2 = new Image(1,1);
           i2.src = _ivySubmitPage + _ivyIDssend;
           i2.onload=function() { _uVoid(); };
        }catch(err1){
           _addIvyID(_ivyIDssend);
        }
    }
  }
  if (_cntUrl && _cntUrl != ""){
    var i3 = new Image(1,1);
    i3.src = _cntUrl;
    i3.onload=function() { _uVoid(); };
    _cntUrl ="";
  }
  __lock__ = 0;
}
function _uVoid() { return; }
function _ivyRandom(size){
  try{
    hi_now = new Date();
    hi_id= hi_now.getSeconds() % size;
    return hi_id;
  }catch(err) {
    return 0;
  }
}
_submitIvyID=function(){ //这里特意将_submitIvyID()串分开，防止采编内嵌时被插入_addIvyID(...)串
   if(__lock__!=0){
      window.setTimeout(_submitIvyID,3000);
      return;
   }
   _state_ = 0;
   _count_ = 1;
   _submitIvyID_impl();
};

function _submitIvyID2(){
   if(__lock__!=0){
      window.setTimeout(_submitIvyID2,3000);
      return;
   }
    _state_ = 1;
   _count_ = 1;

   var needDelay= _ivyIDs&&_ivyIDs!="";
   if(needDelay) _addIvyID("480946_302688"); //用于统计未加载完页面就跳出的次数
   _submitIvyID_impl();
   if(needDelay) { var d=new Date(); while(new Date()-d<100){} } //延时100毫秒以保证请求发出，不会Abort
}
function _submitIvyID3(){
   if(__lock__!=0){
      window.setTimeout(_submitIvyID3,3000);
      return;
   }
   _state_ = 0;
   _count_ = 2;
   _submitIvyID_impl();
}
window.onbeforeunload = _submitIvyID2;

var userAgent = navigator.userAgent.toLowerCase();

if(/msie/.test(userAgent) && !/opera/.test(userAgent)){
    document.onreadystatechange = function(){
      if (document.readyState == "complete"){
     	 _submitIvyID3();
      }
    };
}else if(/opera/.test(userAgent) ||/mozilla/.test(userAgent)){
    document.addEventListener( "DOMContentLoaded", _submitIvyID3 , false );
}

function document_write(s) { document.write(s); }
function document_writeln(s) { document.writeln(s); }

//add for show3
var _IVY_AD_MAP_ = new Array();
function struct_IVY_AD_MAP(key, value){

  this.key = key;
  this.value = value;

}

function setLocationAd(key, value){

  for (var i = 0; i < this._IVY_AD_MAP_.length; i++)
  {
    if ( this._IVY_AD_MAP_[i].key === key )
    {
      this._IVY_AD_MAP_[i].value = value;
      return;
    }
  }

  this._IVY_AD_MAP_[this._IVY_AD_MAP_.length] = new struct_IVY_AD_MAP(key, value);

}

function getLocationAd(key,pex)
{
   var tmp = new Array();
   var obj = new Array();
  for (var i = 0; i < this._IVY_AD_MAP_.length; i++)
  {
    if ( this._IVY_AD_MAP_[i].key === key )
    {
      tmp = this._IVY_AD_MAP_[i].value;
	  break;
    }
  }
  if(tmp != null && tmp.length>0){
	var level = tmp[0].level;
	for(var i=0;i<tmp.length;i++){
		if(pex != null && pex>0){
			if(pex>obj.length){
				obj[obj.length] = tmp[i];
				if(tmp[i].level>=2) _addIvyID(tmp[i].locationId + "_" + tmp[i].adId);
			}
		}else{
			if(level>tmp[i].level)break;
			obj[obj.length] = tmp[i];
			if(tmp[i].level>=2) _addIvyID(tmp[i].locationId + "_" + tmp[i].adId);
			if(level<2)break;
		}
	}
  }
  return obj;
}

ivymap = window.ivymap || {}; //防重载写法，用于show4合并方式
function showIvyViaJs(locationId) {
	var _f = undefined;
	var _fconv = 'ivymap[\"'+locationId+'\"]';
	try {
		_f = eval(_fconv);
		if (_f!=undefined) {
			_f();
		}
	} catch(e) {
	}
}

/** 关键字广告保存的数组列表和回调函数 add by yjx **/
//关键字广告列表
var ivyAdList = new Array();
//关键字广告内容，key-关键字，content-广告内容，href-点击链接，ivyPara-计数参数，showCount-关键字显示次数，linkCss-链接样式
function IvyKeyword(key, content, href, ivyPara, showCount, linkCss){
	this.key = key;
	this.content = content;
	this.href = href;
	this.ivyPara = ivyPara;
	this.showCount = showCount;
	this.tmpCount = 0;
	this.linkCss = linkCss;
}

//提供给程序的回调JS函数
function showKeyWorkAd(keys, content, href, ivyPara, showCount, linkCss){
	var keyArray=keys.split("|||");
	//alert(keyArray)
	for(var aa=0;aa<keyArray.length;aa++) {
		ivyAdList[ivyAdList.length] = new IvyKeyword(keyArray[aa], content, href, ivyPara, showCount, linkCss);
	}
}

//针对inline形式出的定向投放的
function getContent(adList,keyList,areaKey,area){
	var content = "";//找出匹配的广告
	try {
		var isFind = "";
		for(var a=0;a<keyList.length;a++){//将area与KeyList比较
			if(area.indexOf(keyList[a])!= -1){isFind = keyList[a];break;}
		}
		if(isFind == "") isFind = "其他地区";//找出地区全称
		areaKey = eval(areaKey);
		var areaFind = "";
		for(var a=0;a<areaKey.length;a++){
			if(areaKey[a] != null && areaKey[a].key == isFind) {areaFind = areaKey[a].value;break;}
		}
		if(areaFind == "") return "";
		for(var a=0;a<adList.length;a++){
			if(adList[a] != null && adList[a].key.indexOf(areaFind) != -1){content = adList[a].value;break;}
		}
	} catch(e) {}
	return content;
}

/*
广告监测代码 2011-11-30
*/
(function(){
	function calljs(src) {
		var s = document.createElement('script');
		s.src=src;
		document.getElementsByTagName('head')[0].appendChild(s);
	}
	function pcc_games() {
		if (! /(^|; )u=[^;]/.test(document.cookie)) {
			var uf=document.cookie.replace(/(^|.*; )uf=([^;]+).*|.*/,"$2")
			if (uf=="") {
				document.cookie = "uf=" + ((new Date().getTime())) +
					";domain=.pcgames.com.cn;path=/;expires=Mon, 30-Nov-2099 08:00:00 GMT;";
			} else {
				var now = new Date().getTime();
				if (now - uf > 43200000) {
					calljs("http://tga.pcgames.com.cn/adpuba/online-self.jsp");
				}
			}
		} else {
			if (/(^|; )uf=[^;]/.test(document.cookie)) {
				document.cookie = "uf=1;domain=.pcgames.com.cn;path=/;expires=Thu, 01-Jan-1970 00:00:01 GMT;";
			}
		}
	}
	// call cookie functions
	// 跨域 iframe 时 top.location.href 为空
	try{
		pcc_games();
    	
        //增加访问即时生成cookie_c的功能  wyw 2013-05-17
    	if (! /(^|; )c=[^;]/.test(document.cookie)) {
	    	calljs("http://tga.pcgames.com.cn/adpuba/online-c-self.jsp");
    	}
    	// 测试弹出用的 要延时才正确
    	//setTimeout(function(){if ( /(^|; )c=[^;]/.test(document.cookie)) {
    		//alert("c===="+document.cookie.replace(/(^|.*; )c=([^;]+).*|.*/,"$2"));
    	//}},2000);
    } catch(e) {
    	
    }
})();


// 2012-08-20 关键字图片广告
var ivyImgAdList = [];

// keys: 关键字, types: ['bottom', 'side'], main:主广告内容, holder:占位图片地址, adLink：点击链接, adId：广告标识
function ivyImgAd(keys, type, main, holder, jsData, adLink, count, adId) {
	this.keys = keys.split('|||');
	this.main = main;
	this.holder = holder == 'null' ? null : holder;
	this.jsData = jsData;
	this.type = type;
	this.adLink = adLink;
	this.count = count;
	this.adId = adId;
}

/* for callback, 预处理从广告系统获取到的关键字图片广告信息 */
function showImgKeywordAd(data) {
	ivyImgAdList.push(new ivyImgAd(data.keys, data.type, data.main, data.holder, data.jsData, data.adLink, data.count, data.adid));
}