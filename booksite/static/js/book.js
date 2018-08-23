$(document).ready(function () {
    console.log("loaded");
    /**
     * Create Book
     */
    // process the form
    $('#create_bookfrm').submit(function (e) {
        // console.log("Creating the book");
        e.preventDefault();
        // get the form data
        var formData = {
            'title': $('#id_title').val(),
            'publisher': $('#id_publisher').val(),
            'author': $('#id_author').val(),
            'price': $('#id_pages').val(),
            'pages': $('#id_price').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            contentType: 'application/x-www-form-urlencoded',
            encode: true,
        };
        $.ajax({
            type: 'POST',
            url: 'create/',
            data: formData,
            dataType: 'json',
        }).done(function (data) {
            $(function () {
                /**
                 * Update book view
                 */
                $('#addbook').modal('toggle').slideUp(500);
                $("#bookdata").append(
                    '<tr id="book_row">' +
                    '<th scope="row">' + data.data['id'] + '</th>' +
                    '<td>' + data.data['title'] + '</td>' +
                    '<td>' + data.data['publisher'] + '</td>' +
                    '<td>' + data.data['author'] + '</td>' +
                    '<td>' + data.data['pages'] + '</td>' +
                    '<td>' + data.data['price'] + '</td>' +
                    '<td>' + '<input type="button" class="edit-button btn btn-primary" ' + 'id="' + data.data['id'] + '"' + 'name="edit-button' + data.data['id'] + '" value="edit">' +
                    '</td>' +
                    '<td>' + '<input type="button" class="delete-button btn btn-primary" ' + 'id="' + data.data['id'] + '"' + 'name="delete-button' + data.data['id'] + '" value="delete">' +
                    '</td>' +
                    '</tr>'
                )
            });
        });
    });

    /**
     * Update Book
     */
    $(document).on('click', '.edit-button', function (e) {
        e.preventDefault();
        btn = e.target.id;      //get clicked button
        var formData = {
            'id': btn,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        };
        $.ajax({
            type: 'POST',       // define the type of HTTP verb we want to use (POST for our form)
            url: "update/" + formData.id + "/",
            encode: true,
            contentType: 'application/x-www-form-urlencoded',
            crossDomain: false,
            dataType: 'json',
            data: formData,     // our data object
            success: function (data) {
                console.log('success', data);
            },
            error: function (exception) {
                alert('Exeption:' + exception);
            },
        });
    });
    /**
     * Delete Book
     */
    $(document).on('click', '.delete-button', function (e) {
        e.preventDefault();
        row = $(this).closest('tr');
        btn = e.target.id;      //get clicked button
        del_id = $(this).attr(btn);
        var formData = {
            'id': btn,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        };
        $.ajax({
            type: 'POST',       // define the type of HTTP verb we want to use (POST for our form)
            url: "delete/" + formData.id + "/",
            encode: true,
            contentType: 'application/x-www-form-urlencoded',
            crossDomain: false,
            dataType: 'json',
            data: formData,     // our data object
            success: function (data) {
                /**
                 * Update book view
                 */
                // console.log('success', data);
                row.fadeOut(1000, function () {
                    $(this).remove();
                });
            },
            error: function (exception) {
                alert('Exeption:' + exception);
            }
        });
    });
});

