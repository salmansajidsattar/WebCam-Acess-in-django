/*var video_player = document.getElementById("videoarea"),
links = video_player.getElementsByTagName('a');
for (var i=0; i<links.length; i++) {
    links[i].onclick = handler;
}*/

function handler(e) {
    e.preventDefault();
    videotarget = this.getAttribute("href");
    filename = videotarget.substr(0, videotarget.lastIndexOf('.')) || videotarget;
    video = document.querySelector("#videoarea video");
    //video.removeAttribute("controls");
    //video.removeAttribute("poster");
    source = document.querySelectorAll("#videoarea video source");
    source[0].src = one + "one.mp4";
    source[1].src = two + "two.mp4";
    source[2].src = three + "three.mp4";

    video.load();
    video.play();    
}
