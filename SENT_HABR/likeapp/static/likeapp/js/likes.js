$(".like").on("click", addVote);
$(".dislike").on("click", addVote);

function addVote() {
    let type = $(this).attr("data-type")
    let pk = $(this).attr("data-id")
    let action = $(this).attr("class")
    let crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url : "/likes/" + type +"/" + pk + "/" + action + "/",
        type : 'POST',
        data : { 'obj' : pk,
                 'csrfmiddlewaretoken': crf_token
                },
        success : function (json) {
            if (json.redirect) window.location.href = json.redirect;
            else {
               $(`li[data-type="${type}"][data-id="${pk}"]>span[class=like_count]`).html(json.like_count);
               $(`li[data-type="${type}"][data-id="${pk}"]>span[class=dislike_count]`).html(json.dislike_count);
               if (type == "article") $(`span[class=article_rating]`).html(json.sum_rating);
               if (type == "user") $(`span[class=user_rating]`).html(json.sum_rating);
            };
        }
    });
    return false;
};