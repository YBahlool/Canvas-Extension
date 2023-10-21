// ELEMENTS
const test = document.getElementById("Assignment1")
const bar = document.querySelector('bar')

Assignment1.onclick = function() {
    window.open('https://deanza.instructure.com/courses/31830/discussion_topics/671206')
}
//MainMenu.onclick = function() {
    //cdocument.getElementById("Assignment1").style.visibility = "hidden"
//}
//cdocument.getElementById("Assignment1").style.visibility = "visible"
MainMenu.onclick = function() {
  if (document.getElementById("Assignment1").style.display === "none") {
    document.getElementById("Assignment1").style.display = "block"
    document.getElementById("MainMenu").className = "is-active";

  }
   else {
    document.getElementById("Assignment1").style.display = "none"
    document.getElementById("MainMenu").className = "";
}
//2
if (document.getElementById("Assignment2").style.display === "none") {
    document.getElementById("Assignment2").style.display = "block"
  }
   else {
    document.getElementById("Assignment2").style.display = "none"

}
//3
if (document.getElementById("Assignment3").style.display === "none") {
    document.getElementById("Assignment3").style.display = "block"
  }
   else {
    document.getElementById("Assignment3").style.display = "none"
}
//Second Menu

MainMenuG.onclick = function() {
    if (document.getElementById("Grades1").style.display === "none") {
      document.getElementById("Grades1").style.display = "block"
      document.getElementById("MainMenuG").className = "is-active";
  
    }
     else {
      document.getElementById("Grades1").style.display = "none"
      document.getElementById("MainMenuG").className = "";
  }
  //2
  if (document.getElementById("Grades2").style.display === "none") {
      document.getElementById("Grades2").style.display = "block"
    }
     else {
      document.getElementById("Grades2").style.display = "none"
  
  }
  //3
  if (document.getElementById("Grades3").style.display === "none") {
      document.getElementById("Grades3").style.display = "block"
    }
     else {
      document.getElementById("Grades3").style.display = "none"
  }




}
}