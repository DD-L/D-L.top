#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def application(arg_io, query_string, ex_parm = None):
	assert isinstance(arg_io, dict) and isinstance(query_string, dict)
	TemplParse = ex_parm['TemplParse']
	templ_parse = TemplParse()
	
	import os
	root = './resource/template'
	# header
	context = {'hello_message': '"Never stop believing in yourself."'}
	templ_file = 'common/header.htm'
	doc_header, return_code = templ_parse.get_doc(root, templ_file, context)
	assert return_code

	# footer
	doc_footer, return_code = templ_parse.get_text(os.path.join(root, 'common/footer.htm'))
	assert return_code

	# body_div
	#doc_body_div, return_code = templ_parse.get_text(os.path.join(root, 'site_examples.htm'))
	#assert return_code
	
	site_examples = (
			{'title': '[渣裤]youku.com', 'title_ex': '', 'playurl': 'http://v.youku.com/v_show/id_XMzgzNTUyNTI0.html', 'apiurl': 'http://api.D-L.top/svapi/token/PublicToken/url/aHR0cDojI3YueW91a3UuY29tL3Zfc2hvdy9pZF9YTXpnek5UVXlOVEkwLmh0bWw=', 'example_xml': 'youku.xml'},
			{'title': '[you土逼]youtube.com', 'title_ex': '(请自觉翻墙)', 'playurl': 'https://www.youtube.com/watch?v=lC4JlGtkC9M', 'apiurl': 'http://api.D-L.top/svapi/token/PublicToken/url/aHR0cHM6IyN3d3cueW91dHViZS5jb20vd2F0Y2g_dj1sQzRKbEd0a0M5TQ==', 'example_xml': 'youtube.xml'},
			{'title': 'instagram.com', 'title_ex': '', 'playurl': 'https://instagram.com/p/2Q-1N5H_Gu/', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cHM6IyNpbnN0YWdyYW0uY29tL3AvMlEtMU41SF9HdS8=', 'example_xml': 'instagram.xml'},
			{'title': '[土豆]tudou.com', 'title_ex': '', 'playurl': 'http://www.tudou.com/programs/view/1lQfOXdaFPs/', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cDojI3d3dy50dWRvdS5jb20vcHJvZ3JhbXMvdmlldy8xbFFmT1hkYUZQcy8=', 'example_xml': 'tudou.xml'},
			{'title': 'v.ku6.com', 'title_ex': '', 'playurl': 'http://v.ku6.com/show/8_F5IAo4ee5HpMSwAcWNDQ...html?csrc=14_76_1', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cDojI3Yua3U2LmNvbS9zaG93LzhfRjVJQW80ZWU1SHBNU3dBY1dORFEuLi5odG1sP2NzcmM9MTRfNzZfMQ==', 'example_xml': 'v.ku6.xml'},
			{'title': 'v.pptv.com', 'title_ex': '', 'playurl': 'http://v.pptv.com/show/M5EjoD4Q2hh7ibWE.html', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cDojI3YucHB0di5jb20vc2hvdy9NNUVqb0Q0UTJoaDdpYldFLmh0bWw=', 'example_xml': 'v.pptv.xml'},
			{'title': 'ted.com', 'title_ex': '', 'playurl': 'http://www.ted.com/talks/erin_mckean_redefines_the_dictionary', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cDojI3d3dy50ZWQuY29tL3RhbGtzL2VyaW5fbWNrZWFuX3JlZGVmaW5lc190aGVfZGljdGlvbmFyeQ==', 'example_xml': 'ted.xml'},
			{'title': 'v.ifeng.com', 'title_ex': '', 'playurl': 'http://v.ifeng.com/ent/mingxing/201504/0157d604-155f-4340-a1e4-0546b4391856.shtml', 'apiurl': 'http://api.D-L.top/svapi/token/PublicToken/url/aHR0cDojI3YuaWZlbmcuY29tL2VudC9taW5neGluZy8yMDE1MDQvMDE1N2Q2MDQtMTU1Zi00MzQwLWExZTQtMDU0NmI0MzkxODU2LnNodG1s', 'example_xml': 'v.ifeng.xml'},
			{'title': 'video.sina.com.cn', 'title_ex': '', 'playurl': 'http://video.sina.com.cn/p/sports/pl/v/2015-04-17/103464845903.html', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cDojI3ZpZGVvLnNpbmEuY29tLmNuL3Avc3BvcnRzL3BsL3YvMjAxNS0wNC0xNy8xMDM0NjQ4NDU5MDMuaHRtbA==', 'example_xml': 'video.sina.xml'},
			{'title': 'v.yinyuetai.com', 'title_ex': '', 'playurl': 'http://v.yinyuetai.com/video/2055667', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cDojI3YueWlueXVldGFpLmNvbS92aWRlby8yMDU1NjY3', 'example_xml': 'v.yinyuetai.xml'},
			{'title': 'kugou.com', 'title_ex': '', 'playurl': 'http://www.kugou.com/yy/album/single/536957.html', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cDojI3d3dy5rdWdvdS5jb20veXkvYWxidW0vc2luZ2xlLzUzNjk1Ny5odG1s', 'example_xml': 'kugou.xml'},
			{'title': 'kuwo.cn', 'title_ex': '', 'playurl': 'http://www.kuwo.cn/yinyue/6416282/', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cDojI3d3dy5rdXdvLmNuL3lpbnl1ZS82NDE2MjgyLw==', 'example_xml': 'kuwo.xml'},
			{'title': 'zhanqi.tv', 'title_ex': '', 'playurl': 'http://www.zhanqi.tv/videos/lol/2015/04/18257.html', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cDojI3d3dy56aGFucWkudHYvdmlkZW9zL2xvbC8yMDE1LzA0LzE4MjU3Lmh0bWw=', 'example_xml': 'zhanqi.tv.xml'},
			{'title': 'alive.in.th', 'title_ex': '', 'playurl': 'http://alive.in.th/watch_video.php?v=BNXYGNK5SUM9', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cDojI2FsaXZlLmluLnRoL3dhdGNoX3ZpZGVvLnBocD92PUJOWFlHTks1U1VNOQ==', 'example_xml': 'alive.in.th.xml'},
			{'title': 'music.baidu.com', 'title_ex': '', 'playurl': 'http://music.baidu.com/song/122674119', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cDojI211c2ljLmJhaWR1LmNvbS9zb25nLzEyMjY3NDExOQ==', 'example_xml': 'music.baidu.xml'},
			{'title': 'bilibili.com', 'title_ex': '(B站bug尚未修复)', 'playurl': 'http://www.bilibili.com/video/av2260278/', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cDojI3d3dy5iaWxpYmlsaS5jb20vdmlkZW8vYXYyMjYwMjc4Lw==', 'example_xml': 'bilibili.xml'},
			{'title': 'freesound.org', 'title_ex': '', 'playurl': 'http://www.freesound.org/people/Corsica_S/sounds/26110/', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cDojI3d3dy5mcmVlc291bmQub3JnL3Blb3BsZS9Db3JzaWNhX1Mvc291bmRzLzI2MTEwLw==', 'example_xml': 'freesound.org.xml'},
			{'title': 'xiami.com', 'title_ex': '', 'playurl': 'http://www.xiami.com/collect/48908426?spm=a1z1s.2943601.6856193.2.gIFBds', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cDojI3d3dy54aWFtaS5jb20vY29sbGVjdC80ODkwODQyNj9zcG09YTF6MXMuMjk0MzYwMS42ODU2MTkzLjIuZ0lGQmRz', 'example_xml': 'xiami.xml'},
			{'title': 'tv.sohu.com', 'title_ex': '', 'playurl': 'http://tv.sohu.com/20150430/n412179147.shtml', 'apiurl': 'http://api.d-l.top/svapi/token/PublicToken/url/aHR0cDojI3R2LnNvaHUuY29tLzIwMTUwNDMwL240MTIxNzkxNDcuc2h0bWw=', 'example_xml': 'tv.sohu.xml'},
			{'title': '[乐视]letv.com', 'title_ex': '(注意: 乐视资源有地域限制)', 'playurl': 'http://www.letv.com/ptv/vplay/22650278.html', 'apiurl': 'http://api.D-L.top/svapi/token/PublicToken/url/aHR0cDojI3d3dy5sZXR2LmNvbS9wdHYvdnBsYXkvMjI2NTAyNzguaHRtbA==', 'example_xml': 'letv.xml'},
			{'title': '[爱奇艺]iqiyi.com', 'title_ex': '(爱奇艺站点暂时失效)', 'playurl': 'http://www.iqiyi.com/v_19rrntkwac.html', 'apiurl': 'http://api.D-L.top/svapi/token/PublicToken/url/aHR0cDojI3d3dy5pcWl5aS5jb20vdl8xOXJybnRrd2FjLmh0bWw=', 'example_xml': 'iqiyi.xml'},
			)
			#{'title': '', 'title_ex': '', 'playurl': '', 'apiurl': '', 'example_xml': ''},
	
	ymPrompt_js, return_code = templ_parse.get_text(os.path.join(root, '../js/common/ymPrompt.js'))
	assert return_code

	context = {'site_examples': site_examples, 'ymPrompt_js': ymPrompt_js}
	templ_file = 'site_examples.htm'
	doc_body_div, return_code = templ_parse.get_doc(root, templ_file, context)
	#assert return_code

	# container
	context = {'container': doc_body_div}
	templ_file = 'common/container.htm'
	doc_container, return_code = templ_parse.get_doc(root, templ_file, context)
	assert return_code

	doc = doc_header + doc_container + doc_footer
	
	arg_io['doc'] = doc
	arg_io['return_code'] = return_code
	if return_code:
		arg_io['ctype'] = 'text/html'
