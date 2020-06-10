jQuery(document).ready(function ($) {
    const element = document.querySelector("#nextPage");

    element.onclick = function () {
        element.classList.remove('animate__fadeIn');
        element.classList.add('animate__fadeOut');
    };
});
