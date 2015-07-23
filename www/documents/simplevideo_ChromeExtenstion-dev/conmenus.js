// file: conmenus.js 右键菜单

// A generic onclick callback function.
function genericOnClick(info, tab) {
  /*
  console.log("item " + info.menuItemId + " was clicked");
  console.log("info: " + JSON.stringify(info));
  console.log("tab: " + JSON.stringify(tab));
  */
  var url = 'http://imzker.com/' + info.linkUrl.split("://")[1];
  window.open(url);
}

// Create one test item for each context type.
//var contexts = ["page","selection","link","editable","image","video","audio"];
var contexts = ["link", "video"];
for (var i = 0; i < contexts.length; i++) {
  var context = contexts[i];
  //var title = "Test '" + context + "' menu item";
  var title = "Simple Video ->";
  var id = chrome.contextMenus.create({"title": title, "contexts":[context],
                                       "onclick": genericOnClick});
}

// Intentionally create an invalid item, to show off error checking in the
// create callback.
console.log("About to try creating an invalid item - an error about " +
            "item 999 should show up");
chrome.contextMenus.create({"title": "Oops", "parentId":999}, function() {
  if (chrome.extension.lastError) {
    console.log("Got expected error: " + chrome.extension.lastError.message);
  }
});
