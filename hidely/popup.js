document.addEventListener('DOMContentLoaded', function() {
  var hideaction = document.getElementById('hide');
  hideaction.addEventListener('click', function() {
    function modifyDOM() {
        document.body.style.display = "none"
    }
    //We have permission to access the activeTab, so we can call chrome.tabs.executeScript:
    chrome.tabs.executeScript({
        code: '(' + modifyDOM + ')();' //argument here is a string but function.toString() returns function's code
    }, (results) => {
        //Here we have just the innerHTML and not DOM structure
        console.log('Hidden')
    });
  }, false);


  var showaction = document.getElementById('show');
  showaction.addEventListener('click', function() {
    function modifyDOM() {
        document.body.style.display = "block"
    }
    //We have permission to access the activeTab, so we can call chrome.tabs.executeScript:
    chrome.tabs.executeScript({
        code: '(' + modifyDOM + ')();' //argument here is a string but function.toString() returns function's code
    }, (results) => {
        //Here we have just the innerHTML and not DOM structure
        console.log('Showed')
    });
  }, false);
}, false);