// BASE.HTML
// nav-bar
const btnToggle = document.querySelector(".btn-toggle");
const links = document.querySelector(".links");

btnToggle.addEventListener("click", function(){
    if(links.classList.contains("show-links")){
        links.classList.remove("show-links")
        links.classList.add("links")
    }else if(links.classList.contains("links")){
        links.classList.remove("links")
        links.classList.add("show-links")
    }
})
window.addEventListener("resize", function(){
    if(innerWidth > 700){
        links.classList.remove("show-links")
        links.classList.add("links")
    }
})

