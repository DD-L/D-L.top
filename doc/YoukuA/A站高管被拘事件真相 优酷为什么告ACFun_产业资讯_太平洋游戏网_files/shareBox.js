/*
 * @name shareBox v1.0
 * @desc ��Ϸ������ҳ�����½Ǹ�����
 * ���÷�ʽ ��
	<div id="fixBox"></div>
	<script src="http://js.3conline.com/ue/share/games/shareBox.js"></script>
	<script>
		shareBox.init({});

		������
		contentWidth:[Number]ҳ���������ݵĿ�ȣ����ǵ��������ж���ҳ��ߴ磬���ṩ���������壻Ĭ��Ϊ1000
		show:[Array]��ʾ�İ�ť�Լ�˳�򣬿�ѡֵΪ��"tools"�����߰�ť��,"share"������ť��,��top��(���ض�����ť);Ĭ��Ϊȫ����ʾ
			eg:
			shreBox.init({
				show:["top"]//��ʾ�������ͷ��ض�����ť
			});
	</script>
 * @author liqiang
 * @email liqiang@pconline.com.cn
 * @update
 * 	2011-11-03  ����show��ѡ����
 * @author ganjianwei
 * @update
 * 2013-01-04  ȥ��������,�޸����,���ӹ���һ������ʾ���ض�����ť
 * 2013-08-12  ȥ������,�޸����,�򻯴���
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
					top:'<a class="top" hidefocus="true" href="javascript:;"><i class="tico"></i><i class="ttix">�ض���</i></a>'
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
				this.fixLeft();//��ʼleftֵ����
				if(document.attachEvent && window.ActiveXObject && !window.XMLHttpRequest){//ie6
					if(this.needHide()){
						this.fixBox.style.display="none";
					}
					document.documentElement.style.background="url(about:blank) no-repeat fixed";//ie6�¶���
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
			* ȷ��handle��ָ����������context��ִ��
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
			* ie6��֧��fixed��λ����Ҫ����top��left
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
			* ���������֧��fixed��λ��ֻ����resizeʱ����left����
			* */
			otherFix:function(){
				this.fixLeft();
			},
			fixLeft:function(){
				var newLeft=document.documentElement.clientWidth/2 + this.contentWidth/2 +5;
				this.fixBox.style.left = newLeft+'px';
			},
			/*
			* ��ʼ����ʱ�����������ڹ���ʱ����fixBox������ie6�¶�������
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