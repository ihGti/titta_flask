
function populateDropdown(selectElement, start, end){
    for (let i = start; i <= end; i++) {
        let option = document.createElement("option");
        option.value = i;
        option.text = i;
        selectElement.appendChild(option);
    }
}

function submitBirthday(){
    let year = document.getElementById("year").value;
    let month = document.getElementById("month").value;
    let day = document.getElementById("day").value;
    let fullDate = year + "-" + month + "-" + day;
}


let yearDropdown = document.getElementById("year");
let monthDropdown = document.getElementById("month");
let dayDropdown = document.getElementById("day");

populateDropdown(yearDropdown, 1900, new Date().getFullYear());
populateDropdown(monthDropdown, 1, 12);
populateDropdown(dayDropdown, 1, 31);