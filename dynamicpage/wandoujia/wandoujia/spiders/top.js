function loadMore(){
    var loadButton = document.getElementById("j-refresh-btn");
    var loadAgain = function(){
        loadButton.click();
    }
    var timer = setInterval(function(){
        var apps = document.getElementById("j-top-list").getElementsByClassName('card');
        console.log(apps.length)
        if(apps.length > 200){
            clearInterval(timer);
        }
        loadAgain();
    },300);
}