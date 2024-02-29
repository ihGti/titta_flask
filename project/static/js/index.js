
$('.slider').slick({
    autoplay: true,
    infinite: true,
    speed: 500,
    slidesToShow: 3,
    slidesToScroll: 1,
    prevArrow: '<div class="slick-prev"></div>',
    nextArrow: '<div class="slick-next"></div>',
    centerMode: true,
    variableWidth: true,
		dots: true,
  });

    $(".slider_sJs").slick({
      arrows: true,
      infinite: true,
      speed: 500,
      slidesToShow: 4,
      slidesToScroll: 1,
      prevArrow: '<img src="/static/images/slick_prevI.png" class="slide-arrow prev-arrow">',
      nextArrow: '<img src="/static/images/slick_nextI.png" class="slide-arrow next-arrow">',
      variableWidth: true,
		  dots: true,
    });
