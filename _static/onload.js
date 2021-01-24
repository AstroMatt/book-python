const PREFIX = {
    0: "1.",
    1: "2.",
    2: "3.",
    3: "4.",
    4: "5.",
    5: "6.",
    6: "7.",
    7: "8.",
    8: "9.",
    9: "",
    10: "",
    11: "",
    12: "",
    13: "",
    14: "",
    15: "",
};

const ALPHABET = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
};

document.addEventListener("DOMContentLoaded", () => {

    /* Replace solution links to chapter */
    document.querySelectorAll('a.download').forEach( (a) => {
        let chapter = window.location.pathname.split('/')[1];
        a.innerHTML = a.innerHTML.replace('solution',  chapter);
    });



    let chapters = document.querySelectorAll("nav.wy-nav-side p.caption");
    let menuItems = document.querySelectorAll("nav.wy-nav-side p.caption + ul");

    menuItems.forEach((ul) => {
        if (ul.className === "current")
            ul.style.display = "block";
        else
            ul.style.display = "none";
    });

    chapters.forEach((chapter, i) => {
        chapter.innerHTML = `${PREFIX[i]} ${chapter.innerHTML}`;

        chapter.onclick = () => {
            let ul = chapter.nextElementSibling;

            if (ul.style.display !== "block")
                ul.style.display = "block";
            else
                ul.style.display = "none";
        }
    });

    try {
        let current_section_number = document.querySelector('#assignments h2').innerText.split(' ')[0];
        document.querySelectorAll('#assignments h3').forEach((h3) => {
            let title = h3.innerHTML.slice(current_section_number.length);
            let num = parseInt(title.substr(0, 1));
            let name = title.substr(3);
            let alpha = ALPHABET[num];
            h3.innerHTML = `<h3>${current_section_number}${alpha}. ${name}</h3>`
        });
    } catch (e) {}

    let search_input = '<iframe src="https://duckduckgo.com/search.html?site=python.astrotech.io&prefill=Search..." style="overflow:hidden;margin:0;padding:0;width:200px;height:40px;" frameborder="0"></iframe>';
    document.querySelectorAll('div[role="search"]')[0].innerHTML = search_input;
});
