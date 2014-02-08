<script>
var images = document.getElementsByTagName("img");
for(var i = 0; i < images.length; i++) {
    var image = images[i];
    image.onclick = function(event) {
         window.location.href = this.id + '.html';
    };
}
</script>