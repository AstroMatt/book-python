document.addEventListener("DOMContentLoaded", function (event) {

    let lastname = document.querySelector('#id_lastname');
    lastname.value = lastname.value.toUpperCase();

    lastname.addEventListener("focus", () => {
        lastname.value = lastname.value.toUpperCase();
    })

});
