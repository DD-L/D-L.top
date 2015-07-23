/*
 * @name shareBox v1.0
 * @desc 游戏网库类页面右下角浮动栏
 * 调用方式 ：
	<div id="fixBox"></div>
	<script src="http://js.3conline.com/ue/share/games/shareBox.js"></script>
	<script>
		shareBox.init({});

		参数：
		contentWidth:[Number]页面主体内容的宽度，考虑到电脑网有多种页面尺寸，估提供参数来定义；默认为1000
		show:[Array]显示的按钮以及顺序，可选值为："tools"（工具按钮）,"share"（分享按钮）,“top”(返回顶部按钮);默认为全部显示
			eg:
			shreBox.init({
				show:["top"]//显示工具栏和返回顶部按钮
			});
	</script>
 * @author liqiang
 * @email liqiang@pconline.com.cn
 * @update
 * 	2011-11-03  增加show可选参数
 * @author ganjianwei
 * @update
 * 2013-01-04  去掉分享功能,修改设计,增加滚动一屏后显示返回顶部按钮
 * 2013-08-12  去掉工具,修改设计,简化代码
*/

(function(){
		var shareBox={
			init:function(config){
				if(!config){return;}
				this.contentWidth = config.contentWidth || 1000;
				var css=document.createElement('link');
				css.type='text/css';
				css.rel='stylesheet';
				css.href='http://js.3conline.com/ue/share/games/shareBox.css';
				document.getElementsByTagName('head')[0].appendChild(css);
				var tabObj={
					top:'<a class="top" hidefocus="true" href="javascript:;"><i class="tico"></i><i class="ttix">回顶部</i></a>'
				};
				var tabCode = '',
					show = config.show;
				if(!show){
					for( var t in tabObj){
						tabCode += tabObj[t];
					}
				}else {
					for(var i=0;i<show.length;i++){
						if (show[i]=='top') {
							tabCode = tabObj[show[i]];
						}
					}
				}
				var htmlCode =

				'<div class="tab" id="J_shareBox_top">'+
					tabCode+
				'</div>';
				if(document.getElementById('fixBox')){document.getElementById('fixBox').innerHTML = htmlCode;}

				this.fixBox = document.getElementById('fixBox');
				this.top   = document.getElementById('J_shareBox_top');
				this.addEvent(this.top,'click',this.bind(this.clickTop,this));
				this.fixLeft();//初始left值设置
				if(document.attachEvent && window.ActiveXObject && !window.XMLHttpRequest){//ie6
					if(this.needHide()){
						this.fixBox.style.display="none";
					}
					document.documentElement.style.background="url(about:blank) no-repeat fixed";//ie6下抖动
					this.addEvent(window,'scroll',this.bind(this.scrollStart,this));
					this.addEvent(window,'scroll',this.bind(this.ie6fix,this));
					this.addEvent(window,'scroll',this.bind(this.scrollHide,this));
					this.addEvent(window,'resize',this.bind(this.ie6fix,this));
				}else{
					this.addEvent(window,'scroll',this.bind(this.scrollHide,this));
					this.addEvent(window,'resize',this.bind(this.otherFix,this));
				}
			},
			clickTop:function(){
				this.goTop();
			},
			/*
			* 确保handle在指定的作用域context下执行
			* */
			bind:function(handle,context){
				return function(){
					handle.apply(context,arguments);
				}
			},
			needHide:function(){
				return document.documentElement.clientWidth<1250;
			},
			/*
			* ie6不支持fixed定位，需要重设top和left
			* */
			ie6fix:function(){
				if(this.needHide()){
					//document.title+=document.documentElement.clientWidth;
					this.fixBox.style.display="none";
					return;
				}else{
					this.fixBox.style.display="block";
				}
				this.fixLeft();
			},
			/*
			* 其他浏览器支持fixed定位，只需在resize时重设left即可
			* */
			otherFix:function(){
				this.fixLeft();
			},
			fixLeft:function(){
				var newLeft=document.documentElement.clientWidth/2 + this.contentWidth/2 +5;
				this.fixBox.style.left = newLeft+'px';
			},
			/*
			* 开始滚动时触发，用于在滚动时隐藏fixBox，避免ie6下抖动问题
			* */
			scrollStart:function(){
				var self=this;
				clearTimeout(self.scrollTimer);
				self.fixBox.style.display="none";
				this.scrollTopOld = document.documentElement.scrollTop + document.body.scrollTop;
				this.scrollTimer=setTimeout(function(){
					var scrollTopNew=document.documentElement.scrollTop + document.body.scrollTop;
					if(!self.needHide() && scrollTopNew === self.scrollTopOld){
						clearTimeout(self.scrollTimer);
						self.fixBox.style.display="block";
					}else{
						setTimeout(arguments.callee,2000);
						//self.fixBox.style.display="none";
					}
				},500);
			},
			scrollHide:function () {
				var sTop = document.documentElement.scrollTop || document.body.scrollTop;
				if (sTop>600) {
					this.top.style.display='block'
				}else {
					this.top.style.display='none'
				}
			},
			goTop:function(){
				document.documentElement.scrollTop=document.body.scrollTop=0;
			},
			addEvent:function(ele,event,handle){
				if(!ele){return;}
				if(ele.addEventListener!=undefined){
					ele.addEventListener(event,handle,false);
				}else if(ele.attachEvent!=undefined){
					ele.attachEvent('on'+event,handle);
				}
			}
		};
		window.shareBox= shareBox;
	})();