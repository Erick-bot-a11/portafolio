const element = document.querySelector('.avatar_header');
element.classList.add('animate__animated', 'animate__bounce');

element.addEventListener('animationend', () => {
    element.classList.remove('animate__animated', 'animate__bounce');
  setTimeout(() => {
    console.log("Ya acabo");
    element.classList.add('animate__animated', 'animate__bounce');
  }, 3000);
});
