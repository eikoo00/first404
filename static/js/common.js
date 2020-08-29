// $('.container').infiniteScroll({
//     path: '.pagination__next',
//     append: '.post',
//     history: false,
//     hideNav: '.pagination',
//   });

// $(function(){ // if document is ready
//   alert('jQuery is ready.')
// });

$(function(){
  $.fn.extend({
    random : function(num){
      return this.each(function(){
        var chn = $(this).children().hide().length;
        for(var i = 0; i < num && i < chn; i++){
          var r = parseInt(Math.random() * (chn - i)) + i;
          $(this).children().eq(r).show().prependTo($(this));
        }
      });
    }
  });

  $("[random]").each(function(){
    $(this).random($(this).attr("random"));
  });
});






$('.container').infiniteScroll({
    path: '.pagination__next',
    append: '.post',
    history: false,
    hideNav: '.pagination',
  });

// $(function(){ // if document is ready
//   alert('jQuery is ready.')
// });
