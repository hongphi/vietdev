// ----------------------------------------------------------------------------
// markItUp!
// ----------------------------------------------------------------------------
// Copyright (C) 2011 Jay Salvat
// http://markitup.jaysalvat.com/
// ----------------------------------------------------------------------------
// Html tags
// http://en.wikipedia.org/wiki/html
// ----------------------------------------------------------------------------
// Basic set. Feel free to add more tags
// ----------------------------------------------------------------------------
var mySettings = {
	onShiftEnter:  	{keepDefault:false, openWith:'\n\n'},
	onCtrlEnter:  	{keepDefault:false, openWith:'\n<p>', closeWith:'</p>'},
	onTab:    		{keepDefault:false, replaceWith:'    '},
    resizeHandle: false,
    previewParser: function(content) {
        return MarkdownParser(content);
    },
	markupSet:  [
		{name:'Bold', key:'B', openWith:'**', closeWith:'**' },
		{name:'Italic', key:'I', openWith:'_', closeWith:'_'  },
		{name:'Stroke through', key:'S', openWith:'<del>', closeWith:'</del>' },
		{separator:'---------------' },
		{name:'Bulleted List', openWith:'_', closeWith:'_'},
		{name:'Numeric List', openWith:function(markItUp) { return markItUp.line+'. '; }},
		{separator:'---------------' },
		{name:'Picture', key:'P', replaceWith:'![[![Alternative text]!]]([![Url:!:http://]!] "[![Title]!]")' },
		{name:'Link', key:'L', openWith:'[', closeWith:']([![Url:!:http://]!] "[![Title]!]")', placeHolder:'Your text to link here...' },
		{separator:'---------------' },
		{name:'Clean', className:'clean', replaceWith:function(markitup) { return markitup.selection.replace(/<(.*?)>/g, "") } },		
		{name:'Preview', className:'preview',  call:'preview'}
	]
}

function MarkdownParser(content){
    var converter = new Showdown.converter();
    return converter.makeHtml(content);
}
