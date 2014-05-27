var counter=0,
$item = $( '.main-slideshow figure' ),
numItems = $item.length;

var showCurrent = function(){

  var itemToShow = Math.abs(counter%numItems);
  $item.removeClass('show');
  $item.eq(itemToShow).addClass('show');

};


$('.next').on('click', function(){
  counter ++;
  showCurrent();
}

$('.prev').on('click', function(){
  counter --;
  showCurrent();
}
