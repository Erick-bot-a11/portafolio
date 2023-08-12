const element = document.querySelector('.h3animado');
if(element){
  element.classList.add('animate__animated', 'animate__bounce');

  element.addEventListener('animationend', () => {
      element.classList.remove('animate__animated', 'animate__bounce');
    setTimeout(() => {
      element.classList.add('animate__animated', 'animate__bounce');
    }, 3000);
  });
}


const listaDesplegable=document.querySelector("#icono-desplegar");
const menu=document.querySelector("#nav");

if(listaDesplegable){
  listaDesplegable.addEventListener("click",desplegarLista);
}

function desplegarLista(){
  if (document.querySelector("#nav.active")) {
    menu.classList.remove("active");
  }
  else{
    menu.classList.add("active");
  }
}

