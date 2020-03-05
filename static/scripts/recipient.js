$(document).ready(function () {
  $("form.box").submit((e) => {
    e.preventDefault();
  });
  $('#submit').click(() => {
    const data = {
      firstName: $('#firstName').val(),
      lastName: $('#lastName').val(),
      birthDate: $('#birthDate').val(),
      phoneNumber: $('#phoneNumber').val(),
    };
    $.ajax({
      url: 'http://127.0.0.1:5000/recipient',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: function () {
        window.location = "/reminder";
      }
    });
  });
});