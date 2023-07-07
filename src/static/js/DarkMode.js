const toggle = document.getElementById("toggleDark");

toggle.addEventListener("click", function(){
   this.classList.toggle('bi-moon')
   if(this.classList.toggle('bi-brightness-high-fill')){
       document.body.classList.toggle("dark-mode")
       document.body.style.transition = "2s"
      
   }else {
      document.body.classList.remove("dark-mode")
      document.body.style.transition = "2s"
   }
})