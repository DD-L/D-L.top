function yyjl(){
	var css=document.createElement('link');
	css.type='text/css';
	css.rel='stylesheet';
	css.href='http://www1.pcgames.com.cn/zt/yxsjk/css/showbox.css';
	document.getElementsByTagName('head')[0].appendChild(css);
	if(!window.pc) {
	var ele=document.createElement("script"); 
	ele.src="http://js.3conline.com/min/temp/v2/core-pc_v1.js"; 
	document.body.appendChild(ele);
	}
	document.getElementById("showbox").innerHTML ='<div class="sboxtop"></div><div class="scontent clearfix" id="showcontent"></div><div class="sboxfoot"></div>';	
}
function yycjs(){
	var yysj=0;
	for(var i=0; i<Oanum;i++){
	   //跑一遍游戏数据库的链接词,判断是不是有游戏数据库的链接
	   if(Oa[i].href.indexOf('db.pcgames.com.cn')!=-1){
		   var ncs = Oa[i].href.split("_");
		   if(ncs[1]){
			   var nsttr = ncs[1].replace('.html','');
			  if(!isNaN(nsttr)){
				   Oa[i].rel = nsttr;
				   Oa[i].className = Oa[i].className+' sw';
			   }
		   }
	   }
		if(Oa[i].rel){
			yysj=1;
		}
	}
	if(yysj==1){
		yyjl();
	 	Ocon=document.getElementById("showcontent");
	}
}
function findDimensions(){
  if (window.innerHeight)
  winHeight = window.innerHeight;
  else if ((document.body) && (document.body.clientHeight))
  winHeight = document.body.clientHeight;
  if (document.documentElement  && document.documentElement.clientHeight && document.documentElement.clientWidth)
  {
  winHeight = document.documentElement.clientHeight;
  }
  return winHeight;
}

var sh=findDimensions();

function mousePosition(ev){
  if (ev.pageX || ev.pageY) {
	  return{x:ev.pageX,y:ev.pageY}
  } else if (ev.clientX || ev.clientY) {
	  return{
	  x:ev.clientX + document.documentElement.scrollLeft + document.body.scrollLeft,
	  y:ev.clientY + document.documentElement.scrollTop + document.body.scrollTop
	  }
  };
}
 
function mouseMoveb(ev){
  ev = ev || window.event;
  var mousePos = mousePosition(ev);
	  if(document.body.scrollWidth-mousePos.x<290){
		  Obox.style.left= parseInt(mousePos.x-300)+"px";
	  }else{
		  Obox.style.left= parseInt(mousePos.x+20)+"px";
	  }
  var mainshow=parseInt(sh+getScrollTop()-mousePos.y);
	  if(mainshow<tall){
		  Obox.style.top=parseInt(mousePos.y-tall)+"px";
	  }else{
		  Obox.style.top=parseInt(mousePos.y)+"px";
	  }
}

