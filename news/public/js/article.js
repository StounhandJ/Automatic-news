$(document).ready(function() {
    const urlParams = new URLSearchParams(window.location.search);
    $(`select[name="type"] option[value="${urlParams.get('type')}"]`).prop("selected", true);
    $('input[name="from"]').val(urlParams.get('from'));
    $('input[name="to"]').val(urlParams.get('to'));
    $(`input[name="verified"][value="${urlParams.get('verified')}"]`).prop("checked", true);
})