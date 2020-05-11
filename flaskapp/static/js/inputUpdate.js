window.onload = function () {
    document.getElementById("file-input").onchange = function () {
        document.getElementById(
            "upload-filename"
        ).innerHTML = this.value.replace(/.*[\/\\]/, '');
    };
}