function getScrollTop()  {  
	var scrollTop=0;  
	if(document.documentElement&&document.documentElement.scrollTop)      {  
		scrollTop=document.documentElement.scrollTop;  
	}  
	else if(document.body)      {  
		scrollTop=document.body.scrollTop;  
	}  
	return scrollTop;  
} 
function getScrollHeight(){  
    return Math.max(document.body.scrollHeight,document.documentElement.scrollHeight);  
}
function stripscript(s){
	var pattern = new RegExp("\r\n")
	var rs = "";
	for (var i = 0; i < s.length; i++) {
		rs = rs+s.substr(i, 1).replace(pattern, '');
	}
	return rs;
} 
function joinbr(str,fgf){
	var strs=str.split(fgf);
	var html="";
	for (i=0;i<strs.length ;i++ )    
		{    
			if(strs[i]!=""){
				html+=strs[i]+"<br/>"; 
			}
		}
	return html;
}
//对象转字符
function Obj2str(o) {  
	if (o == undefined) {  
	   return "";  
   }  
   var r = [];  
	if (typeof o == "string") return "\"" + o.replace(/([\"\\])/g, "\\$1").replace(/(\n)/g, "\\n").replace(/(\r)/g, "\\r").replace(/(\t)/g, "\\t") + "\"";  
   if (typeof o == "object") {  
		if (!o.sort) {  
			for (var i in o) r.push("\"" + i + "\":" + Obj2str(o[i]));  
			if ( !! document.all && !/^\n?function\s*toString\(\)\s*\{\n?\s*\[native code\]\n?\s*\}\n?\s*$/.test(o.toString)) {  
				r.push("toString:" + o.toString.toString());  
		   }  
		   r = "{" + r.join() + "}";  
		} else {  
		   for (var i = 0; i < o.length; i++) r.push(Obj2str(o[i]));  
		   r = "[" + r.join() + "]";  
		}  
	   return r;  
   }  
	return o.toString().replace(/\"\:/g, '":""');  
} 

function cldata(data){
	var html="";
	if(data.isHero=="true"){
		html+="<img src="+data.img+" />";
		html+="<div class='p'>";
		html+="<i class='t1'>"+data.first+"</i>";
		html+="<i class='t2'>"+data.five+"</i>";
		html+="<i class='t3'>";
		if(data.second!= null && data.second.length>0){
			for(var i=0;i<data.second.length;i++){
				if(data.second[i].value!=null && data.second[i].value!="undefined"){
					html+="<span style='color:"+data.second[i].color+"'> "+data.second[i].attrName+":"+data.second[i].value+"</span>";
					html+="<br>";
				}
			}
			html+="<i class='jg'></i>";
		}
		
		if(data.third!= null && data.third.length>0){
			for(var i=0;i<data.third.length;i++){
				if(data.third[i].value!= null && data.third[i].value!="undefined"){
					html+="<span style='color:"+data.third[i].color+"'> "+data.third[i].attrName+data.third[i].value+"</span>";
					html+="<br>";
				}
			}
			html+="<i class='jg'></i>";
		}
		var d6=Obj2str(data.four).replace(/\"/g, "").replace(/\\/g,"");
		d6=d6.replace("{'", "").replace("'}", "").replace("{}", "");
		if(d6!="" && d6!="undefined"){
			  html+=d6;
		  }
		
		html+="</i></div>";
	}else{
		html+="<i class='bt'>"+data.first+"</i>";
		html+="<i><p class='fr'>"+data.five+"</p>";
		if(data.second!= null && data.second.length>0){
			for(var i=0;i<data.second.length;i++){
				if(data.second[i].value!=null && data.second[i].value!="undefined"){
					if(data.second[i].color==""){data.second[i].color="#0090ff"}
					html+="<span style='color:"+data.second[i].color+"'>"+data.second[i].attrName;
					if(data.second[i].attrName!=""){
						html+="："
					}
					html+=" "+data.second[i].value+"</span>";
					html+="<br>";
				}
			}
			html+="<i class='jg'></i>";
		}
		
		
		if(data.third!= null && data.third.length>0){
			for(var i=0;i<data.third.length;i++){
				if(data.third[i].value!= null && data.third[i].value!="undefined"){
					html+="<span style='color:"+data.third[i].color+"'>"+data.third[i].attrName+" "+data.third[i].value+"</span>";
					html+="<br>";
				}
			}
			html+="<i class='jg'></i>";
		}

		var d6=Obj2str(data.four).replace(/\"/g, "").replace(/\\/g,"");
		d6=d6.replace("{'", "").replace("'}", "").replace("{}", "");
		if(d6!="" && d6!="undefined"){
			  html+=d6;
		  }

		html+="</i>";
	}
		if(data.citeRelations!= null && data.citeRelations.length>0){
			for(var i=0;i<data.citeRelations.length;i++){
				if(data.citeRelations[i].relationName!= null && data.citeRelations[i].relationName!="undefined"){
					html+="<i class='t4'>"+data.citeRelations[i].relationName+"</i>";
						if(data.citeRelations[i].relProducts!= null && data.citeRelations[i].relProducts.length>0){
							for(var j=0;j<data.citeRelations[i].relProducts.length;j++){
								html+="<i class='pic'><img src="+data.citeRelations[i].relProducts[j].relProductImg+" style='width:25px;hight:25px' /> "+data.citeRelations[i].relProducts[j].relProductName+"</i>";				
							}
						}
				}
			}
		}
		if(data.citedRelations!= null && data.citedRelations.length>0){
			for(var i=0;i<data.citedRelations.length;i++){
				if(data.citedRelations[i].relationName!= null && data.citedRelations[i].relationName!="undefined"){
					html+="<i class='t4'>"+data.citedRelations[i].relationName+"</i>";
						if(data.citedRelations[i].products!= null && data.citedRelations[i].products.length>0){
							for(var j=0;j<data.citedRelations[i].products.length;j++){
								html+="<i class='pic'><img src="+data.citedRelations[i].products[j].productImg+" style='width:25px;hight:25px' /> "+data.citedRelations[i].products[j].productName+"</i>";				
							}
						}
				}
			}
		}
		if(data.img && data.isCard==1){
			html+="<i class='kpi'><img src='"+data.img.replace("_30x30","")+"'></i>";
		}
		html+="</div>";
		return html;
}
function showbig(){
	var Theight=getScrollHeight();
	var pdt;
	for(var i=0; i<Oanum;i++){
		Oa[i].onmouseover=function(){
		if(this.rel && this.className.indexOf('sw')!=-1){
			var _this=this;
			Obox.style.display="block";
			var html="";
			Ocon.innerHTML='<div class=loding><img src=http://www1.pcgames.com.cn/zt/yxsjk/images/loadding.gif /> 内容加载中......</div>';
			if(this.getAttribute("data-title")){
				Ocon.innerHTML=this.getAttribute("data-title");
			}else{
				var urll=game_root+"/service/getProductAttrInfo.jsp?productId="+this.rel+"&ss=dfeg&t=20140429";
				//alert(url);
				 pc.need('ajax', function(){
					 pc.ajax({
						 url: urll,
						 type: 'GET',
						 dataType: 'json',
						 success: function(data){
								html=cldata(data);
								Ocon.innerHTML=html;
								_this.setAttribute("data-title",html);
						}
						}); 
				}); 
			}
			tall=parseInt(Ocon.offsetHeight);
			document.onmousemove = mouseMoveb;
		}
	}
	Oa[i].onmouseout=function(){
			Obox.style.display="none";
			Obox.style.left="-1000px";
			document.onmousemove = "";
	}
}
}
if(document.getElementById("artArea")){
	var game_root = 'http://db.pcgames.com.cn';
	var Ofather,Oa,Oanum,Obox,Ocon
	  Ofather=document.getElementById("artArea");
	 Oa=Ofather.getElementsByTagName("a");
	 Obox=document.getElementById("showbox");
	 Oanum=Oa.length;
	 yycjs();
	 tall=0;
	 showbig();
 }