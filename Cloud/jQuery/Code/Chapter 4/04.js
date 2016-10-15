// 文档就绪事件
$(document).ready(function () {
  var $speech = $("div.speech");
  var defaultSize = parseFloat($speech.css("font-size"));

  // $("#switcher button").click(function () {
  //   // 获取匹配元素集合中的第一个元素的font-size属性值
  //   // parseFloat()将字符串解析为浮点数并返回
  //   var num = parseFloat($speech.css("font-size"));
  //   if (this.id == "switcher-large") {
  //     num *= 1.4;
  //   } else if (this.id == "switcher-small") {
  //     num /= 1.4;
  //   } else {
  //     num = defaultSize;
  //   }
  //   // 设置元素的font-size属性值
  //   $speech.css("font-size", num + "px");
  // });

  $("#switcher button").click(function () {
    var size = parseFloat($speech.css("font-size"));

    switch (this.id) {
      case "switcher-large": size *= 1.4; break;
      case "switcher-small": size /= 1.4; break;
      case "switcher-default": size = defaultSize;
    }
    $speech.css("font-size", size + "px");
  });

  var $paragraph = $("p").eq(1);
  var $link = $("a.more");
  $paragraph.hide();
  // $("a.more").click(function (event) {
  //   // 阻止事件的默认行为
  //   event.preventDefault();
  //   // 判断$paragraph是否隐藏
  //   if ($paragraph.is(":hidden")) {
  //     $paragraph.slideDown(800);
  //     $(this).text("read less");
  //   } else {
  //     $paragraph.slideUp(800);
  //     $(this).text("read more");
  //   }
  // });
  $link.click(function (event) {
    event.preventDefault();
    $paragraph.slideToggle(800);

    if ($link.text() == "read more") {
      $link.fadeOut(800, function () {
        $link.text("read less");
        $link.show(0);
      });
    } else {
      $link.fadeOut(800, function() {
        $link.text("read more");
        $link.show(0);
      });
    }
  });
});
