function myFunction() {
    var name, review;
    name = document.getElementById("Name").value;
    review = document.getElementById("Review").value;
    if (name === ""||review === "") {
        document.getElementById("error").innerHTML = "Please fill up the form correctly";
        document.getElementById("error").style.display = "block";
    }
    else {
        temp = document.getElementById("table").innerHTML;
        document.getElementById("table").innerHTML = temp + "<tr><td>" + name + "</td><td>" + review + "</td></tr>";
        document.getElementById("error").style.display = "none";
    }
}