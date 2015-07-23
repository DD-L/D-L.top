function dev_log() {
	var msg_title = '开发日志 - SimpleVideo API';
	var msg_content = function() {/*
	 <fieldset>
		 <h4>简要记录</h4>
	 </fieldset>							 
	*/}
	var msg_height = 385;
	if (!+[1,]) msg_height = 368; // IE
	if (navigator.userAgent.indexOf("Firefox") > 0) msg_height = 355;
	ymPrompt.win({message:msg_content,width:655,height:msg_height,msgCls:'myContent',title:msg_title});
}
