const gliders = document.querySelectorAll("[id^=glider]");

gliders.forEach((glide) => {
    const glider = document.querySelector(`#${glide.id} .glider`);
  const gliderPrev = document.querySelector(`#${glide.id} .glider-prev`);
  const gliderNext = document.querySelector(`#${glide.id} .glider-next`);
  const gliderDots = document.querySelector(`#${glide.id} .dots`);

    new Glider(glider, {
        slidesToShow: 3,
        draggable: true,
        dots: gliderDots,
        arrows: {
          prev: gliderPrev,
          next: gliderNext
        }
      });
    });
// new Glider(document.querySelector('.glider'), {
//     slidesToShow: 3,
//     dots: '#dots',
//     arrows: {
//       prev: '.glider-prev',
//       next: '.glider-next'
//     }
//   });