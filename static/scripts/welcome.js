$(document).ready(function () {
  console.log("taco")
  $("form.box").submit((e) => {
    e.preventDefault();
  });
  $('#submitRecipient').click((e) => {
    window.location = 'recipient';
  });

  $('#submitReminder').click(() => {
    window.location = 'reminder';
  });
});