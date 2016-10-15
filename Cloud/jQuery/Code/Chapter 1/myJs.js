window.onload = function () {
  var divs = document.getElementsByTagName("div");
  for (var i = 0; i < divs.length; i++) {
    if (hasClass(divs[i], "poem-stanza") && !hasClass(divs[i], "highlight")) {
      divs[i].className += " highlight";
    }
  }

  function hasClass(elem, cls) {
    // /cls/这种写法匹配的就是字符串cls，而不是传入的参数
    var regClass = new RegExp(cls);
    console.log(regClass);
    return regClass.test(elem.className);
  }
};
