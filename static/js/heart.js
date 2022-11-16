const q_heart = document.querySelector('#q-heart');

q_heart.addEventListener('click', questHeartClick)

function questHeartClick(){
    console.log('this is heart');
    done_bucket();
}


function done_bucket() {
    $.ajax({
        type: "POST",
        url: "/heart/update",
        data: {
            quest_id : 8 ,
        },
        success: function (response) {
            console.log(response)
        }
    });
}
