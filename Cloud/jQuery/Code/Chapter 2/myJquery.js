$(document).ready(function () {
  $("#selected-plays > li").addClass("horizontal");
  $("#selected-plays li:not(.horizontal)").addClass("sub-level");
  $("a[href^='mailto:']").addClass("mailto");
  $("a[href$='.pdf']").addClass("pdflink");
  // 没有空格
  $("a[href^='http'][href*='henry']").addClass("henrylink");
  // $("tr:even").addClass("alt");
  $("tr:nth-child(odd)").addClass("alt");
});
