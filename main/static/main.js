$(function() {
    const csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });

    $('button.tag').click(function() {
        let is_checked = $(this).data('checked');
        $(this)
            .toggleClass('btn-secondary')
            .toggleClass('btn-primary')
            .data('checked', ! is_checked);

        const method = 'post';
        const headers = {'X-CSRFToken': csrftoken};
        const body = $(this).data();
        console.log(body)
        $.post({
            url: '/api/update-tag/',
            data: body,
        });
    });
});