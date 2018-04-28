console.log('Loading a web page');
var page = require('webpage').create();
var url = 'https://httpbin.org/get?show_env=1';
page.open(url, function (status) {
    //Page is loaded!
    phantom.exit();
});
