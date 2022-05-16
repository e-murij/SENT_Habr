let btns_like = document.querySelectorAll('#green');
let btns_dislike = document.querySelectorAll('#red');

btns_like.forEach(btn_like => {btn_like.addEventListener('click', function() {
    let btn_dislike = btn_like.parentElement.nextElementSibling.querySelector('button');

    if (btn_dislike.classList.contains('red')) {
      btn_dislike.classList.remove('red');
    }
  this.classList.toggle('green');

})});

btns_dislike.forEach(btn_dislike => {btn_dislike.addEventListener('click', function() {
    let btn_like = btn_dislike.parentElement.previousElementSibling.querySelector('button');

    if (btn_like.classList.contains('green')) {
      btn_like.classList.remove('green');
    }
  this.classList.toggle('red');

})});