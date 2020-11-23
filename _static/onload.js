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
    9: "10.",
    10: "11.",
    11: "12.",
    12: "13.",
    13: "14.",
    14: "",
    15: "",
};

const ALPHABET = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
    10: "k",
    11: "l",
    12: "m",
    13: "n",
    14: "o",
    14: "p",
    15: "q",
};

document.addEventListener("DOMContentLoaded", () => {
    /* Left menu - auto-expand current chapter  */
    let menuItems = document.querySelectorAll("nav.wy-nav-side p.caption + ul");
    menuItems.forEach((ul) => {
        if (ul.className === "current")
            ul.style.display = "block";
        else
            ul.style.display = "none";
    });

    /* Left menu - allow to expand other chapters */
    let chapters = document.querySelectorAll("nav.wy-nav-side p.caption");
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

    /* Left menu - Search */
    let search_input = '<form id="search" action="https://duckduckgo.com/"><input id="search-input" type="search" placeholder="Search..." name="q" onfocusout="onFormSubmit(); this.form"><input id="search-submit" type="submit" value="" onclick="onFormSubmit();"></form>'
    document.querySelectorAll('div[role="search"]')[0].innerHTML = search_input;

    /* Assignment - Change numbering to A, B, C, ... */
    let assignments = document.querySelectorAll('#assignments .caption-number')
    i = 0;
    for (let assignment of assignments)
        assignment.innerHTML = `Assignment ${ALPHABET[i++].toUpperCase()}.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`;
});


function onFormSubmit() {
    let query = document.getElementById("search-input");
    if (query.value) {
        query.value += ' site:python.astrotech.io';
        document.getElementById("search").submit();
        return true;
    }

}

