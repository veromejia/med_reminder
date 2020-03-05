$(document).ready(function () {
  $("form").submit((e) => {
    e.preventDefault();
  });
  $('#submit').click(() => {
    const data = {
      'controlSelect1': $('#controlSelect1').val(),
      'controlInput1': $('#controlInput1').val(),
      'appt': $('#appt').val(),
      'textArea1': $('#textArea1').val(),
      'startDate': $('#startDate').val(),
      'endDate': $('#endDate').val(),
    };
    $.ajax({
      url: 'http://127.0.0.1:5000/reminder',
      method: "POST",
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: function () {
        window.location = "/record";
      }
    });
  });
});